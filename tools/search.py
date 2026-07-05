from datetime import datetime
from tools.band_db import BAND_DB
from tools.core.web_search import search_web


def search_band(name: str) -> dict:
    if name in BAND_DB:
        return {
            "band_name": name,
            "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "source": "band_db",
            "data": BAND_DB[name]
        }

    search_result = search_web(name)

    return {
        "band_name": name,
        "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "source": "web_search",
        "search_result": search_result
    }