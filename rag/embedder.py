def get_embedding(text, dim=10):
    words = text.split()
    vec = [sum(ord(c) for c in word) % 1000 for word in words]

    # ensure fixed size
    if len(vec) < dim:
        vec += [0] * (dim - len(vec))
    else:
        vec = vec[:dim]

    return vec
