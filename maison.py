from genieCivilOuvrage2D import *

speed(2000)

# reglages initiaux

# configurer la tortue en mode cachee
hideturtle()
# initialisation de la posion
setPosition(-500, -280)

# facade de la maison 
fillcolor("whitesmoke")
begin_fill()
rectangle(1000, 400)
end_fill()

# definition de la couleur du bas de la maison en blanc 
setPosition(-500, -280)
fillcolor("white")
begin_fill()
rectangle(1000, 10)
end_fill()

# definition de la couleur du centre de la maison en blanc
setPosition(-100, -270)
fillcolor("white")
begin_fill()
rectangle(200, 390)
end_fill()

# rectangle au niveau de la porte en gris clair
setPosition(-80, -200)
fillcolor("lightgrey")
begin_fill()
rectangle(160, 310)
end_fill()

setPosition(-500, -270)
forward(1000)

# limitation des espaces pour les fenetres
penup()
setx(-100)
pendown()
left(90)
forward(390)
setPosition(100, -270)
forward(390)

# trapeze de support du toit
setPosition(560, 160)
left(90)
fillcolor("whitesmoke")
begin_fill()
trapeze(1120, 1000, 73, 33)
end_fill()

# rectangle du toit
setPosition(-340, 160)
left(180)
rectangle(680, 80)
setPosition(-160, 160)
left(90)
forward(80)
setPosition(160, 160)
forward(80)

# trapeze de cloture du toit
setPosition(-340, 240)
right(90)
fillcolor("yellowgreen")
begin_fill()
trapeze(680, 500, 104, 30)
end_fill()

# traits de finition du toit
pensize(3)
setPosition(-340, 240)
forward(180)
setPosition(160, 240)
forward(180)
setPosition(-160, 240)
left(150)
forward(104)
setPosition(160, 240)
right(120)
forward(104)
pensize(1)

# elaboration des petites fenetres droites et gauches du toit 
setPosition(-340, 160)
right(30)
for i in range(3):
    setx(xcor() + 15)
    simpleWindow()
setPosition(160, 160)
for i in range(3):
    setx(xcor() + 15)
    simpleWindow()
    
# elaboration des fenetres de la facade
setPosition(-500, -260)
for i in range(3):
    penup()
    setx(xcor() + 25)
    pendown()
    windowSpace()
setPosition(90, -260)
for i in range(3):
    penup()
    setx(xcor() + 28)
    pendown()
    windowSpace()
    
# elaboration des escaliers a l'entree
setPosition(-90, -270)
longueurRectangle = 180
for i in range(6):
    fillcolor("white")
    begin_fill()
    rectangle(longueurRectangle, 10)
    end_fill()
    longueurRectangle -= 10
    setPosition(xcor() - (longueurRectangle + 5), ycor() + 10)
    
# elaboration des finition du bas de la porte
setPosition(-92, -270)
left(90)
forward(60)
setPosition(92, -270)
forward(60)
setPosition(-100, -210)
right(90)
forward(200)
setPosition(-100, -200)
pensize(2)
forward(200)
pensize(1)
setPosition(-60, -210)
left(90)
forward(10)
setPosition(60, -210)
forward(10)

# finition aux abords de a porte
setPosition(-90, -200)
forward(310)
setPosition(-80, -200)
forward(310)
setPosition(80, -200)
forward(310)
setPosition(90, -200)
forward(310)

# la porte
setPosition(-60, -200)
right(90)
fillcolor("white")
begin_fill()
rectangle(120, 160)
end_fill()
setx(xcor() - 60)
left(90)
forward(160)
setPosition(xcor() - 60, ycor() - 80)
right(90)
forward(120)

# la pancarte
setPosition(-120, 110)
fillcolor("white")
begin_fill()
rectangle(240, 50)
end_fill()

# les fenetres centrales du toit
setPosition(-145, 160)
for i in range(5):
    setx(xcor() + 15)
    simpleWindow()
    
# le haut de la porte
setPosition(60, -50)
demiCercle(60)

# peit cercle noir au dessus de la porte
setPosition(-10, 30)
fillcolor("black")
begin_fill()
circle(10)
end_fill()

# petite fenetre au dessus de la porte
setPosition(-35, 50)
left(90)
fillcolor("white")
begin_fill()
rectangle(70, 50)
end_fill()
setx(xcor() - 35)
left(90)
forward(50)

done()