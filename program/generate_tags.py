import re
from collections import Counter
import nltk
from nltk.stem import PorterStemmer
from nltk import pos_tag, word_tokenize
from nltk.corpus import stopwords


# OSU-specific stopwords
OSU_STOPWORDS = {
    "ohio", "state", "university", "osu", "buckeye", "campus", "student", "students",
    "faculty", "staff", "department", "office", "resources", "services", "program",
    "programs", "college", "colleges", "school", "schools", "center", "centers",
    "academic", "academics", "education", "educational", "advising", "advisor",
    "advisors", "contact", "information", "email", "phone", "address", "website",
    "homepage", "login", "apply", "application", "applications", "events", "event",
    "calendar", "news", "about", "home", "main", "menu", "search",
    "link", "links", "page", "pages", "pdf", "doc", "docs", "file", "files",
    "copyright", "reserved", "year", "date", "update", "updated", "visit",
    "location", "locations", "building", "buildings", "room", "rooms", "hours",
    "website", "web", "site", "sites", "portal", "directory", "map", "maps", "member", "members", "office", "offices"
}

# Combine NLTK and OSU-specific stopwords
STOPWORDS = set(stopwords.words('english')).union(OSU_STOPWORDS)

def generate_tags_from_text(text, top_n=8):
    # Download NLTK resources if not present
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt')
    try:
        nltk.data.find('taggers/averaged_perceptron_tagger')
    except LookupError:
        nltk.download('averaged_perceptron_tagger')

    # Tokenize and lowercase
    words = word_tokenize(text.lower())
    # Remove stopwords and non-alpha
    words = [w for w in words if w.isalpha() and w not in STOPWORDS]

    # POS tagging and noun extraction
    tagged = pos_tag(words)
    nouns = [word for word, pos in tagged if pos.startswith('NN')]

    # Stemming
    stemmer = PorterStemmer()
    stemmed_nouns = [stemmer.stem(word) for word in nouns]

    # Count most common stemmed nouns
    common_nouns = [word for word, _ in Counter(stemmed_nouns).most_common(top_n)]
    return common_nouns

