def is_pangram(sentence):
    return set('abcdefghijklmnopqrstuvwxyz') == set(sentence.lower())

# Example usage
sentence = input("Enter a sentence: ")
print("The sentence is a pangram." if is_pangram(sentence) else "The sentence is not a pangram.")