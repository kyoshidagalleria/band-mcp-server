from mcp.server.fastmcp import FastMCP
from tools.search import search_band

mcp = FastMCP("Live Production Assistant")


@mcp.tool()
def hello(name: str) -> str:
    """動作確認用"""
    return f"Hello, {name}!"


@mcp.tool()
def get_band_info(name: str) -> dict:
    """
    バンド情報を取得する
    """
    return search_band(name)


if __name__ == "__main__":
    mcp.run(transport="streamable-http")