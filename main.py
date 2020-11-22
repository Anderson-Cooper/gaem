#imports
from random import randint as r
#Variables
hp=30
ehp=45
choice=""
mc=25
#Definitions
def check():
  print("HP", hp)
  print("ENEMY HP", ehp)
  print("MC", mc)
  print("==================")
  print("S: Slash")
  print("M: Magic")
#Spaghetti
print("Surge Attacks You!")
print("===================")
while True:
  check()
  choice=input("What are you doing>")
  if choice.lower() == "s":
    slsh=r(4,7)
    ehp=ehp-slsh
    print("You did", slsh, "In damage!")
  if choice.lower() == "m":
    if mc==0:
      exit("You opened the spell book and died from dying")
      
    print("MC", mc)
    print("1: MC Power Pow, 10 MC 10 DMG")
    print("2: MC Flask, 5 MC +10 HP")
    print("3: MC Magnet, +5 MC")
    mci=input("Input the spell code>")
    if mci=="1":
      mc=mc-10
      ehp=ehp-10
      print("New MC", mc)
      
    if mci=='2':
      mc=mc-5
      hp=hp+10
      print("New MC", mc)
    if mci=='3':
      mc=mc+3
      print("New MC", mc)
  print("=======================")
  eatt=r(1,8)
  hp=hp-eatt
  print("Surge did", eatt, "in damage!")
  if ehp<0:
    break
  if ehp==0:
    break
  if hp==0:
    exit("You have died!")
  if hp<0:
    exit("You have died!")
print("You have Won!")
