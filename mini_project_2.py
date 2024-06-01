# -*- coding: utf-8 -*-
import random


def roll():
  die1 = random.randint(1, 6)
  die2 = random.randint(1, 6)
  s = die1 + die2
  print(f"Die1: {die1}, die2: {die2}, sum: {s}")
  return s


res = roll()
if res == 7 or res == 11:
  print("You win!")
if res == 2 or res == 3 or res == 12:
  print("You lose. Game over")
else:
  goal = res
  print(f"New goal is {goal}")
  while True:
    res = roll()
    if res == goal:
      print("Win!")
      break
    if res == 7:
      print("Game over.")
      break
    
