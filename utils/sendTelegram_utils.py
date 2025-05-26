from datetime import datetime
import re


def escape_markdown(text):
    # Escapa os caracteres especiais exigidos pelo Telegram MarkdownV2
    return re.sub(r'([_\*\[\]\(\)~`>#+\-=|{}.!])', r'\\\1', text)


# padronizacao de menssagem para telegram
def build_error_message(name, url, status, aboutTheError):
    name = escape_markdown(name)
    url = escape_markdown(url)
    status = escape_markdown(str(status))
    aboutTheError = escape_markdown(aboutTheError)
    timestamp = escape_markdown(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
    
    return (
        f"⚠️ *Alerta de Falha na API*\n\n"
        f"*Nome:* {name}\n"
        f"*URL:* {url}\n"
        f"*Status HTTP:* {status}\n"
        f"*Erro:* {aboutTheError}\n\n"
        f"⏱️ *Data/Hora:* {timestamp}"
    )


def build_returnApi_message(name, url, status):
    name = escape_markdown(name)
    url = escape_markdown(url)
    status = escape_markdown(str(status))
    timestamp = escape_markdown(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
    
    return (
        f"✅ *API voltou a funcionar*\n\n"
        f"*Nome:* {name}\n"
        f"*URL:* {url}\n"
        f"*Status HTTP:* {status}\n\n"
        f"⏱️ *Data/Hora:* {timestamp}"
    )