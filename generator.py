import re
import reprlib
RE_WORD = re.compile('\w+')
class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        print("on est dans __iter__ de Sentence")
        return SentenceIterator(self.words)

class SentenceIterator:
    def __init__(self, words):
        self.words = words
        self.index = 0
        print("on est dans __init__ de SentenceIterator")

    def __next__(self):
        
        try:
            print("on est dans __next_ de SentenceIterator")
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()

        self.index += 1
        

        return word

    def __iter__(self):
        return self

def gen_123():
    yield 1
    yield 2
    yield 3
    
#if __name__ == "__main__":
#myiter = Sentence("A B C")
#c=iter(myiter)
