from rover import Rover


rover = Rover()


# -----------------------------------
# STUDENT FUNCTIONS
# -----------------------------------

def forward(steps):

    rover.step(
        steps,
        steps
    )


def reverse(steps):

    rover.step(
        -steps,
        -steps
    )


def turn_left(steps):

    rover.step(
        -steps,
        steps
    )


def turn_right(steps):

    rover.step(
        steps,
        -steps
    )


# -----------------------------------
# STUDENT PROGRAM
# -----------------------------------

forward(200)

turn_left(100)

forward(150)

turn_right(100)

reverse(100)


input("Press Enter to close simulator...")