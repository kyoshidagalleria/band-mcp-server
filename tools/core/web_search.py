from duckduckgo_search import DDGS


def _run_query(query: str, max_results: int = 5) -> list:
    with DDGS() as ddgs:
        results = list(ddgs.text(query, max_results=max_results))
    return results


def search_web(band_name: str) -> dict:
    queries = [
        f"{band_name} バンド",
        f"{band_name} official",
        f"{band_name} X",
        f"{band_name} Instagram",
        f"{band_name} YouTube",
    ]

    all_results = {}

    try:
        for query in queries:
            all_results[query] = _run_query(query, max_results=5)

        return {
            "status": "OK",
            "band_name": band_name,
            "results_by_query": all_results
        }

    except Exception as e:
        return {
            "status": "ERROR",
            "band_name": band_name,
            "error": str(e)
        }