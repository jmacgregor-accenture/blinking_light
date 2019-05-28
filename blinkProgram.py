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
        elif selection == "n":
            controller.startBlink()
            stop = input("Press any key to stop blinking: ")
            controller.stopBlink()
        else:
            print("That wasn't a valid answer...\n")
    exit = input("Press any key to go again, or 'y' to exit! ")
