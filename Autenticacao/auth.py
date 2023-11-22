from requests_pkcs12 import post
from dotenv import load_dotenv
import os

caminho_script = os.path.dirname(os.path.abspath(__file__))
caminho_pasta_pai = os.path.dirname(caminho_script)

certificado_path = os.path.join(caminho_pasta_pai, 'arquivo certificado', 'seu_certificado_digital.pfx')
senha_path = os.path.join(caminho_pasta_pai, 'arquivo certificado','.env' )

# Carrega o arquivo .env
load_dotenv(senha_path)

# Atribui o valor da variável de ambiente a uma variável Python
SENHA_CERTIFICADO_PFX = os.getenv("senha_certificado")

# Configurar os headers de acordo com a documentação
## IMPEXP = Declarante importador/exportador (despachantes)

headers = {
    'Role-Type': 'IMPEXP',
}

url = 'https://portalunico.siscomex.gov.br/portal/api/autenticar'

r = post(url, headers=headers,pkcs12_filename=certificado_path, pkcs12_password= SENHA_CERTIFICADO_PFX)

set_token = r.headers.get('Set-Token')
set_x_CSRF = r.headers.get('X-CSRF-Token')

""""
Toda requisição que fizer para consumir dados da API do portal unico, usarão essas variaveis abaixo nos headers da requisição. Ficará algo parecido com isso

    def configurar_api(self):
        payload = {}
        headers = {
            'Authorization': set_token,
            'X-CSRF-Token': set_x_CSRF,
        }
        response = requests.get(self.url_api, headers=headers, data=payload)
        return response
"""

print("Variavel Set-Token:", r.headers.get('Set-Token'))
print("Variavel X-CSRF-Token:", r.headers.get('X-CSRF-Token'))