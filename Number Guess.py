# this is a Number Guess Game
from random import randint
from time import sleep

for again in range(100):
    def get_user_guess():
        guess = int((raw_input("What's your guess: ")))
        return guess

    def roll_dice(number_of_sides):
        first_roll = randint(1, number_of_sides)
        second_roll = randint(1, number_of_sides)
        max_val = number_of_sides * 2
        print "Maximum value: %d" % max_val
        guess = get_user_guess()
        if guess > max_val:
            print "You have typed an inappropriate answer!"
        else:
            print "Rolling....."
            sleep(2)
            print "The first roll is: %d" % first_roll
            sleep(1)
            print "The second roll is: %d" % second_roll
            sleep(1)
            total_roll = first_roll + second_roll
            print "The total value is: %d" % total_roll
            print "Result...."
            sleep(1)
            if total_roll == guess:
                print "Congrats! You Win!"
            else:
                print "OOPS! You Lost!"
            print
    random = randint(3, 10)
    roll_dice(random)






