from fastapi import FastAPI
import asyncio
import uvicorn

app = FastAPI()

@app.get("/hi")
async def greet():
    await asyncio.sleep(3)
    return "Hello? World?"

if __name__ == "__main__":
    uvicorn.run(app=app, host="127.0.0.1", port=8000)