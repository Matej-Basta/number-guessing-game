import random
import math
from errors import InvalidRangeError, OutOfRangeError

def get_valid_input(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            if 'lower_limit' in globals() and 'upper_limit' not in globals() and lower_limit >= user_input:
                raise InvalidRangeError
            if 'lower_limit' in globals() and 'upper_limit' in globals() and (user_input < lower_limit or user_input > upper_limit):
                raise OutOfRangeError  
            return user_input
        except InvalidRangeError:
            print("Upper limit must be higher than the lower limit.")
        except OutOfRangeError:
            print("Your selected number is outside of the defined range.")
        except:
            print("Please, insert an integer.")

print("Please select a range.")
lower_limit = get_valid_input("Lower limit: ")
upper_limit = get_valid_input("Upper limit: ")

result = random.randint(lower_limit, upper_limit)
number_of_guesses = 0
maximum_number_of_guesses = math.log2(upper_limit - lower_limit + 1)
found = False

while not found and number_of_guesses < maximum_number_of_guesses:
    number_of_guesses += 1
    selected_number = get_valid_input("Guess a number: ") 
    if selected_number == result:
        found = True
    elif selected_number < result:
        print("Try again! You guessed too small.")
    else:
        print("Try again! You guessed too high.")

if found:
    print(f'''You've found the number.
        
You needed {number_of_guesses} guess{"es" if number_of_guesses > 1 else ""}.''')
else:
    print(f'''Unfortunately, you haven't found the number
          
It was {result}.''')