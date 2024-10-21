from random import *
def main():
    balls = 0 # variable to count 6 balls of an over
    while balls < 6:
        ball = randint(0, 9)
        if ball >= 0 and ball <= 6: print(ball, end = ' ');
        elif ball == 7:
            out = randint(0, 3)
        if out == 0: print(end = 'B '); # bold out
        elif out == 1: print(end = 'C '); # catch out
        elif out == 2: print(end = 'S '); # stump out
        else: print(end = 'R '); # Run out
        if ball == 8: print(end = 'W '); balls -= 1 # wide ball will not be counted as a legal ball
        else: print(end = 'N '); balls -= 1 # no ball will not be counted as a legal ball
        balls += 1
main()
