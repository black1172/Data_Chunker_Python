import re
from collections import Counter

# Expanded stopwords list
STOPWORDS = {
    "the", "and", "is", "in", "it", "you", "of", "to", "a", "for", "on", "with",
    "at", "by", "an", "be", "this", "that", "from", "or", "as", "are", "was",
    "were", "but", "so", "if", "can", "all", "about", "into", "not", "no", "your",
    "their", "them", "they", "there", "then", "than", "such", "just", "also",
    "very", "more", "most", "some", "any", "every", "many", "because", "how",
    "what", "which", "when", "where", "who", "whom", "why", "while", "life",
    "daily", "long", "thing", "good", "new", "time", "day", "online"
}

def generate_tags_from_text(text, top_n=8):
    # Extract words and lowercase them
    words = re.findall(r"\b[a-zA-Z]{3,}\b", text.lower())
    # Remove stopwords
    words = [w for w in words if w not in STOPWORDS]
    # Count most common words
    common_words = [word for word, _ in Counter(words).most_common(top_n)]
    return common_words

