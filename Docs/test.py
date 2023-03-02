
start = False

while start == False:
    name = input("What is your name? to start the game ... ")
    if name == "start":
        start = True
        print("Game started")
    else:
        print("Please type 'start' to start the game")
