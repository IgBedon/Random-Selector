from checker import check_ready


def introduct_rules():
    # Present the rules
    print("===============================")
    print("!Random Number Game! Guess the number drew!")
    print("The program will draw a number (0-100) and your goal is to match the drawn number")
    print("You have 100 life points and 3 attempts to match the number...")
    print("And obviusly... 10 SECONDS.")
    print("===============================\n")

    continue_choice = False
    while (not continue_choice):
        # Get the user answer
        answer = input("Are you ready? [Yes or No]\n")
        # Check the user answer
        continue_choice = check_ready(answer)
