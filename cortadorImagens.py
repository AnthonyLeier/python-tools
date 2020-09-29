from PIL import Image
import os

i = 0000
print("Iniciando corte")
print("Cortando...")

for imagemName in os.listdir("./prints"):
    i = i + 1
    imagem = Image.open('./prints/' + imagemName)
    imagem.crop((2015, 98, 2655, 993)).save("./" + str(i) + ".png", format="PNG")
    
print("Corte finalizado com sucesso")
