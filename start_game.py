from selector import random_select
from interaction import user_interaction
from introduct import introduct_rules
def start_game():
    # Introduction
    introduct_rules()
    # This line calls the random number selector and inside of this function, after the draw, a thread will be started
    random_number = random_select()
    # This line call the interaction function passing random_number as a parameter
    user_interaction(random_number)


if __name__ == "__main__":
    start_game()
