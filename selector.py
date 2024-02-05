from random import randint
from timer import timer
from threading import Thread
from checker import check_prime


def random_select():
    valid_number = False
    random_number = 0
    # This while loop is to ensure that the selected number will be draw again if it isn't prime
    while(not valid_number):
        # It'll draw a number
        random_number = randint(0, 100)
        # Starting number to check if it's prime
        mult = 2
        # This while loop is to check if the selected number is prime
        valid_number = check_prime(mult, random_number)

    # Starts the timer thread and calls the function
    Thread(target=timer, args=(random_number,)).start()

    # return the random_number to be used in interaction function
    return random_number
