import requests
from supabase import create_client, Client

class SupabaseClient:
    def __init__(self, url: str, key: str):
        self.client: Client = create_client(url, key)

    def get_contacts(self, table_name: str = 'Contacts'):
        try:
            print(f"Buscando contatos na tabela '{table_name}'...")
            
            response = self.client.table(table_name).select("nome_contato, telefone").execute()
            
            return response.data
        
        except requests.exceptions.ConnectionError as e:
            print(f"Erro de conexão com o Supabase. Verifique a URL e sua conexão com a internet. Detalhes: {e}")
            return None

        except Exception as e:
            print(f"Ocorreu um erro inesperado ao interagir com o Supabase. Detalhes: {e}")
            return None