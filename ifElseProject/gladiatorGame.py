import random

player_health = 100
opponent_health = 100
opponent_big_attack_counter = 0

print("Welcome to Gladiator Battle!")
print("You are facing off against your opponent.")

# While loop. Keeps game going while conditions are met
while player_health > 0 and opponent_health > 0:
    print("\nPlayer Health:", player_health)
    print("Opponent Health:", opponent_health)
    
    # Actions on Player's turn
    print("\nChoose your action:")
    print("1. Slash (Reliable attack with less damage)")
    print("2. Stab (Less reliable attack with more damage)")
    print("3. Block (Reduces half of incoming damage)")
    print("4. Surrender (End the current game)")
    
    while True:
        try:
            action_choice = int(input("Enter your action choice (1-4): "))
            if action_choice not in [1, 2, 3, 4]:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a valid action choice.") # Catch for invalid key-input

    if action_choice == 1:  # Slash calculations
        player_damage = random.randint(10, 20)
        opponent_health -= player_damage
        print("You slashed the opponent and dealt", player_damage, "damage!")
    elif action_choice == 2: # Stab calculations
        stab_chance = random.randint(1, 10) # Gives stab action a chance to miss
        if stab_chance <= 7:  # 70% miss chance
            player_damage = random.randint(20, 30)
            opponent_health -= player_damage
            print("You stabbed the opponent and dealt", player_damage, "damage!")
        else:
            print("Your stab missed!")
    elif action_choice == 3: # Block calculations/ Needs more testing though does work against the big attack
        print("You chose to block and prepare for the opponent's attack.")
    elif action_choice == 4: # Surrender calculation
        confirm_surrender = input("Are you sure you want to surrender? (Y/N): ")
        if confirm_surrender.upper() == "Y":
            print("\nYou surrender. The opponent mocks your weakness.")
            break
        else:
            print("You continue the battle.")

    if opponent_health <= 0:
        break

    # Opponent's turn
    # Calculations for Big attacks ensuring it happens every third computer attack
    opponent_big_attack = False
    
    if opponent_big_attack_counter % 2 == 1:
        opponent_big_attack = True
        print("\nThe opponent is preparing for a big attack on the next swing!")

    # Calculations for the computer's attack on the player
    opponent_attack_choice = random.randint(1, 2)

    if opponent_attack_choice == 1:
        opponent_damage = random.randint(10, 20)
        if opponent_big_attack:
            opponent_damage *= 2  # Double the damage for the big attack
        if action_choice == 3:  # If the player chose to block
            opponent_damage //= 2  # Reduce incoming damage by half
        player_health -= opponent_damage
        print("The opponent slashed you and dealt", opponent_damage, "damage!")
    elif opponent_attack_choice == 2:
        opponent_damage = random.randint(20, 30)
        if opponent_big_attack:
            opponent_damage *= 2  # Double the damage for the big attack
        if action_choice == 3:  # If the player chose to block
            opponent_damage //= 2  # Reduce incoming damage by half
        player_health -= opponent_damage
        print("The opponent stabbed you and dealt", opponent_damage, "damage!")

    opponent_big_attack_counter += 1

# Tests the games conditions to determine the winner
if player_health > 0:
    print("\nCongratulations! You defeated your opponent!")
else:
    print("\nGame over. You were defeated by your opponent!")

# Prompt to replay game or return to quit
play_again = input("Do you want to play again? (yes/no): ")
if play_again.lower() == "yes":
    game()
else:
    print("Thanks for playing! Goodbye!")
