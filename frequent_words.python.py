from collections import Counter

def frequent_words(sentence):
    words = sentence.lower().split()
    count = Counter(words)
    print(count.most_common(2))

sentence = input("Enter a sentence: ")
frequent_words(sentence)