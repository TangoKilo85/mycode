import random

GREEN = "\033[32m"  # sets text to green
RED = "\033[31m"    # sets text to red
BLUE = "\033[34m"   # sets text to blue
RESET = "\033[0m"   # resets text color

def calculate_player_damage():  # Damage calculations for attacks
    return random.randint(15, 20)

def calculate_opponent_damage():
    return random.randint(5, 40)

def calculate_opponent_big_attack_damage():
    return 40

def get_action_name(action_choice):
    if action_choice == '1':
        return "slashed"
    elif action_choice == '2':
        return "stabbed"
    elif action_choice == '3':
        return "blocked"
    else:
        return "chosen an invalid action"

# Game set-up
def game():
    player_health = 100 
    opponent_health = 100
    turn = 1
    prompt_turn = 2
    big_attack_turn = prompt_turn + 1

    print(GREEN + "Welcome to the Colosseum Gladiator! Arm yourself and prepare for battle!" + RESET)
    print(GREEN + "Your opponent is hungry for blood. I'd be on my guard if I were you." + RESET)
    print(GREEN + "He has a wild swing, but your shield seems sturdy. Just remember to use it." + RESET)
    print(GREEN + "Enough with talk, now get ready to fight for the glory of Rome!" + RESET)
    print()
    print("Player Health:", player_health)
    print("Opponent Health:", opponent_health)
    print()

    #Game loop to keep going while condtions are met
    while player_health > 0 and opponent_health > 0:
        print("Turn", turn)
        
        # Player's turn and damage calculations according to input
        action_choice = input(BLUE + "Choose your action:\n"
                              "1. Slash (Reliable attack with modest range damage)\n"
                              "2. Stab (Strong attack with chance to deal lesser damage)\n"
                              "3. Block (Reduces all incoming damage)\n"
                              "4. Surrender (End the current game)\n"
                              "Enter your action choice (1-4): " + RESET)

        player_damage = calculate_player_damage()

        if action_choice == '1':
            opponent_damage = calculate_opponent_damage()
        elif action_choice == '2':
            opponent_damage = calculate_opponent_damage()
        elif action_choice == '3':
            player_damage = 0
            opponent_damage = 0
        else:
            opponent_damage = 0

        print()

        if turn == prompt_turn:
            print(RED + "Your opponent begins to swing wildly! Raise your shield!" + RESET)
            print()
        
        if turn > prompt_turn and (turn - prompt_turn) % 2 == 0: # This is to ensure the opponent makes a big attack when the conditions are met. This is currently not working as intended.
            opponent_damage = calculate_opponent_big_attack_damage()

        if action_choice == '4':
            print("Are you not entertained!!!")
            break

        player_health -= opponent_damage
        opponent_health -= player_damage

        print("You", get_action_name(action_choice), "the opponent and dealt", player_damage, "damage!")
        print("The opponent", get_action_name(action_choice), "you and dealt", opponent_damage, "damage!")
        print()
        print("Player Health:", player_health)
        print("Opponent Health:", opponent_health)
        print()
        # Ends game if either of the following conditions are true
        if player_health <= 0:
            print(GREEN + "You have been defeated. Your corpse a feast for the crows!" + RESET)
            break
        elif opponent_health <= 0:
            print(GREEN + "Congratulations! The glory of the Colosseum is yours!" + RESET)
            break

        # Prompt turn counter
        if turn == prompt_turn:
            prompt_turn += 2  # Increment the prompt turn by 2 to occur every other turn

        turn += 1

# Start the game
game()

