from collections import Counter

def freq_words():
    user_input = input("Enter a string: ")
    words = user_input.split()
    occurrences = Counter(words)
    print("Occurrences of each word:", occurrences)

freq_words()
