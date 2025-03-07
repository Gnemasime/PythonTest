import re
from collections import Counter

def word_frequencies(text):
    # Remove punctuation and split the text into words
    words = re.findall(r'\b\w+\b', text.lower())  # Using lower() to make it case-insensitive

    # Count the frequency of each word
    word_count = Counter(words)

    # Sort words by frequency in descending order
    sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    # Display the word frequencies
    print("Word Frequencies:")
    for word, count in sorted_word_count:
        print(f"{word}: {count}")

# Test the function
text = "Hello world! This is a test. Hello, this test is only a test."
word_frequencies(text)
