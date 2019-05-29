from blinking_light.circuit_controller import CircuitController
import os

isDev = os.path.isfile('/__devenv__.py')

print(isDev)

exit = ""
controller = CircuitController()

while exit != "y":
    try:
        selection = input("Do you want to turn on the blinker? y or n: ")

        if selection == "y":
            timeOn = input(str.format("How many seconds should the light be on before turning off (hit enter for {0})? ",controller.timeOn))
            if timeOn != "":
                controller.adjustOnTime(timeOn)

            timeOff = input(str.format("How many seconds should the light be off before turning back on (hit enter for {0})? ", controller.timeOff))
            if timeOff != "":
                controller.adjustOffTime(timeOff)
            
            selection = input("Do you want it on a timer? y or n: ")

            if selection == "y":
                seconds = input("How many total seconds should it blink? ")
                controller.blinkFor(seconds)
                
            elif selection == "n":
                controller.startBlink()
                stop = input("Press any key to stop blinking: ")
                controller.stopBlink()
                
            else:
                print("That wasn't a valid answer...\n")

        exit = input("Press any key to go again, or 'y' to exit! ")
    finally:
        controller.stopBlink()
        controller.powerOff()