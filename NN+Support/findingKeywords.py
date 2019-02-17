import NLP_For_Training
import tensorflow as tf
from tensorflow import keras
import numpy as np
#open the datafile
file = open("C:\\Users\\Spencer\\Documents\\Programming\\Python\\310-Software-Engineering\\310-Software-Engineering\\NN+Support\\Dataset+Feelings.txt", "r")


Dataset = []

for line in file:
	# take endline character off the 'feeling'
	line = line[:-1]
	line = line.split(";")
	Dataset.append(line)


file.close()

keywordDoc = open("C:\\Users\\Spencer\\Documents\\Programming\\Python\\310-Software-Engineering\\310-Software-Engineering\\NN+Support\\resp_keywords.txt", "r")
keywords = []
for line in keywordDoc:
	line = line.split()
	keywords.append(line)
keywordDoc.close()

for statement in Dataset:
	for word in keywords[0]:
		if statement[1] == word:
			statement[1] = keywords[0].index(word)

#run NLP on user
for statement in Dataset:
	statement[0] = NLP_For_Training.main(statement[0])

for statement in Dataset:
	print(statement[1])

#separate into input/response
input = []
resp = []
for point in Dataset:
	input.append(point[0])
	resp.append(point[1])



#separate into training and testing set
train_in = input[:-100]
train_resp = resp[:-100]
test_in = input[len(input)-100:]
test_resp = resp[len(input)-100:]

train_in = np.array(train_in)
train_resp = np.array(train_resp)
test_in = np.array(test_in)
test_resp = np.array(test_resp)

model = keras.Sequential([
	keras.layers.Dense(len(keywords[0]), activation = tf.nn.relu),
	keras.layers.Dense(128, activation = tf.nn.relu),
	keras.layers.Dense(len(keywords[0]), activation=tf.nn.softmax)
])

model.compile(
	optimizer='adam',
	loss='sparse_categorical_crossentropy',
	metrics=['accuracy']
)

model.fit(train_in, train_resp, epochs=8)

test_loss, test_acc = model.evaluate(test_in, test_resp)
print(test_acc)




#parse into user and response
#match responses

#use binary presence to create variables
#match response to the variables
#run neural net on the vairables for association





