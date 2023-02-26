#Bibliothèques
from pygame import mixer
from tkinter import *
import pygame

#Fenêtre
root = Tk()
root.geometry("600x300")

# Initialisation bibli
mixer.init()
mixer.music.load("nom_fichier.mp3")

#Def play + pause + reprendre + quitter
def pause():
    mixer.music.pause()

def play():
    mixer.music.play()

def resume():
    mixer.music.unpause()

#"Widgets"
Label(root, text="MP3", font="lucidia 30 bold").pack()
Button(text="|>", command=play).place(x=200, y=100)
Button(text="||", command=pause).place(x=250, y=100)
Button(text="Reprendre", command=resume).place(x=310, y=100)
Button(text="Quitter", command=quit).place(x=380, y=100)

root.mainloop()

pygame.init()
mixer.init()
screen = pygame.display.set_mode((600, 400))
mixer.music.load("nom_fichier.mp3")
mixer.music.play()
