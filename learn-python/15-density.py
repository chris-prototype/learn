import httpx
from fastapi import FastAPI
import uvicorn

# app object follows the ASGI standard and can be passed to uvicorn
app = FastAPI()

# registers root as the handler for GET requests to "/"
@app.get("/")
# with async, root is now a coroutine, a function that can pause itself
# calling root now creates a coroutine object, something has to run it
async def root():

    # this version requires async but a sync version is available as well
    # the name client is user defined and is what is handed back
    async with httpx.AsyncClient() as client:

        # await only works inside an async function
        # while waiting other coroutines can run
        r = await client.get("https://httpbin.org/delay/1")
    return {"status": r.status_code}

if __name__ == "__main__":
  uvicorn.run(app)

# uvicorn runs on port 8000 by default
# test using - curl http://127.0.0.1:8000/