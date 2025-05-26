# 🤖 SentinelaPlus

SentinelaPlus é um sistema de monitoramento contínuo de APIs que verifica a disponibilidade de endpoints, registra falhas no Supabase e envia alertas em tempo real via Telegram.

## 🚀 Funcionalidades

- ✅ Verificação periódica de múltiplas APIs
- ⚠️ Notificação automática para APIs com status HTTP >= 400 ou falhas de conexão
- 💾 Registro de falhas no banco de dados Supabase
- 📩 Alertas personalizados enviados para grupo ou canal do Telegram
- 🔐 Uso de `.env` para manter dados sensíveis fora do código

---

## 🛠️ Tecnologias Utilizadas

- Python 3.11+
- [Requests](https://docs.python-requests.org/en/latest/)
- Supabase REST API
- Bot do Telegram
- Monitoramento com autenticação via SessionId (SAP B1)
