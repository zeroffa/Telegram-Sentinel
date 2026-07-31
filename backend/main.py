from fastapi import FastAPI

app = FastAPI(
    title="Telegram Sentinel",
    version="0.1.0",
    description="自架式 Telegram 安全管理平台"
)


@app.get("/")
def root():
    return {
        "name": "Telegram Sentinel",
        "version": "0.1.0",
        "status": "running"
    }
