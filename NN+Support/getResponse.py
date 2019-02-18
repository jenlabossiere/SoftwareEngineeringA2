import NLP_For_Training
import tensorflow as tf
import numpy as np
from tensorflow import keras


def getResponse(userInput):

    modelFile = open("C:\\Users\\Spencer\\Documents\\Programming\\Python\\310-Software-Engineering\\310-Software-Engineering\\NN+Support\\saved_model", "r")
    modelString = modelFile.read()

    model = tf.keras.models.model_from_json(modelString)

    resp_prob = model.predict(NLP_For_Training.main(userInput))

    np.argmax(resp_prob)
    



