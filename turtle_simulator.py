import turtle
import math
import time


class TurtleSimulator:

    def __init__(self):

        # Create simulator window
        self.screen = turtle.Screen()
        self.screen.title("Rover Simulator")
        self.screen.setup(width=800, height=600)

        # Manually update the screen
        self.screen.tracer(0)

        # CREATE CUSTOM ROVER SHAPE
        rover_shape = turtle.Shape("compound")

        # Main rover body
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

        # Front / nose section
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

        # Small front marker so we can easily
        # tell which direction the rover is facing
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

        # Register the finished compound shape
        self.screen.register_shape(
            "rover",
            rover_shape
        )

        # -------------------------------------------------
        # CREATE ROVER
        # -------------------------------------------------

        self.rover = turtle.Turtle()
        self.rover.shape("rover")

        self.rover.penup()

        # -------------------------------------------------
        # MOTOR VALUES
        # -------------------------------------------------

        self.left_speed = 0
        self.right_speed = 0

        # Rover position
        self.x = 0
        self.y = 0

        # Direction in radians
        self.angle = 0

        # Distance between simulated left
        # and right wheels
        self.wheel_base = 70

        # Converts motor power into
        # movement speed
        self.speed_scale = 0.8

        # Draw rover immediately
        self.update_rover_graphics()
        self.screen.update()

    # LEFT WHEEL

    def set_left_wheel(self, speed):

        self.left_speed = max(
            -100,
            min(100, speed)
        )

    # RIGHT WHEEL

    def set_right_wheel(self, speed):

        self.right_speed = max(
            -100,
            min(100, speed)
        )

    # WAIT

    def wait(self, seconds):

        end_time = time.perf_counter() + seconds
        previous_time = time.perf_counter()

        while time.perf_counter() < end_time:

            current_time = time.perf_counter()

            delta_time = (
                current_time
                - previous_time
            )

            previous_time = current_time

            self.update(delta_time)

            self.screen.update()

            # Around 60 updates per second
            time.sleep(0.016)

    # UPDATE MOVEMENT

    def update(self, delta_time):

        left_velocity = (
            self.left_speed
            * self.speed_scale
        )

        right_velocity = (
            self.right_speed
            * self.speed_scale
        )

        # Average wheel speed controls
        # forward/backward movement
        velocity = (
            left_velocity
            + right_velocity
        ) / 2

        # Difference between wheel speeds
        # controls turning
        angular_velocity = (
            right_velocity
            - left_velocity
        ) / self.wheel_base

        # Update direction
        self.angle += (
            angular_velocity
            * delta_time
        )

        # Update X position
        self.x += (
            math.cos(self.angle)
            * velocity
            * delta_time
        )

        # Update Y position
        self.y += (
            math.sin(self.angle)
            * velocity
            * delta_time
        )

        self.update_rover_graphics()

    # UPDATE GRAPHICS

    def update_rover_graphics(self):

        self.rover.goto(
            self.x,
            self.y
        )

        self.rover.setheading(
            math.degrees(self.angle)
        )