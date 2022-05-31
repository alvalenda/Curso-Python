# Exercício 21 - Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
#                descorbrir o módulo que faz isso, vou ter que pesquisar. bjos
"""
>>> from playsound import playsound
>>> playsound('/path/to/a/sound/file/you/want/to/play.mp3')
"""

# Código com playsoound >>>>>>>>>>>>>>>>>>>>>>>>>> MELHOR FORMA PARA ESSE EXERCÍCIO
from playsound import playsound
playsound('C:/Users/banys/.vscode/python/exercicios/arquivos/python.mp3')

'''
import pygame

def pmusic(file):
    pygame.init()
    pygame.mixer.init()
    clock = pygame.time.Clock()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        print("Playing...")
        clock.tick(1000)

def stopmusic():
    pygame.mixer.music.stop()


def getmixerargs():
    pygame.mixer.init()
    freq, size, chan = pygame.mixer.get_init()
    return freq, size, chan


def initMixer():
'''
# código com pygame >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ótimo aprendizado, agora funcionando
'''
from pygame import mixer
arquivo = 'C:/Users/banys/.vscode/python/exercicios/arquivos/python.mp3'

mixer.init()
mixer.music.load(arquivo)
mixer.music.play()
input('Agora você escuta? Aperte Enter para fechar.\t')
'''
# Conclusão: Apesar do pygame ser uma ferramenta muito poderosa o código com o playsound ficou mais simples e elegante
# Uma solução mais prática pro problema pedido. Porém a existência e implementação do pygame foi excelente.
