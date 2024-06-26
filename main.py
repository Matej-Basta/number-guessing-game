def get_valid_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except:
            print("Please, insert an integer.")

print("Please select a range.")
lower_limit = get_valid_input("Lower limit: ")
upper_limit = get_valid_input("Upper limit: ")
