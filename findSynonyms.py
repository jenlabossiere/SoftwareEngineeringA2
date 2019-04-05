import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet as wn
import spacy as spacy
from spacy.lang.en import English
spacy.load('en_core_web_sm')
nlp = English()

inputFile = "feelings.txt"
doc = nlp((open(inputFile)).read())
synonyms = []
for token in doc:
    synonyms.append(str(token))

def syn(synonyms):
    lch_threshold = 2.7
    for net1 in wn.synsets(synonyms):
        for net2 in wn.all_synsets():
            try:
                lch = net1.lch_similarity(net2)
                if lch >= lch_threshold:
                    yield (net2)
            except:
                continue


outputFile = open("synonyms.txt", "w")
