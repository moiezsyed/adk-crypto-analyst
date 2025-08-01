from fastapi import FastAPI

app= FastAPI()

@app.get("/")
async def root():
    return {"status": "Ok", "message": "Crypto ADK service is up and running!"}