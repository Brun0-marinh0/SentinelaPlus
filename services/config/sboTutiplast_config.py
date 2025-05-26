import urllib3
from dotenv import load_dotenv
import os

load_dotenv()

# Desativa warning de SSL (pois estamos usando verify=False)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

SAP_LOGIN_URL = os.getenv("SAP_LOGIN_URL")

LOGIN_PAYLOAD = {
    "CompanyDB": os.getenv("SAP_COMPANY_DB"),
    "UserName": os.getenv("SAP_USERNAME"),
    "Password": os.getenv("SAP_PASSWORD")
}