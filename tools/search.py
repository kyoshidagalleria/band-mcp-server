from datetime import datetime
from tools.core.web_search import search_web


def search_band(name: str) -> dict:
    search_result = search_web(name)

    return {
        "band_name": name,
        "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "search_result": search_result
    }