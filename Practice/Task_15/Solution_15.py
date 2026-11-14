sentence = input("Enter a sentence: ")

words = sentence.split() # split() breaks the sentence into individual words and stores them in a list.

word_count = {} #This dictionary will store each word and its frequency.

for word in words:
    if word in word_count:
        word_count[word] += 1 #If the word already exists in the dictionary, increase its count by 1.
    else:
        word_count[word] = 1 #If the word appears for the first time, add it to the dictionary with a value of 1.
        
print(word_count)