# Original paragraph
paragraph = "Artificial intelligence is the simulation of human intelligence by machines. Machines learn from data and data drives intelligence"

# Convert text to lowercase
text = paragraph.lower()

# Remove full stops
text = text.replace(".", "")

# Split paragraph into a list of words
words = text.split()

print("\nOriginal Word List:")
print(words)

# Slicing: First 5 words
print("\nFirst 5 words:")
print(words[:5])

# Slicing: Last 5 words
print("\nLast 5 words:")
print(words[-5:])

# Slicing: Every third word
print("\nEvery third word:")
print(words[::3])

# Slicing: Reverse the word list
print("\nReversed Word List:")
print(words[::-1])

# List comprehension: Words longer than 6 characters
long_words = [word for word in words if len(word) > 6]

print("\nWords longer than 6 characters:")
print(long_words)

# Dictionary comprehension: Map each word to its length
word_lengths = {word: len(word) for word in words}

print("\nWord Length Dictionary:")
print(word_lengths)