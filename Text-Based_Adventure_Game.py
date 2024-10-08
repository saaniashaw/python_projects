def start_game():
    print("Welcome to the Text-Based Adventure Game!")
    print("You find yourself in a dark forest. You can go 'left' or 'right'.")
    first_choice()

def first_choice():
    choice = input("What do you want to do? (left/right): ").lower()
    
    if choice == 'left':
        left_path()
    elif choice == 'right':
        right_path()
    else:
        print("Invalid choice. Please try again.")
        first_choice()

def left_path():
    print("You walk left and come across a river.")
    choice = input("Do you want to 'swim' across or 'build' a bridge? (swim/build): ").lower()
    
    if choice == 'swim':
        print("You swim across the river safely. You find treasure on the other side! You win!")
    elif choice == 'build':
        print("You build a bridge but it collapses. You fall into the river. Game Over.")
    else:
        print("Invalid choice. Please try again.")
        left_path()

def right_path():
    print("You walk right and encounter a fierce wolf!")
    choice = input("Do you want to 'fight' the wolf or 'run' away? (fight/run): ").lower()
    
    if choice == 'fight':
        print("You bravely fight the wolf and win! You find a hidden cave. You win!")
    elif choice == 'run':
        print("You run away but get lost in the forest. Game Over.")
    else:
        print("Invalid choice. Please try again.")
        right_path()

if __name__ == "__main__":
    start_game()
