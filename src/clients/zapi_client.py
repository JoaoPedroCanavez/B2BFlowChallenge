import requests

class ZapiClient:
    def __init__(self, instance_id: str, token: str):
        self.instace_id = instance_id
        self.token = token
        self.base_url = f"https://api.z-api.io/instances/{self.instace_id}/token/{self.token}"

    def send_message(self, phone: str, message: str):
        url = f"{self.base_url}/send-text"
        payload = {
            "phone": phone,
            "message": message
        }
        headers = {
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()
            print(f"Mensagem enviada com sucesso para {phone}!")
            return response.json()
            
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                # erro 404
                print(f"Erro 404: O ID '{self.instance_id}' está incorreto ou não existe.")
            elif e.response.status_code == 403:
                # erro 403
                print(f"Erro 403: Token '{self.token}' invalido ou expirado.")
            elif e.response.status_code == 400:
                # erro 400 (Bad Request)
                print(f"Erro 400: Requisição inválida. Verifique o status da sua instância.")
            else:
                # Trata outros erros HTTP
                print(f"Erro HTTP {e.response.status_code} ao enviar a mensagem para {phone}: {e}")
            return None

        except requests.exceptions.RequestException as e:
            # exeception generico
            print(f"Erro de conexão ao enviar a mensagem: {e}")
            return None