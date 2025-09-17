# we import the SentenceMastermind module
import sentence_mastermind

# We create a SentenceMastermind object with the hidden sentence "Hello, World"
# We suggest to use this sentence for testing purposes
mastermind = sentence_mastermind.SentenceMastermind("Hello, World")

# Alternatevely, we can select a random sentence from the file proverbs.txt
# We suggest to use this sentence for the final version
# sentence_mastermind.set_sentence_from_file()

# We try to guess the sentence. In order to make an "educated" guess we:
# 1. Get the length of the hidden sentence
sentence_length = mastermind.get_sentence_length()
print("sentence lenght:", sentence_length)

# 2.1 Get all characters from the file proverbs.txt. This method returns a list with all unique characters in the file.
all_characters = mastermind.get_unique_characters_in_file()
print("possible characters", all_characters)

# 2.2 Get all possible characters and punctuation marks. This method returns a list with all possible characters.
print("all possible characters", mastermind.get_all_possible_char())

# 3. We create a guess
guess = "hello, World"

# 4. We check the guess
correct_position, correct_character = mastermind.check_guess(guess)
print("correct position:", correct_position)
print("correct character:", correct_character)

# NOTES:
# - the check_guess method expect a string with exactly same length as the hidden sentence. It will ignore any extra characters in the guess.
# - the check_guess method is not case sensitive.