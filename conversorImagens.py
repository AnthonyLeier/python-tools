from PIL import Image
import os

i = 0000
print("Iniciando conversao")
print("Convertendo...")
for imagemName in os.listdir("./data_src"):
	i = i + 1
	imagem = Image.open('./data_src/' + imagemName)
	imagemName = imagemName.replace(".jpg", "")
	imagem.save("./organizadas/" + str(i) + ".png", format="PNG")
print("Conversao finalizada com sucesso")