from spacy.lang.en import English
from spacy.matcher import Matcher


#determine whether to read from file or use a single line of input
nlp = English()
matcher = Matcher(nlp.vocab)
doc = nlp('')
inputSentence = input("Enter sentence, or type '=' to enter file name instead")
if inputSentence != '=':
    doc = nlp(inputSentence);
else:
    inputFileName = input("Enter inputFile name (.txt)")
    doc = nlp((open(inputFileName)).read())

#open the keywords file and read in the flagged words
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
    #if the keyword was counted previously increment the counter
    for i in range(len(output)):
        if s == output[i]:
            output2[i] = output2[i] + 1
            return
    #otherwise add the new keyword
    output.append(s)
    output2.append(1)

#for each match call teh addoutput fucntion
for match_id, start, end, in matches:
    span = doc[start:end]
    addoutput(span.text)

#output the keywords and count to a file to open later
outputFile = open("output.txt", "w")
i = 1
while i < len(output):
    print(output[i], ": ", output2[i])
    outputStr = output[i] + " -> " + str(output2[i]) + '\n'
    outputFile.write(outputStr)
    i = i+1



