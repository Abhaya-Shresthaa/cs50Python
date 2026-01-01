import time

def countdown(seconds):
    while seconds > 0:
        print(f"\rTime left: {seconds} seconds", end="")
        time.sleep(1)
        seconds -= 1
    print("\rTime's up!            ")

countdown(10)