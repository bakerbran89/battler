import time

# Character stats
Robot={"attack":45, "defense":60, "illusive":50}
Martian={"attack":50, "defense":40, "illusive":60}
Velociraptor={"attack":45, "defense":60, "illusive":50}
Warewolf={"attack":45, "defense":60, "illusive":50}
# Characters
characters=['Robot', 'Martian', 'Velociraptor', 'Warewolf']

# Game functions
'''def charSelect(val):
  if val.isdigit():
    print('digit')
  elif val == 'R' or 'r':
    print('R')
  elif val == 'M' or 'm':
    print('M')
  elif val == 'V' or 'v':
    print('V')
  else:
    print('W')

  selected = characters[val]
  print(selected)
  return selected
  '''


# Player select
promptUser = input("Select a character: 1) Robot 2) Martian 3) Velociraptor: ")
charSelect(promptUser)

# Game setup
userHealth = 100
opponentHealth = 100
# Begin game loop
#while (userHealth>0 and opponentHealth>0):