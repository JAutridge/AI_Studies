import asyncio

# --- ASYNC FUNCTION (Coroutine) ---
# 'async def' means this is an asynchronous function (coroutine)
# It can be paused and resumed, allowing other tasks to run while waiting
# Parameters:
#   delay = how many seconds to wait (simulates fetching data)
#   data  = the name of the data being recovered
async def get_data(delay, data):
    print(f"Data: {data} has start recovery")  # Prints when data recovery starts
    await asyncio.sleep(delay)                  # PAUSES this task for 'delay' seconds
                                                # While paused, OTHER tasks can run
    print(f"Data: {data} has been recovered")  # Prints when recovery is complete


# --- MAIN ASYNC FUNCTION ---
# This is the entry point for all async tasks
# 'async def' makes it a coroutine that can run tasks concurrently
async def main():
    print("Start if Coroutine.")

    # create_task() schedules each coroutine to run concurrently
    # All 3 tasks START immediately and run at the same time
    # They do NOT wait for each other to finish before starting
    d1 = asyncio.create_task(get_data(10, "Dogs"))   # Task 1 - takes 10 seconds
    d2 = asyncio.create_task(get_data(5, "Birds"))   # Task 2 - takes 5 seconds
    d3 = asyncio.create_task(get_data(10, "Cats"))   # Task 3 - takes 10 seconds

    # await pauses main() until each task is complete
    # But since all 3 tasks are already running concurrently
    # the total wait time is 10 seconds NOT 25 seconds (10+5+10)
    await d1  # Wait for Dogs to finish
    await d2  # Wait for Birds to finish (already done by this point)
    await d3  # Wait for Cats to finish


# --- RUNNING THE ASYNC PROGRAM ---
# asyncio.run() starts the event loop and runs the main() coroutine
# You can only call asyncio.run() once — it manages everything
asyncio.run(main())