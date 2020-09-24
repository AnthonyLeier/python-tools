from PIL import Image

image = Image.open("./imagens/convertidas/foto1.png")
largura, altura = image.size
image.crop((largura/2, 0, largura, altura)).save("./imagens/corte.png", format="PNG")