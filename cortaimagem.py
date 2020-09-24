from PIL import Image
from matplotlib import image
from matplotlib import pyplot

from numpy import asarray
image = Image.open("imagemteste.png")

newimage = image.crop((0,0,0,100))

newimage.save("novaimagem.png", format="PNG")