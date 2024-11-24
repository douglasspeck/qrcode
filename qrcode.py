import turtle

def setwindowsize(x=640, y=640):
    turtle.setup(x, y)
    turtle.setworldcoordinates(0,0,x,y)

def drawpixel(x, y, color, pixelsize = 1 ):
    turtle.tracer(0, 0)
    turtle.colormode(255)
    turtle.penup()
    turtle.setpos(x*pixelsize,y*pixelsize)
    turtle.color(color)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(pixelsize)
        turtle.right(90)
    turtle.end_fill()

def showimage():
    turtle.hideturtle()
    turtle.update()

input = input("Please enter your string: ")

if len(input) > 20:
    print("The input is too long")

else:
    qrsize = 21
    qrcode = []
    for i in range(21):
        row = []
        for j in range(21):
            row.append({'value': False, 'filled': False})
        qrcode.append(row)
    chars = list(input)
    bin = []
    for char in chars:
        charbin = list(format(ord(char), '08b'))
        for i in range(len(charbin)):
            charbin[i] = int(charbin[i])
        bin += charbin
    setwindowsize(qrsize,qrsize)
    
    for i in range(7):
        for j in range(7):
            qrcode[i][j]['value'] = True
            qrcode[i][j]['filled'] = True

    for i in range(len(qrcode)):
        for j in range(len(qrcode[0])):
            if qrcode[i][j]['value']:
                color = (0, 0, 0)  # Preto
            else:
                color = (255, 255, 255)  # Branco
            drawpixel(i, j, color)
    print(qrcode)
    showimage()
    turtle.mainloop()