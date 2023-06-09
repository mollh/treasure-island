print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
left_or_right = input("Will you go left towards the river or right towards the forest? Left or right.\n").lower()
if left_or_right == "right":
  print("You're eaten alive by a herd of zombie bunnies. GAME OVER")
elif left_or_right == "left":
  swim_or_wait = input("You're at the river. You notice a panther is stalking you. You have to cross the river, but crocodiles are slowly swimming by. Do you swim now or wait? Swim or wait.\n").lower()
  if swim_or_wait == "swim":
    print("You make it past the crocodiles to the other side of the river, but a family of kangaroos attack and drown you in the shallow end of the river. GAME OVER")
  elif swim_or_wait == "wait":
    which_door = input("You wait for the crocodiles to pass and prepare to fight the panther with your bare hands. As the panther approaches, you realize it is a winged unicorn. You mount the unicorn and it flies you across the river. You dismount the unicorn and walk up a windy staircase leading to a large stone wall with three doors side by side ; a blue door, a red door, and a yellow door. Which color door do you choose to open? Blue, red, or yellow.\n").lower()
    if which_door == "blue":
      print("You are sucked into a blackhole. GAME OVER")
    elif which_door == "red":
      print("You fall into hell and are tortured forever. GAME OVER")
    elif which_door == "yellow":
      print("Congratulations! You found the treasure and live happily ever after!")
    else:
      print("GAME OVER. You will fail at real life because you can't accurately type colors.")