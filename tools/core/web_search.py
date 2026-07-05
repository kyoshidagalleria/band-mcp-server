from duckduckgo_search import DDGS


def search_web(query: str) -> dict:
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=5))

        return {
            "status": "OK",
            "query": query,
            "results": results
        }

    except Exception as e:
        return {
            "status": "ERROR",
            "query": query,
            "error": str(e)
        }