import words
import re

class WordList:
    def __init__(self, filepath):
        self.words = self.load_words(filepath)
    
    def load_words(self, filepath):
        with open(filepath, "r") as file:
            return [word.strip().lower() for word in file if len(word.strip()) == 5]
        #Loads 5 letter words from a file.

class WordleGame:
    def __init__(self):
        self.history = [ ]
    
    def add_guess(self, guess, result):
        self.history.append(guess, result)
    #Stores guesses and results

class WordleSolver:
    def __init__(self, words):
        self.candidates = words

    def apply_guess(self, guess, result):
        pass

    def suggest_word(self):
        pass
    #Filters out all the impossible words, and gives possible suggestions for words.

def filter_green(words, guess, result):
    pattern = " "
    for i in range(len(result)):
        if result[i] == "g":
            pattern += guess[i]
        else:
            pattern += "."
        
        regex = "^" + pattern + "$"
        return [word for word in words if re.match(regex, word)]
    #filters words based on green letters(correct positioning)

def filter_red(words, guess, result):
    filtered = []

    for word in words:
        valid = True

        for i in range(len(result)):
            if result[i] == "r" and guess[i] in word:
                valid = False
        
        if valid:
            filtered.append(word)

    return filtered
    #removes words containing letters marked as red (not in the wordle)