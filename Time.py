from datetime import datetime, timedelta
import time
import pyautogui as pag


def time_active():
    print("The current time is", datetime.now().strftime("%H:%M:%S"))

    current = datetime.now()
    time_gone = int(input("How long in minutes?"))
    time_done = current + timedelta(minutes=time_gone)
    print("This process will end at", time_done.strftime("%H:%M:%S"), '\n')

    while datetime.now() < time_done:
        time_pass = datetime.now() - current
        pag.moveRel(0, 15)
        time.sleep(0.8)
        pag.moveRel(0, -15)
        if time_pass.seconds % 60 == 0:
            mins = time_pass.seconds / 60
            print("You've been gone for {} minutes".format(mins))
            # print('The time is:', datetime.now().strftime("%H:%M:%S"))

    print('This process ended at', datetime.now().strftime("%H:%M:%S"))


if __name__ == "__main__":
    time_active()
