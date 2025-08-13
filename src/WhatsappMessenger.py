from .clients.supabase_client import SupabaseClient
from .clients.zapi_client import ZapiClient

class WhatsappMessenger:
    def __init__(self, supabase_client: SupabaseClient, zapi_client: ZapiClient):
        self.supabase_client = supabase_client
        self.zapi_client = zapi_client

    def run(self):
        try:
            contacts = self.supabase_client.get_contacts()
            
            if not contacts:
                print("Nenhum contato para enviar mensagens.")
                return

            print(f"{len(contacts)} contatos encontrados. Iniciando o envio...")
            for contact in contacts:
                name = contact.get('nome_contato')
                phone = contact.get('telefone')

                if name and phone:
                    message = f"Olá {name}, tudo bem com você?"
                    self.zapi_client.send_message(phone, message)
                else:
                    print(f"Contato com dados incompletos: {contact}. Pulando.")
        
        except Exception as e:
            print(f"Ocorreu um erro inesperado no processo: {e}")