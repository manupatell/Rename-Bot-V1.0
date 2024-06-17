import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "23032012")

API_HASH = os.environ.get("API_HASH", "5e47a644cc456147dbc79a24511c4dbb")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7264263787:AAHHNl4ljuaXUhYt4KvGn6NXOFmtQDIxAOA") 

FORCE_SUB = os.environ.get("FORCE_SUB", "WebXBots") 

DB_NAME = os.environ.get("DB_NAME","rename")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://Kanna:Kanna@cluster0.fhbau4i.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/Rename-Bot-01-15")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6704116482').split()]

PORT = os.environ.get("PORT", "8080")
