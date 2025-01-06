from transformers import AutoTokenizer

def split(text, max_len=1024):
    tokenizer = AutoTokenizer.from_pretrained("sshleifer/distilbart-cnn-12-6")
    tokens = tokenizer.encode(text)

    token_chunks = []
    for i in range(0, len(tokens), max_len):
        chunk = tokens[i:i + max_len]
        #print(f"Token chunk size: {len(chunk)}")
        token_chunks.append(chunk)
    
    text_chunks = []
    for chunk in token_chunks:
        text_chunk = tokenizer.decode(chunk)
        #print(text_chunk)
        text_chunks.append(text_chunk)
    
    return text_chunks