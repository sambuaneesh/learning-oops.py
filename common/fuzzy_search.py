import difflib


def fuzzy_search(query, choices, cutoff=0.6):
    matches = difflib.get_close_matches(query, choices, n=1, cutoff=cutoff)
    if matches:
        return matches[0]
    else:
        return None
