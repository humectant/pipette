import uvicorn
from fastapi import FastAPI

from app.api.apiv_v1 import tasks, experiments

app = FastAPI()


@app.get("/")
async def root():
    return {"what": "pipette"}


app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
app.include_router(experiments.router, prefix="/experiments", tags=["experiments"])

if __name__ == "__main__":
    # For development purposes only
    uvicorn.run(app, host="0.0.0.0", port=80, log_level="info")
