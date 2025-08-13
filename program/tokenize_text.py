import re

def tokenize(text):
    # Lowercase and split by words
    tokens = re.findall(r"\b\w+\b", text.lower())
    return tokens