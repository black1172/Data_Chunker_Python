
import re
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
import spacy
from nltk.corpus import stopwords

nlp = spacy.load('en_core_web_sm')


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




def generate_tags_from_text(text, top_n=8):
    # Combine NLTK and OSU-specific stopwords
    STOPWORDS = set(stopwords.words('english')).union(OSU_STOPWORDS)

    # TF-IDF keyword extraction
    vectorizer = TfidfVectorizer(stop_words=STOPWORDS, max_features=top_n)
    tfidf_matrix = vectorizer.fit_transform([text])
    tfidf_tags = vectorizer.get_feature_names_out()

    # spaCy keyphrase and entity extraction
    doc = nlp(text)
    keyphrases = set()
    for chunk in doc.noun_chunks:
        phrase = chunk.text.lower()
        if not any(word in STOPWORDS for word in phrase.split()):
            keyphrases.add(phrase)

    entities = set([ent.text.lower() for ent in doc.ents if not any(word in STOPWORDS for word in ent.text.lower().split())])

    # Combine and deduplicate tags
    tags = set(tfidf_tags) | keyphrases | entities
    tags = [tag for tag in tags if len(tag) > 2][:top_n]
    return tags

