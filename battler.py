# Initial parameters

#characters = ['warewolf', 'robot', 'martian', 'velociraptor']
userHealth = 100
opponentHealth = 100

# Player select
promptUser = input("Select a character: 1) Robot 2) Martian 3) Velociraptor: ")

#place the conditional into a function 
if promptUser.lower() == 'robot' or promptUser[0].lower() == 'r' or promptUser == '1':
    user='robot'
    attack=45
    defense=60
    illusive=50
    print("Robot")
elif promptUser.lower() == 'martian' or promptUser[0].lower() == 'm' or promptUser == '2':
    user='Martian'
    attack=45
    defense=60
    illusive=50
    print("Martian")
elif promptUser.lower() == 'velociraptor' or promptUser[0].lower() == 'v' or promptUser == '3':
    user='Velociraptor'
    attack=45
    defense=60
    illusive=50
    print("Velociraptor")
else:
    user='Warewolf'
    attack=45
    defense=60
    illusive=50
    print("Warewolf")