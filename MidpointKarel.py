from karel.stanfordkarel import *

"""
File: MidpointKarel.py
Name: 
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
    """
    I have tried several methods for almost 4+ hours, but this is the only one work, Q_Q

    For this method, it divided into two parts.
    The first is when there is only one avenue.
    The second is when there is more than one avenue.

    """

    if front_is_clear():  # if front is clear, there's more than one avenue.
        move()
        while front_is_clear():  # Let Karel fill all the street with beeper, except the first and the end.
            put_beeper()
            move()
        turn_around()  # Let Karel move to the first side beeper
        move()
        while on_beeper():  # Start to pick up the beeper.
            start_pick()
            move()
        turn_around()  # When come to this line, beeper must be at the middle of street!
        move()
        put_beeper()  # Put the last beeper at the middle, task done!
    else:  # There's only one avenue, just put a beeper.
        put_beeper()


def start_pick():  # Go to the side and pick the beeper.
    """
    pre-condition: Karel is on beeper, and its on the side.
    post-condition: Karel pick up the side beeper and ready to move on.
    """
    while on_beeper():
        move()
    turn_around()
    move()
    pick_beeper()


def turn_right():  # Karel finally learned how to turn right!
    for i in range(3):
        turn_left()


def turn_around():  # Karel finally learned how to turn around!
    for i in range(2):
        turn_left()

####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)