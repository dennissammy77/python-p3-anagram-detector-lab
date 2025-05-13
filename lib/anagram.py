class Anagram:
    def __init__(self, word):
        self.word = word
        self.sorted_word = sorted(word)

    def match(self, candidates):
        return [w for w in candidates if sorted(w) == self.sorted_word]
