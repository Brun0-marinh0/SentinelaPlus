import requests
import time
import urllib3

# config bot telegram
from services.config.bot_config import send_telegram

# config sbo tutiplast
from services.config.sboTutiplast_config import SAP_LOGIN_URL, LOGIN_PAYLOAD

# padronizacao de menssagem para o telegram
from utils.sendTelegram_utils import build_error_message, build_returnApi_message

from utils.registerInTheDataBase_utils import register_supabase

# lista de verificacoes
from services.myApis_services import api_urls

# tempo para verificar novamente
timeReloading = 60

# Desativa warning de SSL (pois estamos usando verify=False)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

last_status = {}

def check_sps():
    name = "Grupo SPS"
    url = "https://tutiplast.gruposps.com.br:52199/b1s/v1/Login"

    try:
        response = requests.post(SAP_LOGIN_URL, json=LOGIN_PAYLOAD, verify=False, timeout=20)
        response.raise_for_status()

        data = response.json()
        session_id = data.get("SessionId")

        if session_id:
            if last_status.get(name, 200) != 200:
                print(f"🔃 {name} voltou a funcionar.")
                message = build_returnApi_message(name, url, 200)
                send_telegram(message)
            # else:
            #     print(f"✅ Login bem-sucedido no grupo SPS.")
                

            last_status[name] = 200
        else:
            if last_status.get(name, 200) == 200:
                print(f"❌ Login no grupo SPS falhou. SessionId não encontrado.")
                register_supabase(name, url, "500", "SessionId não encontrado")

                aboutTheError = "Falha ao acessar o endpoint — resposta inválida do servidor."
                message = build_error_message(name, url, 500, aboutTheError)
                send_telegram(message)

            last_status[name] = 500

    except requests.exceptions.RequestException as e:
        if last_status.get(name, 200) == 200:
            print(f"❌ Erro ao tentar logar no Grupo SPS: {e}")
            register_supabase(name, url, "500", "Falha na requisição")

            aboutTheError = "Falha na requisição (timeout, DNS, conexão recusada, etc.)"
            message = build_error_message(name, url, 500, aboutTheError)
            send_telegram(message)

        last_status[name] = 500


# loop de verificação
while True:
    for api in api_urls:
        try:
            response = requests.get(api["url"], timeout=20, headers={"Connection": "close"})
            status_code = response.status_code

            if status_code >= 400 and status_code != 401 and status_code != 404:
                if last_status.get(api["name"], 200) == 200:
                    print(f"⚠️ erro na api {api['name']}: Status {status_code}")
                    register_supabase(api["name"], api["url"], str(status_code), "Status de erro HTTP")

                    aboutTheError = "Falha ao acessar o endpoint — resposta inválida do servidor."
                    message = build_error_message(api["name"], api["url"], status_code, aboutTheError)
                    send_telegram(message)

                last_status[api["name"]] = status_code
            else:
                if last_status.get(api["name"], 200) != 200:
                    print(f"🔃 {api['name']} voltou a funcionar.")

                    message = build_returnApi_message(api["name"], api["url"], 200)
                    send_telegram(message)
                # else:
                #     print(f"✅ {api['name']} rodando...")

                last_status[api["name"]] = 200

        except Exception as e:
            if last_status.get(api["name"], 200) == 200:
                print(f"❌ Falha ao acessar {api['name']}: {str(e)}")
                register_supabase(api["name"], api["url"], "500", "Status de erro HTTP")

                aboutTheError = "Falha na requisição (timeout, DNS, conexão recusada, etc.)"
                message = build_error_message(api["name"], api["url"], 500, aboutTheError)
                send_telegram(message)

            last_status[api["name"]] = 500

    check_sps()
    # print(f"aguardando {timeReloading}s ...")
    time.sleep(timeReloading)
    # print("continuando...")