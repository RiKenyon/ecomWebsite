import random

# Function to simulate combat between the player and enemy
def combat(player_skill, enemy_skill):
    player_roll = random.randint(1, 6) + player_skill
    enemy_roll = random.randint(1, 6) + enemy_skill

    if player_roll > enemy_roll:
        return True  # Player wins the combat
    else:
        return False  # Player loses the combat

# Function to handle an encounter
def encounter():
    # Randomly determine the enemy's skill level
    enemy_skill = random.randint(6, 12)

    print("You have encountered an enemy with a skill level of", enemy_skill)

    # Prompt the player for an action
    choice = input("Do you want to [A]ttack or [R]un? ")

    if choice.upper() == "A":
        # Simulate combat
        if combat(player_skill, enemy_skill):
            print("You defeated the enemy!")
        else:
            print("You were defeated by the enemy.")
            # Game over condition
            quit()
    elif choice.upper() == "R":
        # Attempt to escape
        escape_roll = random.randint(1, 6)
        if escape_roll > 3:
            print("You successfully escaped.")
        else:
            print("You failed to escape.")
            # Simulate combat
            if combat(player_skill, enemy_skill):
                print("You defeated the enemy!")
            else:
                print("You were defeated by the enemy.")
                # Game over condition
                quit()

# Game setup
player_skill = 10

print("Welcome to the Fighting Fantasy game!")
print("Your skill level is", player_skill)

# Game loop
while True:
    # Generate a random encounter
    encounter()

    # Prompt the player to continue or quit
    choice = input("Do you want to [C]ontinue or [Q]uit? ")
    if choice.upper() == "Q":
        break

print("Thank you for playing!")