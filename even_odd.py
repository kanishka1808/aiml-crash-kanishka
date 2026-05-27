# even_odd.py ---This file checks whether a number is even, odd, or zero


while True:

    try:

        number = int(input("Enter a number: "))

        if number == 0:
            print("The number is zero")

        elif number % 2 == 0:
            print("The number is even")

        else:
            print("The number is odd")

        break

    # int("abc") gives ValueError because abc is not a valid integer

    except ValueError:
        print("Please enter a valid number")