import turtle
import math
import time


class TurtleSimulator:

    def __init__(self):

        # -----------------------------------
        # WINDOW
        # -----------------------------------

        self.screen = turtle.Screen()
        self.screen.title("Rover Simulator")

        self.screen.setup(
            width=800,
            height=600
        )

        self.screen.bgcolor("white")

        # We manually refresh the screen
        self.screen.tracer(0)

        # -----------------------------------
        # CREATE ROVER SHAPE
        # -----------------------------------

        rover_shape = turtle.Shape("compound")

        # Main body
        body = (
            (-30, -20),
            (25, -20),
            (35, -10),
            (35, 10),
            (25, 20),
            (-30, 20)
        )

        rover_shape.addcomponent(
            body,
            "darkgreen",
            "black"
        )

        # Front nose
        nose = (
            (20, -12),
            (38, -7),
            (38, 7),
            (20, 12)
        )

        rover_shape.addcomponent(
            nose,
            "green",
            "black"
        )

        # Top-left wheel
        wheel_1 = (
            (-25, 20),
            (-5, 20),
            (-5, 28),
            (-25, 28)
        )

        rover_shape.addcomponent(
            wheel_1,
            "black",
            "black"
        )

        # Bottom-left wheel
        wheel_2 = (
            (-25, -28),
            (-5, -28),
            (-5, -20),
            (-25, -20)
        )

        rover_shape.addcomponent(
            wheel_2,
            "black",
            "black"
        )

        # Top-right wheel
        wheel_3 = (
            (8, 20),
            (28, 20),
            (28, 28),
            (8, 28)
        )

        rover_shape.addcomponent(
            wheel_3,
            "black",
            "black"
        )

        # Bottom-right wheel
        wheel_4 = (
            (8, -28),
            (28, -28),
            (28, -20),
            (8, -20)
        )

        rover_shape.addcomponent(
            wheel_4,
            "black",
            "black"
        )

        # Front direction marker
        front_marker = (
            (26, -5),
            (34, 0),
            (26, 5)
        )

        rover_shape.addcomponent(
            front_marker,
            "yellow",
            "black"
        )

        self.screen.register_shape(
            "rover",
            rover_shape
        )

        # -----------------------------------
        # CREATE ROVER
        # -----------------------------------

        self.rover = turtle.Turtle()

        self.rover.shape("rover")
        self.rover.penup()
        self.rover.tiltangle(90)
        
        # -----------------------------------
        # ROVER POSITION
        # -----------------------------------

        self.x = 0
        self.y = 0

        # Angle is stored in radians
        self.angle = math.radians(90)

        # Distance between left and
        # right wheels
        self.wheel_base = 70

        # How far one simulated motor
        # step moves a wheel
        self.distance_per_step = 0.5

        # How quickly steps are animated
        self.step_delay = 0.005

        self.update_rover_graphics()

        self.screen.update()

    # -----------------------------------
    # STEPPER MOTOR COMMAND
    # -----------------------------------

    def step(
        self,
        left_steps,
        right_steps
    ):

        left_steps = int(left_steps)
        right_steps = int(right_steps)

        total_cycles = max(
            abs(left_steps),
            abs(right_steps)
        )

        if total_cycles == 0:
            return

        left_counter = 0
        right_counter = 0

        for _ in range(total_cycles):

            left_distance = 0
            right_distance = 0

            # --------------------------------
            # LEFT STEPPER MOTOR
            # --------------------------------

            left_counter += abs(left_steps)

            if left_counter >= total_cycles:

                left_counter -= total_cycles

                if left_steps > 0:
                    left_distance = (
                        self.distance_per_step
                    )

                elif left_steps < 0:
                    left_distance = (
                        -self.distance_per_step
                    )

            # --------------------------------
            # RIGHT STEPPER MOTOR
            # --------------------------------

            right_counter += abs(right_steps)

            if right_counter >= total_cycles:

                right_counter -= total_cycles

                if right_steps > 0:
                    right_distance = (
                        self.distance_per_step
                    )

                elif right_steps < 0:
                    right_distance = (
                        -self.distance_per_step
                    )

            # Move rover based on what
            # each motor did
            self.move_wheels(
                left_distance,
                right_distance
            )

            self.screen.update()

            time.sleep(
                self.step_delay
            )

    # -----------------------------------
    # DIFFERENTIAL DRIVE MOVEMENT
    # -----------------------------------

    def move_wheels(
        self,
        left_distance,
        right_distance
    ):

        # Average movement determines
        # forward/backward distance
        distance = (
            left_distance
            + right_distance
        ) / 2

        # Difference determines rotation
        angle_change = (
            right_distance
            - left_distance
        ) / self.wheel_base

        self.angle += angle_change

        # Calculate new X position
        self.x += (
            math.cos(self.angle)
            * distance
        )

        # Calculate new Y position
        self.y += (
            math.sin(self.angle)
            * distance
        )

        self.update_rover_graphics()

    # -----------------------------------
    # UPDATE TURTLE
    # -----------------------------------

    def update_rover_graphics(self):

        self.rover.goto(
            self.x,
            self.y
        )

        self.rover.setheading(
            math.degrees(self.angle)
        )