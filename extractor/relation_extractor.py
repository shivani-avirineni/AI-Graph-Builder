def extract_relationships(text, entities):
    relationships = []

    words = text.split()

    for i in range(len(words) - 2):
        subj = words[i]
        rel = words[i + 1]
        obj = words[i + 2]

        # naive pattern: "X works at Y"
        if rel in ["works", "works_at"]:
            relationships.append((subj, "WORKS_FOR", obj))

        if rel in ["in", "at"]:
            relationships.append((subj, "LOCATED_IN", obj))

    return relationships