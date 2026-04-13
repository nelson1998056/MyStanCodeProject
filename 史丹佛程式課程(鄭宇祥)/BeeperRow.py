"""
File: BeeperRow.py
Name:鄭宇祥
-------------------------
This program guides Karel to place beepers
along Street 1.

The goal of this program is to make Karel
fill the entire street with beepers in a
way that works for different world sizes,
not just one specific world.
"""

from karel.stanfordkarel import *


def main():
    pass
while front_is_clear():
    put_beeper()
    move()
put_beeper()
"""
當Karel前面沒有障礙物時 
會一直往前走直到碰到牆壁
"""

# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
