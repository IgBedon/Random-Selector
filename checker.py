from time import sleep


def check_ready(answer):
    if (answer.upper() == "YES" or answer.upper() == "Y"):
        print("Nice! Let's go!")
        return True
    elif (answer.upper() == "NO" or answer.upper() == "N"):
        print("Well, I can wait you all day... :D. Restarting...")
        sleep(5)
    else:
        print("Invalid choice!")


def check_number(user_choice):
    if(0<=user_choice<=100):
        return True
    else:
        print("Invalid value!")
        return False


def check_prime(mult, random_number):
    while (mult < random_number - 1):
        if (random_number % mult == 0):
            return False
        mult += 1
    if (mult == random_number - 1):
        return True
