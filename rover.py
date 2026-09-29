from turtle_simulator import TurtleSimulator


class Rover:

    def __init__(self, backend=None):

        if backend is None:
            backend = TurtleSimulator()

        self.backend = backend

    def left_wheel(self, speed):
        self.backend.set_left_wheel(speed)

    def right_wheel(self, speed):
        self.backend.set_right_wheel(speed)

    def stop(self):
        self.backend.set_left_wheel(0)
        self.backend.set_right_wheel(0)

    def wait(self, seconds):
        self.backend.wait(seconds)