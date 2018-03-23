import turtle           # Tess becomes a traffic light.

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
frank = turtle.Turtle()
dude = turtle.Turtle()


def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()


draw_housing()

tess.penup()
# Position tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)
# Turn tess into a big green circle

tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")


frank.forward(40)
frank.left(90)
frank.forward(190)

frank.shape("circle")
frank.shapesize(3)
frank.fillcolor("red")

dude.forward(40)
dude.left(90)
dude.forward(120)
dude.shape("circle")
dude.shapesize(3)
dude.fillcolor("orange")


state_num = 2


def advance_state_machine():
    global state_num
    if state_num == 0:       # Transition from state 0 to state 1
        tess.fillcolor("black")
        frank.fillcolor("black")
        dude.fillcolor("orange")
        state_num = 1
    elif state_num == 1:
        tess.fillcolor("black")
        dude.fillcolor("black")
        frank.fillcolor("red")
        state_num = 2
    else:                    # Transition from state 2 to state 0
        frank.fillcolor("black")
        dude.fillcolor("black")
        tess.fillcolor("green")
        state_num = 0

# Bind the event handler to the space key.
wn.onkey(advance_state_machine, "space")

wn.listen()                      # Listen for events
wn.mainloop()