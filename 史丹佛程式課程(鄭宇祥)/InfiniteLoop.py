"""
File: InfiniteLoop.py
Name:鄭宇祥
------------------------
This program demonstrates the idea of an
infinite loop.

Through this example, we will observe how
a while loop can run forever if its stopping
condition is not properly designed. This
program serves as a reminder of one common
bug when using while loops.
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will be turning left non-stop
    """
    while front_is_clear():
        turn_left()
"""
如果當karel前面沒有障礙物時，則左轉。
但由於每次左轉後的前方都沒有障礙物，導致Karel一直無限迴轉，形成無限loop。
"""

# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
