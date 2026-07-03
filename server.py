from mcp.server.fastmcp import FastMCP
import os

mcp = FastMCP("band-mcp")

@mcp.tool()
def hello(name: str) -> str:
    return f"Hello {name}"

@mcp.tool()
def get_band_info(name: str) -> dict:
    return {
        "name": name,
        "status": "running",
        "members": []
    }

if __name__ == "__main__":
    # ★重要：引数なしで起動
    mcp.run()