# This file contains the SentenceMastermind class
# This class is responsible for the game logic of the Sentence Mastermind game

import random
import pathlib

class SentenceMastermind:
    def __init__(self, sentence):
        """
        Initialize the SentenceMastermind class with a given sentence.
        Also, set the length of the sentence and the file path for proverbs.txt.
        """
        self.sentence = sentence.lower() # we convert the sentence to lowercase
        self.sentence_length = len(sentence)
        # we use pathlib to get the path of the file and be independent of the OS
        self.file_path = pathlib.Path(__file__).parent / "data/proverbs.txt"

    def set_sentence_from_file(self):
        """
        Set the sentence attribute to a random sentence from the file proverbs.txt.
        The file contains one sentence per line.
        Sentences starting with '#' or empty lines are ignored.
        """
        with open(self.file_path, "r") as file:
            lines = file.readlines()
            sentence = ""
            while sentence == "" or sentence[0] == "#":
                sentence = random.choice(lines).strip()
            self.sentence = sentence.lower() # we convert the sentence to lowercase
            self.sentence_length = len(sentence)
            
    def set_sentence_user(self, sentence):
        """
        Set the sentence attribute to a user-provided sentence.
        Also, update the length of the sentence.
        """
        self.sentence = sentence.lower()
        self.sentence_length = len(sentence)
    
    def get_sentence(self):
        """
        Return the current sentence.
        """
        return self.sentence
    
    def get_sentence_length(self):
        """
        Return the length of the current sentence.
        """
        return self.sentence_length
    
    def get_unique_characters_in_file(self):
        """
        Return a list with all unique characters in the file proverbs.txt.
        """
        unique_characters = set()
        with open(self.file_path, "r") as file:
            for line in file:
                line = line.lower()
                unique_characters.update(set(line.strip()))
            # convert the set to a list and sort it
            unique_characters = list(unique_characters)
            unique_characters.sort()
        return unique_characters
    
    def get_all_possible_char(self):
        """
        Return a list of possible characters and punctuation marks.
        This list is used to check if the guess is valid.
        """
        all_characters = "abcdefghijklmnopqrstuvwxyzáéíóúüñ0123456789.,;:!¿?()[]{}'\"-_/\\|@#$%^&*+=~`<> "
        # we convert the string to a list
        all_characters = list(all_characters)
        return all_characters

        
    def check_guess(self, guess):
        """
        Check the guess against the current sentence.
        Return a tuple with the number of correct characters in the correct position
        and the number of correct characters in the wrong position.
        """
        correct_position = 0
        correct_character = 0
        if len(guess) != self.sentence_length:
            raise ValueError(f"The guess must have the same length as the sentence. Given: {len(guess)}, Expected: {self.sentence_length}")

        # we check if guess is a string
        if not isinstance(guess, str):
            # if it is not a string, we convert it to a string
            # print("Guess is not a string:", guess)
            guess = ''.join(guess)
            
        guess.lower()
        # print("guess", guess)
        # print("hidden sentence", self.sentence)
        for i in range(self.sentence_length):
            if guess[i] == self.sentence[i]:
                correct_position += 1
            elif guess[i] in self.sentence:
                correct_character += 1
        return correct_position, correct_character
