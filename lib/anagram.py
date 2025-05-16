# your code goes here!
class Anagram:
    def __init__(self,word):
        self.word=word
    def match(self,possible_anagrams):
        word_sorted=sorted(self.word.lower())
        return[w for w in possible_anagrams if sorted (w.lower())==word_sorted
               and w.lower()!=self.word]
    
listen=Anagram("listen")  
listen.match(['enlists','google','inlets','banana'])
print(matches)