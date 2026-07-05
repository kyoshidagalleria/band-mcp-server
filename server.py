import os
from fastapi import FastAPI
from mcp.server.fastmcp import FastMCP
from tools.search import search_band

app = FastAPI(title="GALLERIA Live Assistant")
mcp = FastMCP("GALLERIA Live Assistant")


@mcp.tool()
def hello(name: str) -> str:
    """動作確認"""
    return f"Hello, {name}!"


@mcp.tool()
def get_band_info(name: str) -> dict:
    """バンド情報を取得"""
    return search_band(name)


@app.get("/")
def root():
    return {
        "service": "GALLERIA Live Assistant",
        "status": "running"
    }


@app.get("/health")
def health():
    return {"ok": True}