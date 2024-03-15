import os

# Function to clear the console screen
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

# Global variables
consoles = 0  # Number of consoles the player has
speed = 1     # Speed of console production

# Main menu function
def start_menu():
    print("Console Clicker")
    print("[S] Start")
    print("[H] Help")
    cmd = input(">> ").lower()
    # Using match-case statement for Python 3.10+ (if available)
    match cmd:
        case "h":
            clear()
            help_menu()
        case "s":
            clear()
            start_game()

# Help menu function
def help_menu():
    clear()
    print("Welcome to Console Clicker!")
    print("In this game, your goal is to collect as many consoles as possible.")
    print("You can earn consoles by pressing Enter or Return on your keyboard.")
    print("Keep earning consoles to get new upgrades, which let you get even more consoles.")
    input("Press enter to go back.")
    clear()
    start_menu()

# Shop menu function
def shop_menu():
    global consoles
    global speed
    clear()
    print("Welcome to the shop!")
    print("You can buy upgrades for consoles here for more console production.")
    print("[1] Speed +1, Cost: 50 consoles")
    print("[2] Speed +2, Cost: 100 consoles")
    print("[3] Speed x2, Cost: 800 consoles")
    print("[G] Go back")
    cmd = input(">> ").lower()
    if cmd == "1" and consoles >= 50:
        consoles -= 50
        speed += 1
    elif cmd == "2" and consoles >= 100:
        consoles -= 100
        speed += 2
    elif cmd == "3" and consoles >= 800:
        consoles -= 800
        speed *= 2
    elif cmd == "g":
        clear()
        start_game()

# Game loop function
def start_game():
    global consoles
    global speed
    while True:
        print("Consoles:", consoles)
        print("[S] Shop")
        action = input(">> ").lower()
        if action == "s":
            shop_menu()
        consoles += speed
        clear()

# Starting the game
start_menu()
