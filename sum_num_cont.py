# Created by: Zack Isingoma
# Created on: 15th Jan 2022.
# uses a while true loop to find the sum
# of numbers the user inputs.

def main():
    print("Welcome")
    user_range = int(input("How many numbers would you like to add: "))
    count = 0
    num_sum = 0
    number = 1
    while number > 0:
        number_as_string = input('Enter a positive number: ')
        try:
            number_as_int = int(number_as_string)
            if number_as_int > 0:
                num_sum = num_sum + number_as_int
                print("{} was added to the sum".format(number_as_int))
            elif number_as_int <= 0:
                print("Your input is <= 0")
                continue
            if count  == user_range:
                break
            count = count + 1

        except Exception:
            print("Input is not an integer")
    print("The sum of the numbers is {}".format(num_sum))
    print("Thanks for playing")


if __name__ == "__main__":
    main()
