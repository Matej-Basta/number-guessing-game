from errors import InvalidRangeError

def get_valid_input(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            if 'lower_limit' in globals() and lower_limit >= user_input:
                raise InvalidRangeError
            return user_input
        except InvalidRangeError:
            print("Upper limit must be higher than the lower limit.")
        except:
            print("Please, insert an integer.")

print("Please select a range.")
lower_limit = get_valid_input("Lower limit: ")
upper_limit = get_valid_input("Upper limit: ")