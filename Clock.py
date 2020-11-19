import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width = 600, height = 600)
wn.title("Test clock for Zlata")
wn.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)

def draw_clock(h, m):

    pen.up()
    pen.goto(0, 210)
    pen.setheading(180)
    pen.color("green")
    pen.pendown()
    pen.circle(210)


    pen.penup()
    pen.goto(0, 0)
    pen.setheading(90)

    for _ in range(12):
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0, 0)
        pen.rt(30)


    pen.penup()
    pen.goto(0, 0)
    pen.color("white")
    pen.setheading(90)
    angle = (h / 12) * 360 + (m / 60) * 30
    pen.rt(angle)
    pen.pendown()
    pen.fd(100)

    pen.penup()
    pen.goto(0, 0)
    pen.color("blue")
    pen.setheading(90)
    angle = (m / 60) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(180)

    


def draw_time(time_str):
    pen.penup()
    pen.goto(0, 240)
    pen.pendown()
    pen.color("deep pink")
    style = ('Courier', 30, 'italic')
    pen.write(time_str, font=style, align='center')
    pen.hideturtle()

def draw_english(h, m):
    pen.penup()
    pen.goto(0, -280)
    pen.pendown()
    text = time_to_english(h, m)
    style = ('Courier', 30, 'italic')
    pen.write(text, font=style, align='center')
    pen.hideturtle()


def time_to_english(h, m):

    dict_n = {0: "", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", \
            6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", \
            11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", \
            15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen"}
    dict_n2  = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    hour = dict_n[h]

    if m == 0:
        m = " o'clock"
    elif m < 20:
        if m == 15:
            minutes = "quater"
        else:
            minutes = dict_n[m]
        time = minutes + " past " + hour
    elif m == 30:
        time = "half past " + hour
    elif m < 40:
        minutes = dict_n2[m // 10 - 2]
        minutes += " " + dict_n[m % 10]
        time = minutes + " past " + hour
    else:
        if h != 12:
            hour = dict_n[h + 1]
        else:
            hour = dict_n[1]
        if m == 45:
            minutes = "quater"
        elif m == 40:
            minutes = dict_n2[0]
        else:
            minutes = dict_n[60 - m]
        time = minutes + " to " + hour
    
    return time


time_str = wn.textinput("Input", "Enter time:")
h = int(time_str[:2])
m = int(time_str[3:])


wn.onclick(draw_time(time_str))
wn.listen()
wn.onclick(draw_english(h, m))
wn.listen()
wn.onclick(draw_clock(h, m))
wn.update()


wn.mainloop()


