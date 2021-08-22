message = """
start - to start the car
stop - to stop the car
quit - to exit
"""
comand = ""
started = False

while True:
    comand = input("> ").lower()
    if comand == "help":
        print(message)
    elif comand == "start":
        if started:
            print("AVANZANDO")
        else:
            started = True
            print("car START")
    elif comand == "stop":
        if not started:
            print("car is stoped")
        else:
            started = False
            print("stoped")
    elif comand == "quit":
        break
    else:
        print("comando invalido")
