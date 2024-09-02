import random

players = input("Enter the name of players in comma separated fashion:")
playersList = players.split(",")

randIndex = random.randint(0, len(playersList) - 1)
print(randIndex, len(playersList))
print(f"{playersList[randIndex]} will pay for the dinner")