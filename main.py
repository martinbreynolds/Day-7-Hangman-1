import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = word_list[random.randint(0,len(word_list)-1)]
print(chosen_word)

display = []
for letter in chosen_word:
  display.append('_')

guess = input("Guess a letter:  ").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for letter in chosen_word:
  if guess == letter:
    print("Right")
  else:
    print("Wrong")

print(display)