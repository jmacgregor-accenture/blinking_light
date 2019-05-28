from blinking_light.circuit_controller import CircuitController

exit = ""
controller = CircuitController()

while exit != "y":
    selection = input("Do you want to turn on the blinker? y or n: ")

    if selection == "y":
        selection = input("Do you want it on a timer? y or n: ")

        if selection == "y":
            seconds = input("How many seconds should it run? ")
            controller.blinkFor(seconds)
        else:
            controller.startBlink()
            stop = input("Press any key to stop blinking: ")
            controller.stopBlink()

    exit = input("Enter y to exit, any other key to go again! ")
