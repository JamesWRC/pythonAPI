from fastapi import FastAPI
import psutil

app = FastAPI()

healthCheckCount = 0
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/health")
async def health():
    global healthCheckCount
    ram = psutil.virtual_memory().percent
    cpu = psutil.cpu_percent()
    healthCheckCount += 1
    return {"ramUsage": ram, "cpuUsage": cpu, "healthCheckCount": healthCheckCount}