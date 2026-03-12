import words

class WordList:
    def __init__(self, filepath):
        self.words = self.load_words(filepath)
    
    def load_words(self, filepath):
        with open(filepath) as file:
            return [word.strip() for word in file if len(word.strip()) == 5]
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
    