x = "10"
try:
    age = int(input("What is your age?"))
    if age <= 0:
        raise Exception("Your age must be positive")
#    age_plus_10 = age + x
    print(0/0)
except ValueError:
    print("Please enter a number")
except TypeError:
    print("x is not a number")
except ZeroDivisionError:
    print("You can't divide by zero")
# finally:
#   print("Goodbye")


