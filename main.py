from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()


@app.post("/inbound")
async def receive_inbound_call(request: Request):
    # Read JSON or form payload
    try:
        data = await request.json()
    except:
        data = await request.body()  # fallback if not JSON

    headers = dict(request.headers)

    print("=== INCOMING BONVOICE WEBHOOK ===")
    print("Headers:", headers)
    print("Body:", data)

    return {
        "status": "received",
        "headers": headers,
        "body": data.decode() if isinstance(data, bytes) else data,
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5001, reload=True)
