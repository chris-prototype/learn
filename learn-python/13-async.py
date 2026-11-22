import asyncio
import httpx

# with async, root is now a coroutine, a function that can pause itself
# after calling root() a coroutine object is returned from root()
async def root():
    # await only works inside an async function
    # while sleeping/paused other coroutines can run
    await asyncio.sleep(2)
    return {"status": 200}

print('waiting ...')

# program will wait for result here
# the coroutine object requires a runner; in this case asyncio.run() to run it
# it is now inside of an event loop
result = asyncio.run(root())
print(result)


async def fetch(client, label, seconds):
    await client.get(f"https://httpbin.org/delay/{seconds}")
    print(f"{label} done")

async def main():
    async with httpx.AsyncClient() as client:
        await asyncio.gather(
            fetch(client, "A", 3),
            fetch(client, "B", 1),
            fetch(client, "C", 2),
        )

print('waiting ...')

# program will wait for result here
asyncio.run(main())
