from moviepy.editor import VideoFileClip

print("Cortador de Vídeos")
print("Formato para Tempo (00:00:00)")
nome = input("Nome do Vídeo:")
tempoInicial = input("Tempo Inicial:")
tempoFinal = input("Tempo Final:")

horas = int(tempoInicial[0:2])
minutos = int(tempoInicial[3:5])
segundos = int(tempoInicial[6:8])

if(horas <= 60 and minutos <= 60 and segundos <= 60):
    tempoInicial = horas*60*60 + minutos*60 + segundos
else:
    print("Tempo Inválido")
    exit()

horas = int(tempoFinal[0:2])
minutos = int(tempoFinal[3:5])
segundos = int(tempoFinal[6:8])

if(horas <= 60 and minutos <= 60 and segundos <= 60):
    tempoFinal = horas*60*60 + minutos*60 + segundos
else:
    print("Tempo Inválido")
    exit()

video = VideoFileClip(nome)
cortado = video.subclip(tempoInicial, tempoFinal)
cortado.write_videofile("corte_" + nome)