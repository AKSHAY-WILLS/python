def merge_alternately(word1, word2):
    merged = []
    i = 0
    # Iterate over both strings and merge alternately
    while i < len(word1) or i < len(word2):
        if i < len(word1):
            merged.append(word1[i])
        if i < len(word2):
            merged.append(word2[i])
        i += 1
    return ''.join(merged)

# Example usage:
print(merge_alternately("abc", "pqr"))  # Output: "apbqcr"
print(merge_alternately("ab", "pqrs")) # Output: "apbqrs"