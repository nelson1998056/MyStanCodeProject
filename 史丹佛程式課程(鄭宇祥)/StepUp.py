"""
File: StepUp.py
Name: 鄭宇祥:
------------------------
This program demonstrates how Karel picks up a beeper
at Street 1 Avenue 2 and moves it to Street 2 Avenue 4.

By guiding Karel step by step, we will practice writing
clear and well-structured commands. At the end of the
program, Karel will be facing East at Street 2 Avenue 5.
"""

from karel.stanfordkarel import *

def turn_left3():
    turn_left()
    turn_left()
    turn_left()
def main():
    move()
    pick_beeper()
    move()
    turn_left()
    move()
    turn_left3()
    move()
    put_99()
def put_99():
    for i in range(99):
        put_beeper()
    move()
"""
為了省去每次都要寫put_beeper的時間，所以加入for迴圈讓Karel放置特定數量的beeper。
"""





# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
