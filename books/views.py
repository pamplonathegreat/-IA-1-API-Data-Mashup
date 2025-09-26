import requests
from django.shortcuts import render

BOOKS_API = "https://openlibrary.org/search.json"

def index(request):
    query = request.GET.get("q", "harry potter")  # default query
    context = {"query": query, "results": [], "error": None}

    try:
        r = requests.get(BOOKS_API, params={"title": query}, timeout=10)
        if r.status_code != 200:
            context["error"] = f"Book API error (HTTP {r.status_code})"
            return render(request, "books/index.html", context)

        data = r.json()
        docs = data.get("docs", [])
        if not docs:
            context["error"] = "No books found."
            return render(request, "books/index.html", context)

        for d in docs[:5]:  # show first 5 results only
            title = d.get("title")
            author = ", ".join(d.get("author_name", []))
            year = d.get("first_publish_year")
            cover_id = d.get("cover_i")
            cover_url = f"https://covers.openlibrary.org/b/id/{cover_id}-M.jpg" if cover_id else None

            context["results"].append({
                "title": title,
                "author": author or "Unknown",
                "year": year or "N/A",
                "cover": cover_url,
                "title_length": len(title) if title else 0,  # computed field
            })

    except requests.RequestException:
        context["error"] = "Network error. Please retry."

    return render(request, "books/index.html", context)
