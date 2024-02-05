from killer import kill_process
from checker import check_number


def user_interaction(random_number):
    life = 100
    attempts = 0
    valid_choice = False

    # This while checks if we continue playing
    while(life>0 and attempts<3):
        while(not valid_choice):
            user_choice = int(input("Write the drew number!\n"))
            valid_choice = check_number(user_choice)

        # Returning value False to valid_choice
        valid_choice = False
        # Check if the user typed the correct number
        if(user_choice == random_number):
            print("Correct! You win!")
            kill_process()
        else:
            print("You're wrong!")
            attempts += 1
            # Set life points to be taken away
            lost_life_points = (random_number - user_choice)

            # Check the order to realize the math operation
            if(lost_life_points>=0):
                life = life-lost_life_points
            else:
                life = life+lost_life_points

            # Check if attempts have been achieved
            if (attempts == 3):
                print("Your attempts ended! You lost!")
                print(f"The chosen number was: {random_number}")
                kill_process()

                # Check if you have some life
            if(life<=0):
                print(f"Your actual life points are: 0. You lost!")
                print(f"The chosen number was: {random_number}")
                kill_process()
            else:
                print(f"Your actual life points are: {life}")
                print("=============================================")
                