# x is a string — this will cause a TypeError if you try to add it to an int
x = "10"

# --- TRY BLOCK ---
# Code inside try runs first
# If ANY error occurs, Python jumps to the matching except block
try:
    # input() always returns a string
    # int() converts it to an integer — if user types letters, raises ValueError
    age = int(input("What is your age?"))

    # Manually raise our own exception if age is 0 or negative
    # raise Exception() lets you create custom error messages
    if age <= 0:
        raise Exception("Your age must be positive")

    # This line is commented out — would cause TypeError
    # because you can't add an int (age) and a string (x)
    # age_plus_10 = age + x

    # This will ALWAYS raise ZeroDivisionError
    # You cannot divide any number by zero
    print(0/0)


# --- EXCEPT BLOCKS ---
# Each except block catches a specific type of error
# Python checks them in order from top to bottom

# Catches: user types letters instead of a number (e.g. "hello")
except ValueError:
    print("Please enter a number")

# Catches: mismatched types (e.g. adding int + string)
# Would be triggered by age_plus_10 = age + x if uncommented
except TypeError:
    print("x is not a number")

# Catches: any attempt to divide by zero
# Triggered by print(0/0)
except ZeroDivisionError:
    print("You can't divide by zero")

# --- FINALLY BLOCK (commented out) ---
# finally ALWAYS runs whether an error occurred or not
# Useful for cleanup like closing files or database connections
# finally:
#   print("Goodbye")