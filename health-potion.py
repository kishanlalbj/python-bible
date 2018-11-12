import random

name = input("Player Name: ")
health = 30
difficulty = 2

health = int(health + random.randint(10,20) / difficulty)

output = "{} has {}% of health remaining".format(name,health)

print(output)
