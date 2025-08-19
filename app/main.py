import app.config_logger
import logging
from app.hivebox_api import get_avg_senseBox_temp
from fastapi import FastAPI
from app._version import __version__

logger = logging.getLogger(__name__)

app = FastAPI(title="My Awesome API")


@app.get("/version")
async def get_version():
    return {"version": __version__}


@app.get("/temperature")
async def get_temperature():
    avg_temp = get_avg_senseBox_temp()
    if avg_temp is not None:
        return {"temperature": avg_temp}
    else:
        return {"error": "Failed to fetch temperature"}
