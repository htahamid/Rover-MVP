from turtle_simulator import TurtleSimulator


class Rover:

    def __init__(self):
        self.simulator = TurtleSimulator()

    def step(self, left_steps, right_steps):
        self.simulator.step(
            left_steps,
            right_steps
        )