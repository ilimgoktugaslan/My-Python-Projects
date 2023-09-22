import unittest
from unittest.mock import patch
import io
import random
import math
import sys

def guess_number():
    # Taking Inputs
    lower = int(input("Enter Lower bound:- "))
 
    # Taking Inputs
    upper = int(input("Enter Upper bound:- "))
 
    # generating random number between the lower and upper
    x = random.randint(lower, upper)
    print("\n\tYou've only ",
          round(math.log(upper - lower + 1, 2)),
          " chances to guess the integer!\n")
 
    # Initializing the number of guesses.
    count = 0
 
    # for calculation of minimum number of guesses depends upon range
    while count < math.log(upper - lower + 1, 2):
        count += 1
 
        # taking guessing number as input
        guess = int(input("Guess a number:- "))
 
        # Condition testing
        if x == guess:
            print("Congratulations you did it in ",
                  count, " try")
            # Once guessed, loop will break
            break
        elif x > guess:
            print("You guessed too small!")
        elif x < guess:
            print("You Guessed too high!")
 
    # If Guessing is more than required guesses, shows this output.
    if count >= math.log(upper - lower + 1, 2):
        print("\nThe number is %d" % x)
        print("\tBetter Luck Next time!")
 
class GuessNumberTests(unittest.TestCase):

    @patch('builtins.input', side_effect=['10', '50', '30', '40'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_guess_number_successful(self, mock_output, mock_input):
        guess_number()
        expected_output = "Congratulations you did it in  2  try"
        self.assertEqual(mock_output.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['10', '50', '50', '50', '50'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_guess_number_unsuccessful(self, mock_output, mock_input):
        guess_number()
        expected_output = "\nThe number is 30\tBetter Luck Next time!\n"
        self.assertEqual(mock_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()