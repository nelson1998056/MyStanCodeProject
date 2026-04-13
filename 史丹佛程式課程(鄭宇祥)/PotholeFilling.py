"""
File: PotholeFilling.py
Name: 鄭宇祥:
--------------------------
This program demonstrates how Karel fills multiple potholes
by using decomposition.

In this program, we will guide Karel to fix three potholes
on the road. Instead of writing all the commands in one place,
we will practice breaking a big task into smaller, reusable
functions to make the program clearer and easier to manage.
"""

from karel.stanfordkarel import *
def go_in():
    move()
    turn_right()
    move()
    put_99
def go_out():
    turn_left()
    turn_left()
    move()
    turn_right()
    move()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def put_99():
    for i in range(99):
        put_beeper()
def main():
    for i in range(3):
        go_in()
        put_99()
        go_out()
"""
定義三件事 1.進去時候的指令 2.出去時的指令 3.左轉的指令    
以上將動作各自拆解，在最後在一一組裝合併成完整的程式碼。
"""







# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
