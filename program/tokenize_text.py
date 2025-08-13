import tiktoken as tt
# using tiktoken as it matches what gpt API expects

def tokenize(text):
    # Get the GPT encoding (works for GPT-3.5, GPT-4, etc.)
    encoding = tt.get_encoding("cl100k_base")
    
    # Encode text into tokens (list of ints)
    tokens = encoding.encode(text)
    
    return tokens