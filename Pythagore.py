import turtle
import time
from math import *

tortue1 = turtle.Turtle()
tortue1.color("green")
tortue1.shape("turtle")
tortue1.pensize(6)
for i in range(4):
    tortue1.showturtle()
    time.sleep(.5)
    tortue1.hideturtle()
    time.sleep(.5)
tortue1.showturtle()
a = input("Quelle est la longueur du premier côté du triangle que tu veux tracer avec ta tortue?: ")
print("D'accord! J'enregistre donc la première variable pour la formule d'égalité de Pythagore ... a = " + str(a))
print("Et je fais avancer ta tortue de " + str(a) + " hectopixels!")
time.sleep(3)
tortue1.forward(int(a)*100)
for i in range(4):
    tortue1.showturtle()
    time.sleep(.5)
    tortue1.hideturtle()
    time.sleep(.5)
tortue1.showturtle()
tortue1.left(90)
b = input("Quelle est la longueur du deuxième côté du triangle que tu veux tracer avec ta tortue?: ")
print("D'accord! J'enregistre donc la deuxième variable pour la formule d'égalité de Pythagore ... b = " + str(b))
print("Et je fais avancer ta tortue de " + str(b) + " hectopixels!")
time.sleep(3)
tortue1.forward(int(b)*100)
for i in range(4):
    tortue1.showturtle()
    time.sleep(.5)
    tortue1.hideturtle()
    time.sleep(.5)
tortue1.showturtle()
tortue1.goto(0,0)
time.sleep(3)
print("Maintenant laisse moi calculer la longueur de l'hypothénuse de ce triangle rectangle!")
for i in range(10):
    print(".")
    time.sleep(.5)
c = sqrt(int(a)**2 + int(b)**2)
print("La longueur de l'hypoténuse est..." + str(c))       


