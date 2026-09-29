from rover import Rover


rover = Rover()

# Drive forward
rover.left_wheel(100)
rover.right_wheel(100)
rover.wait(2)

# Turn right
rover.left_wheel(100)
rover.right_wheel(30)
rover.wait(2)

# Spin
rover.left_wheel(100)
rover.right_wheel(-100)
rover.wait(1)

# Stop
rover.stop()

input("Press Enter to close simulator...")