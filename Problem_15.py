# Write a program (using functions!) that asks the user for a long string containing multiple words. 
# Print back to the user the same string, except with the words in backwards order. For example, say I type the string:
# My name is Michele
# Then I would see the string:
# Michele is name My
# shown back to me.

def reverse_words(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence


first_sentence =input("Enter a sentence: ")
reversed_sentence = reverse_words(first_sentence)

print("Reversed sentence:", reversed_sentence)