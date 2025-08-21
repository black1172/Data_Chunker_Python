
# Data Chunker Python



---

## Project Overview

Many university resources are scattered across PDFs, websites, and handouts, making it difficult for students—especially freshmen—to quickly find relevant information. Data Chunker addresses this by:

- **Extracting and processing text from PDFs**, including OCR for scanned documents
- **Breaking content into manageable chunks** compatible with large language models (LLMs)
- **Generating context-aware tags** to facilitate precise search and retrieval
- **Producing structured JSON outputs** that can power chatbots or other semantic search tools

---

## Technical Highlights

- **Text Extraction:** PyMuPDF for PDFs, pytesseract for OCR
- **Chunking & Tokenization:** NLTK used to split text into overlapping segments optimized for AI input
- **Contextual Tagging:** Combines TF-IDF, spaCy keyphrases, and custom stopwords to produce meaningful tags
- **Data Output:** Structured JSON containing chunk text, metadata, tags, and source information for downstream applications

---

## Skills & Techniques Demonstrated

- **Natural Language Processing (NLP):** Tokenization, stopword filtering, TF-IDF, and entity extraction
- **Data Structuring:** Designing a reusable, structured JSON schema for AI-powered search
- **AI Integration Support:** Prepares unstructured information for LLM-based chatbots and semantic retrieval systems
- **Custom Tooling:** Automates PDF processing and tagging at scale

---

## Impact & Use Case

This project supports applications like the OSU RA Assistant, enabling first-year students and other users to access campus resources quickly and confidently. By transforming unstructured PDFs into searchable, tagged data, the assistant can provide concise, relevant, and supportive answers, reducing barriers to information access for students who may hesitate to ask for help.

---

## Example Output

Each JSON chunk includes:

- `id`: Unique identifier
- `title`: PDF title
- `source`: Original PDF filename
- `tags`: Relevant contextual tags
- `date`: Processing date
- `text`: Text content of the chunk
A Python toolkit designed to process, chunk, and tag PDF documents for resource chatbots and semantic search applications. This project was developed to structure unorganized campus information into a searchable format, enabling AI assistants to provide accurate, context-aware guidance to students.

Project Overview

Many university resources are scattered across PDFs, websites, and handouts, making it difficult for students—especially freshmen—to quickly find relevant information. The Data Chunker addresses this by:

Extracting and processing text from PDFs, including OCR for scanned documents.

Breaking content into manageable chunks compatible with large language models (LLMs).

Generating context-aware tags to facilitate precise search and retrieval.

Producing structured JSON outputs that can power chatbots or other semantic search tools.

Technical Highlights

Text Extraction: PyMuPDF for PDFs, pytesseract for OCR.

Chunking & Tokenization: NLTK used to split text into overlapping segments optimized for AI input.

Contextual Tagging: Combines TF-IDF, spaCy keyphrases, and custom stopwords to produce meaningful tags.

Data Output: Structured JSON containing chunk text, metadata, tags, and source information for downstream applications.

Skills & Techniques Demonstrated

Natural Language Processing (NLP): Tokenization, stopword filtering, TF-IDF, and entity extraction.

Data Structuring: Designing a reusable, structured JSON schema for AI-powered search.

AI Integration Support: Prepares unstructured information for LLM-based chatbots and semantic retrieval systems.

Custom Tooling: Automates PDF processing and tagging at scale.

Impact & Use Case

This project supports applications like the OSU RA Assistant, enabling first-year students and other users to access campus resources quickly and confidently. By transforming unstructured PDFs into searchable, tagged data, the assistant can provide concise, relevant, and supportive answers, reducing barriers to information access for students who may hesitate to ask for help.

Example Output

Each JSON chunk includes:

id: Unique identifier

title: PDF title

source: Original PDF filename

tags: Relevant contextual tags

date: Processing date

text: Text content of the chunk
