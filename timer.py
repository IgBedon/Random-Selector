from time import sleep
from killer import kill_process


def timer(random_number):
    # Count the time to end the program
    sleep(10)
    print("\nThe time is over! Finishing...")
    print(f"The chosen number was: {random_number}")
    # Call kill function
    kill_process()


