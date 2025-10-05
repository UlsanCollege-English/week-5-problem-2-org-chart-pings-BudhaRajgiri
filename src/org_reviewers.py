# src/org_reviewers.py

def count_senior(node, min_level):
    if node is None:
        return 0

    # current person qualifies?
    count = 1 if node.get("level", 0) >= min_level else 0

    # get reports (default empty list if missing)
    for child in node.get("reports", []):
        count += count_senior(child, min_level)

    return count
