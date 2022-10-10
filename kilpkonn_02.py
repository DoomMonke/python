#Alari Viilma
#10.10.22
# Harjutame kilpkonna
import turtle

aken = turtle.Screen()
aken.setup(300,300)
aken.title("Ülesanne 2 - MM")




k1 = turtle.Turtle()
for i in range (5) :
    k1.fd(100)
    k1.rt(144)
    
for i in range (3) :
    k1.color("red")
    k1.backward(100)
    k1.rt(120)
    
    
turtle.exitonclick()