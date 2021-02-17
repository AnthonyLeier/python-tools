import requests
import json
import unidecode
import unicodedata

def ultimoCep():
    arquivo = open("mapeamento.txt", "r")
    linhas = arquivo.readlines()
    arquivo.close()
    ultimaLinha = linhas[len(linhas)-1]
    cep = int(ultimaLinha[0:8])
    print("Ultimo Cep:", cep)
    return cep

def buscarCeps(cep):
    print("Continuando leitura a partir de:", cep)
    arquivo = open("mapeamento.txt", "a")

    for i in range(cep+1, 89512999):
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

cep = ultimoCep()
buscarCeps(cep)