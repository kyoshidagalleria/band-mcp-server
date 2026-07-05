from duckduckgo_search import DDGS


def _run_query(query: str, max_results: int = 10) -> list:
    with DDGS() as ddgs:
        results = list(ddgs.text(query, max_results=max_results))
    return results


def _pick_by_domain(results: list, keywords: list[str], domain_keywords: list[str] = None) -> list:
    picked = []

    for item in results:
        title = (item.get("title") or "").lower()
        href = (item.get("href") or "").lower()
        body = (item.get("body") or "").lower()

        text = f"{title} {href} {body}"

        keyword_hit = any(k.lower() in text for k in keywords)
        domain_hit = True

        if domain_keywords:
            domain_hit = any(d.lower() in href for d in domain_keywords)

        if keyword_hit and domain_hit:
            picked.append(item)

    return picked


def search_web(band_name: str) -> dict:
    queries = {
        "official": f'"{band_name}" band official site',
        "x": f'"{band_name}" band site:x.com OR site:twitter.com',
        "instagram": f'"{band_name}" band site:instagram.com',
        "youtube": f'"{band_name}" band site:youtube.com OR site:youtu.be',
    }

    raw_results = {}

    try:
        for key, query in queries.items():
            raw_results[key] = _run_query(query, max_results=10)

        official_candidates = _pick_by_domain(
            raw_results["official"],
            keywords=[band_name, "official", "band"]
        )

        x_candidates = _pick_by_domain(
            raw_results["x"],
            keywords=[band_name],
            domain_keywords=["x.com", "twitter.com"]
        )

        instagram_candidates = _pick_by_domain(
            raw_results["instagram"],
            keywords=[band_name],
            domain_keywords=["instagram.com"]
        )

        youtube_candidates = _pick_by_domain(
            raw_results["youtube"],
            keywords=[band_name],
            domain_keywords=["youtube.com", "youtu.be"]
        )

        return {
            "status": "OK",
            "band_name": band_name,
            "official_site_candidates": official_candidates[:5],
            "x_candidates": x_candidates[:5],
            "instagram_candidates": instagram_candidates[:5],
            "youtube_candidates": youtube_candidates[:5],
            "raw_results": raw_results
        }

    except Exception as e:
        return {
            "status": "ERROR",
            "band_name": band_name,
            "error": str(e)
        }