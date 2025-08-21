import re
from collections import Counter
import nltk
from nltk.stem import PorterStemmer
from nltk import pos_tag, word_tokenize
from nltk.corpus import stopwords

# Expanded stopwords list
STOPWORDS = set(stopwords.words('english'))

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

