import random
from time import sleep
from os import system, name

# Dictionaries
Robot={'attack':40, 'defend':50, 'dodge':30}
Martian={'attack':30, 'defend':40, 'dodge':50}
Velociraptor={'attack':50, 'defend':40, 'dodge':30}
Warewolf={'attack':25, 'defend':35, 'dodge':45}

# Lists
characters=['Robot', 'Martian', 'Velociraptor', 'Warewolf']
possibleActions=['attack','defend','dodge']
# Game functions
# Character Select
def charSelect(val):
  if (val == 'R' or val == '1'):
    selected=characters[0]
    #print("Robot")
  elif (val == 'M' or val =='2'):
    selected=characters[1]
    #print("Martian")
  elif (val == 'V' or val =='3'):
    selected=characters[2]
    #print("Velociraptor")
  else:
    selected=characters[3]
    #print("Warewolf")
  return selected
# Move Select
def moveSelect(val):
  if (val == 'A' or val == '1'):
    selAction=possibleActions[0]
    print("You selected attack")
  elif (val == 'B' or val =='2'):
    selAction=possibleActions[1]
    print("You selected block")
  elif (val == 'D' or val =='3'):
    selAction=possibleActions[2]
    print("You selected dodge")
  return selAction
# Clear window
def clear(): # clear window
  if name == 'nt':
    _ = system('cls') # clear cmd
  else:
    _ = system('clear') # clear *nix

# Player select (user)

promptUser = input('''Select a character: 
                      1) Robot 
                      2) Martian 
                      3) Velociraptor
                      > ''')
#print(promptUser[0].upper())
player=charSelect(promptUser[0].upper())
clear()
print(f"You have chosen: {player}")

# Opponent select (random)
#opponent = charSelect(str(random.randrange(1,3,1)))
opponent = random.choice(characters[0:3])
print(f"Your opponent is: {opponent}")

# Initialize game setup

print(f'''
  Beginning battle....
  {player}:500HP vs {opponent}:500HP
''')

sleep(5)
clear()

userHealth = 500
opponentHealth = 500

# Begin game loop

while (userHealth>0 and opponentHealth>0):
  useraction=input(f'''
                   Select your move: 
                   1) Attack 
                   2) Block 
                   3) Dodge: 
                   > ''')
  useraction=moveSelect(useraction[0].upper())
  oppaction=random.choice(possibleActions)
  print(f"Your opponent, {opponent} selected {oppaction}")
  
  if useraction == oppaction:
    print(f"Both players selected {useraction}.")
    if useraction == possibleActions[0]:
      userHealth=userHealth-100
      opponentHealth=opponentHealth-100
    else:
      print("The player moves nullify...")

  elif useraction == possibleActions[0]: # player attack
    if oppaction == possibleActions[1]: # player attack - opp block
      print(f"{opponent} blocked your attack.  You inflicted minimal damage.")
      opponentHealth=opponentHealth-30
    else: # player attack - opp dodge
      print(f"{opponent} dodged your attack, and struck back.")
      userHealth=userHealth-100

  elif useraction == possibleActions[1]: # player block
    if oppaction == possibleActions[0]: # player block - opp attack
      print(f"You blocked {opponent}'s attack.  {opponent} inflicted minimal damage.")
      userHealth=userHealth-30
    else: # player block - opp dodge
      print(f"{opponent} tried to illude you, but you tracked their move.  You were able to attack.")
      opponentHealth=opponentHealth-100

  elif useraction == possibleActions[2]: #dodge
    if oppaction == possibleActions[1]: # player dodge - opp block
      print(f"You tried to illude {opponent}, but {opponent} tracked your move.  They were able to attack you.")
      userHealth=userHealth-100
    else: # player dodge - opp attack
      print(f"You dodged {opponent}'s attack, and struck back.")
      opponentHealth=opponentHealth-100
  print(f'''Current Score:
        {player}:{userHealth}
        {opponent}:{opponentHealth}''')

sleep(1)
clear()

print(f"{player}:{userHealth} {opponent}{opponentHealth}")
if userHealth > opponentHealth:
  print(f"You have defeated {opponent}")
else:
  print(f"{opponent} wins....")

  