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

#open and read response keyword doc into the resp_keywords list
keywordDoc = open("C:\\Users\\Spencer\\Documents\\Programming\\Python\\310-Software-Engineering\\310-Software-Engineering\\NN+Support\\resp_keywords.txt", "r")
resp_keywords = []
for line in keywordDoc:
	line = line.split()
	resp_keywords.append(line)
keywordDoc.close()


#get the user flagged words and store in keywords
keywords = []
kdoc = open("C:\\Users\\Spencer\\Documents\\Programming\\Python\\310-Software-Engineering\\310-Software-Engineering\\NN+Support\\keywords.txt","r")
for line in kdoc:
	line = line.split()
	keywords.append(line)
kdoc.close()


#translate keyword doc into numbered catagories
#adaptive so we can add flagged words later
for statement in Dataset:
	for word in resp_keywords[0]:
		if statement[1] == word:
			statement[1] = resp_keywords[0].index(word)

#run NLP on each user input
for statement in Dataset:
	statement[0] = NLP_For_Training.main(statement[0])

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

#transform the nested lists into 2D arrays for the model
train_in = np.array(train_in)
train_resp = np.array(train_resp)
test_in = np.array(test_in)
test_resp = np.array(test_resp)

#define the neural network
model = keras.Sequential([
	#layer 1: as many nodes as there are input variables
	keras.layers.Dense(len(keywords[0]), activation = tf.nn.relu),
	#layer 2: 128 nodes
	keras.layers.Dense(128, activation = tf.nn.relu),
	#layer 3: probability adding to 1 for each possible catagory
	#max of probabilities is selected
	keras.layers.Dense(len(resp_keywords[0]), activation=tf.nn.softmax)
])

#create the model and specify how it will train
model.compile(
	optimizer='adam',
	loss='sparse_categorical_crossentropy',
	metrics=['accuracy']
)

#train the model and do it 8 times
model.fit(train_in, train_resp, epochs=100)

#find how accurate the model is
test_loss, test_acc = model.evaluate(test_in, test_resp)
print(test_acc)


predictions = model.predict(test_in)
i = 0
for guess in predictions:
	print(np.argmax(guess))
	print(test_resp[i])
	print()
	i = i + 1
model.summary()
model.save("C:\\Users\\Spencer\\Documents\\Programming\\Python\\310-Software-Engineering\\310-Software-Engineering\\NN+Support\\saved_model.h5")


model_stored = model.to_json()
model_file = open("C:\\Users\\Spencer\\Documents\\Programming\\Python\\310-Software-Engineering\\310-Software-Engineering\\NN+Support\\saved_model.txt", "w")
model_file.write(model_stored)
model_file.close()

#parse into user and response
#match responses

#use binary presence to create variables
#match response to the variables
#run neural net on the vairables for association





