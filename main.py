import os
from dotenv import load_dotenv

from src.clients.supabase_client import SupabaseClient
from src.clients.zapi_client import ZapiClient
from src.WhatsappMessenger import WhatsappMessenger

load_dotenv()

URL = os.getenv("s_url")
KEY = os.getenv("s_Key")
ID = os.getenv("z_ID")
TOKEN = os.getenv("z_Token")

if __name__ == "__main__":
    if not all([URL, KEY, ID, TOKEN]):
        print("Erro: Verifique se todas as credenciais estão no arquivo .env.")
    else:
        try:
            supabase_client_instance = SupabaseClient(URL, KEY)
            zapi_client_instance = ZapiClient(ID, TOKEN)
            
            messenger_app = WhatsappMessenger(supabase_client_instance, zapi_client_instance)
            messenger_app.run()
        except Exception as e:
            # Captura qualquer erro inesperado que possa ter ocorrido durante a inicialização
            print(f"Ocorreu um erro fatal na aplicação: {e}")
            print("Por favor, verifique suas credenciais e a conexão com os serviços.")