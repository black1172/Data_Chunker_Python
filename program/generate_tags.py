from collections import Counter
import re

STOPWORDS = {
    "the", "and", "of", "a", "to", "in", "is", "it", "for", "on", "with",
    "that", "as", "are", "at", "be", "from", "or", "by", "this", "an"
}

def auto_tags(text, n=6):
    tokens = re.findall(r'\b\w+\b', text.lower())
    filtered = [t for t in tokens if t not in STOPWORDS and len(t) > 2]
    most_common = [word for word, _ in Counter(filtered).most_common(n)]
    return most_common
