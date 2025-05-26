from dotenv import load_dotenv
import os

load_dotenv()

# config supabase
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

HEADERS = {
   "apikey": SUPABASE_KEY,
   "Authorization": f"Bearer {SUPABASE_KEY}",
   "Content-Type": "application/json",
   "Prefer": "return=minimal"
}