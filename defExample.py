import os
import sys
import time
import yaml


print("wait for it...")
time.sleep(2)
os.system('cls')

name="FooBar" # This is a global variable

def SayHello(name): # This is a local variable
    print("Hello " + name) # This uses a local variable

SayHello(name) #

moves = ["north", "south", "east", "west"]

def move(direction): # This is a local variable
    if direction in moves: 
        print("You move " + direction) 
    else:
        print("You can't move that way")

playerDirection = input("What direction do you want to move? ")
move(playerDirection)

inventory=[] 

def addItem(item):
    print("---Adding " + item + " to inventory---")
    inventory.append(item)
    moreItems = input("Do you want to add more items? (y/n) ")
    if moreItems == "y":
        item = input("What item do you want to add? ")
        addItem(item)
    else:
        print("Inventory: " + str(inventory))

addItem("sword") 



enemyDict={"name":"Goblin", "health":10, "attack":2, "defense":1}

print("Name of enemy: " + enemyDict["name"])

enemies={"Goblin":{"health":10, "attack":2, "defense":1}, "Orc":{"health":15, "attack":3, "defense":2}, "Troll":{"health":20, "attack":4, "defense":3}}

for i in enemies:
    print("Name of enemy: " + i)
    print("Health of enemy: " + str(enemies[i]["health"]))
    print("Attack of enemy: " + str(enemies[i]["attack"]))
    print("Defense of enemy: " + str(enemies[i]["defense"]))
    print("")






