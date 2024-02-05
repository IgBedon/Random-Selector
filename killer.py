from os import kill
from os import getpid
import signal


def kill_process():
    # Get the process PID
    pid = getpid()
    # Kill the process PID
    kill(pid, signal.SIGTERM)
