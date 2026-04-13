"""
File: Steeplechase.py
Name: 鄭宇祥:
---------------------------------
鄭宇祥:
"""

from karel.stanfordkarel import *

def main():
 """
 Karel crosses hurdles in a 12x12 world
 with a for loop
 """
 for i in range(11):
     if front_is_clear():
         move()
     else:
         jump()
         """讓Karel執行固定次數以剛好完成"""
"""
一開始Karel面對東邊
"""
def jump():
    up()
    down()
"""
將跳的動作拆解成上跟下，比較好理解程式如何撰寫
"""
def down():
    while front_is_clear():
          move()
    turn_left()
def up():
    turn_left()
    while not right_is_clear():
        move()
    turn_right()
    move()
    turn_right()


def turn_right():
    for i in range(3):
        turn_left()
# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
