import asyncio

# with async, root is now a coroutine, a function that can pause itself
# calling root now creates a coroutine object, something has to run it
async def root():
    # await only works inside an async function
    # while sleeping/paused other coroutines can run
    await asyncio.sleep(1)
    return {"status": 200}

print(asyncio.run(root()))





# async def fetch(client, label, seconds):
#     await client.get(f"https://httpbin.org/delay/{seconds}")
#     print(f"{label} done")

# async def main():
#     async with httpx.AsyncClient() as client:
#         await asyncio.gather(
#             fetch(client, "A", 3),
#             fetch(client, "B", 1),
#             fetch(client, "C", 2),
#         )

# asyncio.run(main())