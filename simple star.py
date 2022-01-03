import turtle
sc=turtle.Screen()
sc.setup(600,600)
spiral= turtle.Turtle()
spiral.speed (9)
sc.bgcolor("black")
col=["yellow","red","white","grey"]
c=0
for i in range (60):
    spiral.forward(i*10)
    spiral.right(144)
    spiral.color(col[c])
    if c==3 :
        c=0
    else :
        c+=1
turtle . done()