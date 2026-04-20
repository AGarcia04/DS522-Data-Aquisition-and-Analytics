"""
DS 522 - Programming Exercise 02
Part 1: Simple Text Processing

Question: What is the importance of text processing?
Text processing is essential in data analytics and NLP. For example, in spam detection,
counting word frequencies helps identify patterns words like "free" or "winner" appear
far more in spam emails. Cleaning punctuation ensures the analysis focuses on content.
"""

import string

# Open and read the file
with open("/Users/alexgarcia/Desktop/CityUniversity/MSDS/DS522 Data Aquisition and Analytics/Modules/Module2/PE02/poem.txt", "r") as f:
    text = f.read()

# Remove all punctuation
cleaned = text.translate(str.maketrans("", "", string.punctuation))

# Count character frequencies 
char_count = {}
for ch in cleaned:
    if not ch.isspace():
        char_count[ch.lower()] = char_count.get(ch.lower(), 0) + 1

print("=== Character Frequencies ===")
for char, count in sorted(char_count.items(), key=lambda x: x[1], reverse=True):
    print(f"  '{char}': {count}")

# Count word frequencies
words = cleaned.lower().split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("\n=== Word Frequencies ===")
for word, count in sorted(word_count.items(), key=lambda x: x[1], reverse=True):
    print(f"  '{word}': {count}")

# Remove the most frequent word(s)
max_freq = max(word_count.values())
most_common = [w for w, c in word_count.items() if c == max_freq]

print(f"\nRemoving most frequent word(s): {most_common} (appeared {max_freq} times)")

filtered_words = [w for w in words if w not in most_common]
print("\n=== Text After Removal ===")
print(" ".join(filtered_words))