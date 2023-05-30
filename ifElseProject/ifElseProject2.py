import random

def calculate_player_damage():
    return random.randint(10, 20)

def calculate_opponent_damage():
    return random.randint(15, 25)

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

def game():
    player_health = 100
    opponent_health = 100
    turn = 1
    prompt_turn = 2

    print("Welcome to the Colosseum Gladiator! Arm yourself and prepare for battle!")
    print("Your opponent is hungry for blood. I'd be on my guard if I were you.")
    print("He has a wild swing, but your shield seems sturdy. Just remember to use it.")
    print("Enough with talk, now get ready to fight for the glory of Rome!")
    print()
    print("Player Health:", player_health)
    print("Opponent Health:", opponent_health)
    print()

    while player_health > 0 and opponent_health > 0:
        print("Turn", turn)

        action_choice = input("Choose your action:\n"
                              "1. Slash (Reliable attack with less damage)\n"
                              "2. Stab (Less reliable attack with more damage)\n"
                              "3. Block (Reduces all incoming damage)\n"
                              "4. Surrender (End the current game)\n"
                              "Enter your action choice (1-4): ")

        player_damage = calculate_player_damage()

        if action_choice == '1':
            opponent_damage = calculate_opponent_damage()
        elif action_choice == '2':
            if turn == prompt_turn:
                opponent_damage = 0
                print("Your opponent begins to swing wildly! Raise your shield!")
                print()
            else:
                opponent_damage = calculate_opponent_damage()
        elif action_choice == '3':
            opponent_damage = 0
        else:
            opponent_damage = 0

        print()

        if action_choice == '4':
            print("You have chosen to surrender. Game over.")
            break

        player_health -= opponent_damage
        opponent_health -= player_damage

        print("You", get_action_name(action_choice), "the opponent and dealt", player_damage, "damage!")
        print("The opponent", get_action_name(action_choice), "you and dealt", opponent_damage, "damage!")
        print()
        print("Player Health:", player_health)
        print("Opponent Health:", opponent_health)
        print()

        if player_health <= 0:
            print("You have been defeated. The opponent wins!")
            break
        elif opponent_health <= 0:
            print("Congratulations! You have defeated the opponent!")
            break

        if turn == prompt_turn:
            prompt_turn += 2  # Increment the prompt turn by 2 to occur every other turn

        turn += 1

# Start the game
game()
