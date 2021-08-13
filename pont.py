from genieCivilOuvrage2D import *

speed(2000)

# reglages initiaux

# initialisation de la posion
penup()
positionInitiale = setx(-150)
pendown()
# configurer la tortue en mode cachee
hideturtle()
# modifier la couleur
color("blue")
# augmenter la taille du crayon
pensize(2)

# tracage des arcs du pont
for i in range(3):
    left(90)
    semiEllipse(200)
    
    support()
    
    penup()
    setx(xcor() + (3.29 * 200))
    pendown()
    right(90)

# tracage de base du pont
setPosition(-479, 0)
pensize(3)
forward(987)

# etablissement des soutiens du pont

# premier
setPosition(-191.125, -20)
fillcolor("blue")
begin_fill()
rectangle(82.25, 20)
end_fill()
setPosition(xcor() - 102.25, -40)
fillcolor("blue")
begin_fill()
rectangle(122.25, 20)
end_fill()

# second
setPosition(137.875, -20)
fillcolor("blue")
begin_fill()
rectangle(82.25, 20)
end_fill()
setPosition(xcor() - 102.25, -40)
fillcolor("blue")
begin_fill()
rectangle(122.25, 20)
end_fill()

done()