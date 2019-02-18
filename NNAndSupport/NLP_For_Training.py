#!python3
import spacy
spacy.load('en_core_web_sm')
from spacy.lang.en import English
from spacy.matcher import Matcher

def main(toAnalyse):
    nlp = English()
    matcher = Matcher(nlp.vocab)
    doc = nlp(toAnalyse)


    keywords = []
    kdoc = nlp((open("C:\\Users\\Spencer\\Documents\\Programming\\Python\\310-Software-Engineering\\310-Software-Engineering\\NN+Support\\keywords.txt")).read())
    for token in kdoc:
        keywords.append(str(token))


    pattern = [[{'LOWER': item}] for item in keywords]
    matcher.add('Keyword', None, *pattern)
    matches = matcher(doc)
    output = []
    output2 = [0]*len(keywords)



    def addoutput(s):
        for i in range(len(keywords)):
            if s == keywords[i]:
                output2[i] = output2[i] + 1

    for match_id, start, end, in matches:
        span = doc[start:end]
        addoutput(span.text)


    return output2



