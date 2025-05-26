import csv
import os
import re

# Path to dataset file
DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'nine_books_data.csv')


_ARABIC_DIACRITICS = re.compile(r"[\u064B-\u065F]")


def _normalize(text: str) -> str:
    """Remove Arabic diacritics for simple matching."""
    return _ARABIC_DIACRITICS.sub("", text or "")


def search_hadith(query, max_results=5):
    """Simple search for hadith text in the local dataset.

    Args:
        query (str): Arabic text fragment to search for.
        max_results (int): maximum number of results to return.

    Returns:
        list[dict]: list of hadith records matching the query.
    """
    query = _normalize(query or '').strip()
    if not query:
        return []

    results = []
    pattern = re.compile(re.escape(query))

    with open(DATA_FILE, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            matn = _normalize(row.get('Matn', ''))
            title = _normalize(row.get('title', ''))
            if pattern.search(matn) or pattern.search(title):
                results.append({
                    'hadithID': row.get('hadithID'),
                    'BookID': row.get('BookID'),
                    'title': row.get('title'),
                    'Matn': row.get('Matn'),
                })
                if len(results) >= max_results:
                    break
    return results
