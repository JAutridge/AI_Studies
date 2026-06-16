from time import sleep, time

# --- DECORATOR FUNCTION ---
# A decorator wraps another function to add extra behavior
# This decorator measures how long a function takes to run
def cooking_time(func):
    # 'enhanced_func' is the wrapper that replaces the original function
    # *args and **kwargs allow it to accept any arguments
    def enhanced_func(*args, **kwargs):
        start_time = time()       # Record the time before the function runs
        func(*args, **kwargs)     # Run the original function
        end_time = time()         # Record the time after the function finishes
        print(f'Task time:{end_time - start_time} Seconds')  # Print how long it took
    return enhanced_func          # Return the wrapped version of the function


# --- APPLYING THE DECORATOR ---
# The @cooking_time decorator is applied to each cooking function below
# This means every time burger(), fries(), or drink() is called,
# it will automatically be timed


# Burger function - takes a number and multiplies it by 3 for cook time
@cooking_time
def burger(num):
    print("Burger has started cooking!")
    sleep(num * 3)   # Simulate cooking time (num x 3 seconds)
    print("Burger has finished cooking!")


# Fries function - takes a number and multiplies it by 2 for cook time
@cooking_time
def fries(num):
    print("Fries has started cooking!")
    sleep(num * 2)   # Simulate cooking time (num x 2 seconds)
    print("Fries has finished cooking!")


# Drink function - always takes 1 second to make
@cooking_time
def drink():
    print("Drink is being made!")
    sleep(1)         # Simulate 1 second to make the drink
    print("Drink has been made!")


# --- RUNNING THE FUNCTIONS ---
# Each function runs one at a time and prints how long it took
burger(3)   # Cooks for 9 seconds  (3 x 3)
fries(2)    # Cooks for 4 seconds  (2 x 2)
drink()     # Takes 1 second