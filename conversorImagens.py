from PIL import Image
import os

for imagemName in os.listdir("./imagens/converter"):
	imagem = Image.open('./imagens/converter/' + imagemName)
	imagemName = imagemName.replace(".jpg", "")
	imagem.save("./imagens/convertidas/" + imagemName + ".png", format="PNG")