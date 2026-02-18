import turtle

# --- Screen setup ---
screen = turtle.Screen()
screen.title("Polygons with Turtle")
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(6)
t.pensize(3)
t.color("white")  # outline color

# --- Helper functions ---
def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_polygon(sides, length, fill_color):
    t.fillcolor(fill_color)
    t.begin_fill()
    for _ in range(sides):
        t.forward(length)
        t.left(360 / sides)
    t.end_fill()

def write_label(text):
    t.penup()
    t.forward(10)
    t.write(text, font=("Arial", 12, "bold"))
    t.backward(10)
    t.pendown()

# --- Draw Equilateral Triangle ---
move_to(-250, 100)
draw_polygon(3, 120, "deepskyblue")
move_to(-250, 70)
t.color("white")
t.write("Equilateral Triangle", font=("Arial", 12, "bold"))

# --- Draw Rectangle (use 4 sides, but two lengths) ---
move_to(50, 120)
t.fillcolor("lime")
t.begin_fill()
for _ in range(2):
    t.forward(180)
    t.left(90)
    t.forward(100)
    t.left(90)
t.end_fill()
move_to(50, 90)
t.write("Rectangle", font=("Arial", 12, "bold"))

# --- Draw Hexagon ---
move_to(-120, -150)
draw_polygon(6, 90, "orange")
move_to(-120, -180)
t.write("Hexagon", font=("Arial", 12, "bold"))

# Hide turtle and keep window open
t.hideturtle()
turtle.done()
