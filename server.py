from mcp.server.fastmcp import FastMCP

mcp = FastMCP("band-mcp")


@mcp.tool()
def hello(name: str) -> str:
    return f"Hello, {name}!"


@mcp.tool()
def get_band_info(name: str) -> dict:
    return {
        "name": name,
        "members": [],
        "status": "準備中"
    }


if __name__ == "__main__":
    mcp.run(transport="streamable-http")