import random

#Random Word List
word_list = ["aardvark", "baboon", "camel"]

# Chose a Random Word
chosen_word = word_list[random.randint(0, len(word_list) - 1)]
print(chosen_word)

# Display '_' for each letter in the word randomly chosen
display = []
for letter in chosen_word:
    display += '_'
print(display)

# Ask the user for a letter
guessed_letter = input("Guess a letter:  ").lower()

# Check if letter user has input matches the letter in the random word and replace _ with letter.

for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if guessed_letter == letter:
        display[position] = letter

print(display)
