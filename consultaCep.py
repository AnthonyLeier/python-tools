import requests
import json
import unidecode
import unicodedata

def buscarCeps():
    arquivo = open("ruas.txt", "w")

    for i in range(89500000, 89512999):
        request = requests.get("https://brasilapi.com.br/api/cep/v1/" + str(i))
        resposta = json.loads(request.content)
        try:
            string = str(i)+"|"+resposta['street']+"\n"
            string = unidecode.unidecode(string)
            print(string)
            arquivo.write(string)            
        except:
            string = str(i)+"|"+"Erro"+"\n"
            string = unidecode.unidecode(string)
            print(string)
            arquivo.write(string)
buscarCeps()