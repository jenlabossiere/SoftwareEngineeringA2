from spacy.lang.en import English
from spacy.matcher import Matcher

nlp = English()
matcher = Matcher(nlp.vocab)
doc = nlp('')
inputSentence = input("Enter sentence, or type '=' to enter file name instead")
if inputSentence != '=':
    doc = nlp(inputSentence);
else:
    inputFileName = input("Enter inputFile name (.txt)")
    doc = nlp((open(inputFileName)).read())


keywords = []
kdoc = nlp((open("Keywords.txt")).read())
for token in kdoc:
    keywords.append(str(token))


pattern = [[{'LOWER': item}] for item in keywords]
matcher.add('Keyword', None, *pattern)
matches = matcher(doc)
output = []
output2 = []


def addoutput(s):
    for i in range(len(output)):
        if s == output[i]:
            output2[i] = output2[i] + 1
            return
    output.append(s)
    output2.append(1)


for match_id, start, end, in matches:
    span = doc[start:end]
    addoutput(span.text)

outputFile = open("output.txt", "w")
i = 1
while i < len(output):
    print(output[i], ": ", output2[i])
    outputStr = output[i] + " -> " + str(output2[i]) + '\n'
    outputFile.write(outputStr)
    i = i+1



