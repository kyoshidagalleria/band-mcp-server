from mcp.server.fastmcp import FastMCP

mcp = FastMCP("band-mcp")

@mcp.tool()
def hello(name: str) -> str:
    return f"Hello {name}, MCP is working!"

@mcp.tool()
def get_band_info(name: str) -> dict:
    return {
        "name": name,
        "status": "running on Railway",
        "members": []
    }

# ★重要：RailwayではこれでHTTP起動
if __name__ == "__main__":
    mcp.run(
        transport="sse",
        host="0.0.0.0",
        port=int(__import__("os").getenv("PORT", 8000))
    )