def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    if (len(tokens) == 0):
        return []
    if (chunk_size > len(tokens)):
        return [tokens]
    result = []
    for i in range(0, len(tokens), chunk_size - overlap):
        if i + chunk_size > len(tokens):
            break
        result.append(tokens[i:i + chunk_size])

    return result
