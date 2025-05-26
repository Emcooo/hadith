import importlib
import pathlib
import sys

# Ensure local package is used even if a global installation exists
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

plugin = importlib.import_module('openwebui.plugin')

def test_search_returns_results():
    res = plugin.search_hadith('الأعمال بالنيات', max_results=1)
    assert isinstance(res, list)
    assert len(res) >= 1
