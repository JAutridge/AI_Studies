import asyncio

async def get_data(delay, data):
    print(f"Data: {data} has start recovery")
    await asyncio.sleep(delay)
    print(f"Data: {data} has been recovered")

async def main():
    print("Start if Coroutine.")
    d1 = asyncio.create_task(get_data(10, "Dogs"))
    d2 = asyncio.create_task(get_data(5, "Birds"))
    d3 = asyncio.create_task(get_data(10, "Cats"))

    await d1
    await d2
    await d3
asyncio.run(main())