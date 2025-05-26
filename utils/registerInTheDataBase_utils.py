from datetime import datetime

import requests
from services.config.supabase_config import SUPABASE_URL, HEADERS

def register_supabase(name, url, status, error_msg):

    error_data = {
        "name": name,
        "url": url,
        "status": status,
        "error" : error_msg,
        "created_at": datetime.now().isoformat()
    }
    try:
        resp = requests.post(
            f"{SUPABASE_URL}/rest/v1/falhas_api",
            headers=HEADERS,
            json=error_data
        )
        if resp.status_code in [200, 201]:
            return print("📄 Erro registrado no Supabase com sucesso.")
        else:
            return print(f"📄❌ Falha ao registrar no Supabase: {resp.status_code} - {resp.text}")
    except Exception as e:
        print(f"❌ Erro ao comunicar com Supabase: {e}")