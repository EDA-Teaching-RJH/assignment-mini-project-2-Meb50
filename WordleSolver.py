import words

class WordList:
    def __init__(self, filepath):
        self.Words = self.load_words(filepath)
    
    def load_words(self, filepath):
        with open(filepath, "r") as file:
            return [word.strip() for word in file if len(word.strip()) == 5]
        #Loads 5 letter words from a file.