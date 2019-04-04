import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet as wn
import spacy as spacy
from spacy.lang.en import English
spacy.load('en_core_web_sm')
nlp = English()

inputFile = "feelings.txt"
doc = nlp((open(inputFile)).read())
words = []
for token in doc:
    words.append(str(token))

def syn(word):
    lch_threshold = 2.7
    for net1 in wn.synsets(word):
        for net2 in wn.all_synsets():
            try:
                lch = net1.lch_similarity(net2)
                if lch >= lch_threshold:
                    yield (net2)
            except:
                continue


outputFile = open("association.txt", "w")

count = 0
for i in words:
    if i.find(":") == -1:
        print(i + "finding")
        tempList = []
        for x in syn(str(i)):
            temp = str(x).split("'")
            wrd = temp[1].split(".")[0]
            tempList.append(wrd)
        tempList = list(dict.fromkeys(tempList))
        for j in tempList:
            outputFile.write(j + " ")
    else:
        outputFile.write("\n" + i)
        count = count+1