from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()


@app.post("/inbound-call")
async def inbound_call(request: Request):
    body = await request.body()
    print("🔔 Received Bonvoice Webhook:")
    print(body.decode("utf-8"))  # Print raw body to console

    return {"status": "ok"}
