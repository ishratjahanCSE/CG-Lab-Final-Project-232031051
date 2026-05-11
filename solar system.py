import turtle
import math

screen = turtle.Screen()
screen.title("Solar System Simulation")
screen.bgcolor("black")
screen.setup(width=700, height=600)
screen.tracer(0)


PLANETS = [
    ("Mercury", "#b5b5b5", 5,   30,  1.2,  6),
    ("Venus",   "#e8cda0", 7,   55,  1.0, 10),
    ("Earth",   "#4fa3e0", 8,   80,  0.8, 10),
    ("Mars",    "#c1440e", 6,  105,  0.6,  8),
    ("Jupiter", "#c88b3a", 14, 140,  0.3, 22),
    ("Saturn",  "#e4d191", 11, 175,  0.25, 18),
    ("Uranus",  "#7de8e8", 9,  210,  0.18, 14),
    ("Neptune", "#4b70dd", 9,  245,  0.12, 14),
]

def draw_circle(t, x, y, r, color):
    t.penup()
    t.goto(x, y - r)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()

orbit_pen = turtle.Turtle()
orbit_pen.hideturtle()
orbit_pen.speed(0)
orbit_pen.pencolor("#1a1a2e")

for _, _, _, orbit_r, _, _ in PLANETS:
    orbit_pen.penup()
    orbit_pen.goto(0, -orbit_r)
    orbit_pen.pendown()
    orbit_pen.pencolor("#1e1e3a")
    orbit_pen.pensize(1)
    orbit_pen.circle(orbit_r)

sun_pen = turtle.Turtle()
sun_pen.hideturtle()
sun_pen.speed(0)
draw_circle(sun_pen, 0, 0, 28, "#FDB813")

sun_pen.penup()
sun_pen.goto(0, -34)
sun_pen.pendown()
sun_pen.pencolor("#ffd966")
sun_pen.pensize(6)
sun_pen.pencolor("#7a5200")
sun_pen.pensize(2)
sun_pen.circle(34)

sun_pen.penup()
sun_pen.goto(0, 36)
sun_pen.pencolor("#fdb813")
sun_pen.write("Sun", align="center", font=("Arial", 9, "bold"))

planet_turtles = []
label_turtles  = []

for name, color, radius, orbit_r, speed, size in PLANETS:
    pt = turtle.Turtle()
    pt.hideturtle()
    pt.speed(0)
    pt.penup()

    lt = turtle.Turtle()
    lt.hideturtle()
    lt.speed(0)
    lt.penup()
    lt.pencolor(color)

    planet_turtles.append(pt)
    label_turtles.append(lt)

ring_pen = turtle.Turtle()
ring_pen.hideturtle()
ring_pen.speed(0)
ring_pen.pensize(2)

angles = [i * 45 for i in range(len(PLANETS))]   

info = turtle.Turtle()
info.hideturtle()
info.penup()
info.goto(-440, 420)
info.pencolor("white")
info.write("🪐  Solar System", font=("Arial", 14, "bold"))
info.goto(-440, 400)
info.pencolor("#888888")
info.write("Press  +  /  −  to speed up / slow down     Q to quit",
           font=("Arial", 9, "normal"))

state = {"speed_mult": 1.0}

def speed_up():
    state["speed_mult"] = min(state["speed_mult"] + 0.5, 6.0)

def slow_down():
    state["speed_mult"] = max(state["speed_mult"] - 0.5, 0.2)

def quit_sim():
    screen.bye()

screen.listen()
screen.onkey(speed_up,  "equal")
screen.onkey(speed_up,  "plus")
screen.onkey(slow_down, "minus")
screen.onkey(quit_sim,  "q")
screen.onkey(quit_sim,  "Q")

SATURN_INDEX = 5

while True:
    for i, (name, color, radius, orbit_r, speed, size) in enumerate(PLANETS):

        planet_turtles[i].clear()
        label_turtles[i].clear()

        angles[i] += speed * state["speed_mult"]

        rad = math.radians(angles[i])
        x = orbit_r * math.cos(rad)
        y = orbit_r * math.sin(rad)

        draw_circle(planet_turtles[i], x, y, radius, color)

        if i == SATURN_INDEX:
            ring_pen.clear()
            ring_pen.penup()
            ring_pen.goto(x - size + 2, y)
            ring_pen.pendown()
            ring_pen.pencolor("#c8a84b")
            ring_pen.pensize(2)
            steps = 30
            for s in range(steps + 1):
                a = math.radians(s * 360 / steps)
                rx = x + (size + 8) * math.cos(a)
                ry = y + (size + 8) * math.sin(a) * 0.3
                if s == 0:
                    ring_pen.penup()
                    ring_pen.goto(rx, ry)
                    ring_pen.pendown()
                else:
                    ring_pen.goto(rx, ry)

        label_turtles[i].goto(x, y + radius + 4)
        label_turtles[i].write(name, align="center", font=("Arial", 8, "normal"))

    screen.update()