import time

# Dictionaries
Robot={"attack":45, "defense":60, "illusive":50}
Martian={"attack":50, "defense":40, "illusive":60}
Velociraptor={"attack":45, "defense":60, "illusive":50}
Warewolf={"attack":45, "defense":60, "illusive":50}

# Lists
characters=['Robot', 'Martian', 'Velociraptor', 'Warewolf']

# Game functions

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
  


# Player select

promptUser = input("Select a character: 1) Robot 2) Martian 3) Velociraptor: ")
#print(promptUser[0].upper())
player=charSelect(promptUser[0].upper())
print(f"You have chosen: {player}")


# Game setup

userHealth = 100
opponentHealth = 100

# Begin game loop

#while (userHealth>0 and opponentHealth>0):