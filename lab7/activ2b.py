def word_count(sentence):
    words = sentence.split()
    word_freq = {}
    
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    
    return len(words), word_freq

sentence = input("Enter a sentence: ")
count, frequency = word_count(sentence)

print(f"The number of words in the sentence is: {count}")
print("Word frequency:")
for word, freq in frequency.items():
    print(f"{word}: {freq}")
