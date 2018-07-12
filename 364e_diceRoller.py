import random
import sys

# CHALLENGE 364
# DIFFICULTY: EASY
# DND DICE ROLLER
# Author: Sam Haynes
# Date: 07/12/2018

# Fairly straight forward, hardest part was figuring out how to do input in python.

def rollDice(dice, sides):
  result = 0
  for _ in range(dice):
    result += random.randint(1, sides)
  return result 

while True:
  diceRoll = input("Dice to roll: ").split('d')
  print("Result:      ", rollDice(int(diceRoll[0]), int(diceRoll[1])))