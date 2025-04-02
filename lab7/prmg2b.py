def word_count(sentence):
     words = sentence.split()
     return len(words)
sentence = input("enter a sentence:")
print(f"the number of words in the sentence is: {word_count(sentence)}")