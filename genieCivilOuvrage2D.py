from turtle import *
from math import *

positionFinale = 0

def setPosition(abcisse, ordonnee):
    penup()
    setposition(float(abcisse), float(ordonnee))
    pendown()
    
def cercle(rayon):
    circle(float(rayon))
    
def demiCercle(rayon):
    left(90)
    circle(float(rayon), 180)
    
def carre(cote):
    forward(float(cote))
    positionFinale = position()
    for i in range(3):
        left(90)
        forward(float(cote))
    setposition(positionFinale)
    left(90)
    
def triangle(base, coteDroit, angleDroit):
    positionInitiale = position()
    forward(base)
    left(180 - angleDroit)
    forward(coteDroit)
    goto(positionInitiale)
    
def rectangle(longueur, largeur):
    forward(float(longueur))
    positionFinale = position()
    left(90)
    forward(float(largeur))
    left(90)
    forward(float(longueur))
    left(90)
    forward(float(largeur))
    penup()
    setposition(positionFinale)
    left(90)
    pendown()
    
def polygone(nombreCotes, normeCote):
    angle = 360 / nombreCotes
    for i in range(int(nombreCotes)):
        forward(float(normeCote))
        left(angle)
    
def trapeze(grandeBase, petiteBase, coteDroit, angleBasDroit):
    positionInitiale = position()
    forward(float(grandeBase))
    positionFinale = position()
    left(180 - float(angleBasDroit))
    forward(float(coteDroit))
    left(float(angleBasDroit))
    forward(float(petiteBase))
    goto(positionInitiale)
    penup()
    setposition(positionFinale)
    left(180)
    pendown()

def losange(diagonaleVerticale, diagonaleHorizontale):
    angle = atan(diagonaleVerticale / diagonaleHorizontale)
    angle = (angle * 180) / pi
    cote = sqrt(pow((diagonaleVerticale / 2), 2) + pow((diagonaleHorizontale / 2), 2))
    right(angle)
    for i in range(2):
        forward(cote)
        left(angle * 2)
        forward(cote) 
        left((90 - angle) * 2)
    left(angle)
    
def semiEllipse(rayon):
    circle(float(rayon) / 2, 50)
    circle(float(rayon), 80)
    circle(float(rayon) / 2, 50)
    
def ellipse(rayon):
    for i in range(2):
        semiEllipse(float(rayon))
        
def support():
    left(90)
    setPosition(xcor() + 41.125, 0)
    a = position()
    left(90)
    forward(80)
    setPosition(xcor() + 41.125, 0)
    forward(105)
    b = position()
    setPosition(xcor() + 41.125, 0)
    c = position()
    forward(117)
    setPosition(xcor() + 41.125, 0)
    forward(122)
    d = position()
    setPosition(xcor() + 41.125, 0)
    e = position()
    forward(117)
    setPosition(xcor() + 41.125, 0)
    forward(105)
    f = position()
    setPosition(xcor() + 41.125, 0)
    g = position()
    forward(80)

    penup()
    goto(a)
    pendown()
    goto(b)
    goto(c)
    goto(d)
    goto(e)
    goto(f)
    goto(g)

    right(30)
    forward(57)

    penup()
    setposition(a)
    pendown()
    left(60)
    forward(57)

    setPosition(xcor() - 13, ycor() - 50)
    right(30)
    
def simpleWindow():
    rectangle(40,60)
    positionActuelle = position()
    setx(xcor() - 20)
    left(90)
    forward(60)
    penup()
    setposition(positionActuelle)
    pendown()
    right(90)
    
def shortWindow():
    fillcolor("white")
    begin_fill()
    carre(70)
    end_fill()
    setx(xcor() - 35)
    left(90)
    forward(70)
    setPosition(xcor() - 35, ycor() - 35)
    right(90)
    forward(70)
    
def longWindow():
    fillcolor("white")
    begin_fill()
    rectangle(70, 200)
    end_fill()
    setx(xcor() - 35)
    left(90)
    forward(200)
    setPosition(xcor() - 35, ycor() - 100)
    right(90)
    forward(70)
    
def windowSpace():
    fillcolor("grey")
    begin_fill()
    rectangle(100, 350)
    end_fill()
    positionActuelle = position()
    setPosition(xcor() - 85, ycor() + 10)
    longWindow()
    setPosition(xcor() - 70, ycor() + 145)
    shortWindow()
    penup()
    setposition(positionActuelle)
    pendown()