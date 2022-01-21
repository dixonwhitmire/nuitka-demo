from asgi import app

@app.get("/")
def read_root():
    return {"Hello": "World"}
