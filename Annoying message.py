import pyautogui
from time import sleep


def repeat_process():
    repeat = input("Do you want to repeat the process? (yes/no): ").lower()
    return repeat == "yes"

repeat = True

while repeat:
    print("Welcome to my tool for sending spam messages.")
    msg = input("Enter the message: ")
    num_msg = int(input("Enter the number of messages: "))
    time_msg = float(input("Enter the time for sending the message: "))

    for num in range(num_msg):
        pyautogui.typewrite(msg)
        sleep(time_msg)
        pyautogui.press("enter")
        sleep(time_msg)
    

    repeat = repeat_process()
    print("Thank you for using my tool.")
    print("created by: Ahmed Ghallab")
