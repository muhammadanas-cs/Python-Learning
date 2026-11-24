# Given sentence
text = "the cat saw the dog and the cat ran to the big dog"

# Split sentence into individual words
words = text.split()

# Create an empty dictionary
freq = {}

# Count how many times each word appears
for word in words:
    freq[word] = freq.get(word, 0) + 1

# Print all words with their frequencies
print("Word Frequencies:", freq)

# Sort words by frequency (highest to lowest)
# lambda x: x[1] sorts according to the count
# [:3] selects only the top 3 words
top3 = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:3]

# Print top 3 most frequent words
print("Top 3 Words:", top3)

# Create a list of unique words having more than 3 characters
unique_words = [word for word in freq if len(word) > 3]

# Print the list
print("Words longer than 3 characters:", unique_words)