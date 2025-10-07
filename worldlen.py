def longest_word_length(words):
    max_length = 0
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
    return max_length

# Example usage:
words_list = ["apple", "banana", "cherrys", "date"]
print(longest_word_length(words_list))  # Output: 6
  
