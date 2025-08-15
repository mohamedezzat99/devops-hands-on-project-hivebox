from fastapi import FastAPI
from _version import __version__
app = FastAPI(title="My Awesome API")

@app.get("/version")
async def get_version():
    return {"version": __version__}
