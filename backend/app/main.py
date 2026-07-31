from fastapi import FastAPI

app = FastAPI(
    title="Telegram Sentinel",
    version="0.1.0",
    description="自架式 Telegram 安全管理平台"
)

@app.get("/")
async def root():
    return {
        "project": "Telegram-Sentinel",
        "status": "running",
        "version": "0.1.0"
    }
