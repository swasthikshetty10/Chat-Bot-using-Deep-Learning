import json
from threading import Condition 
import numpy as np
from tensorflow import keras
import colorama 
colorama.init()
from colorama import Fore, Style, Back
from sklearn.preprocessing import LabelEncoder
import random
import pickle

with open("intents.json") as file:
    data = json.load(file)


def chat():
    
    model = keras.models.load_model('chat_model')

    
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    
    with open('label_encoder.pickle', 'rb') as enc:
        lbl_encoder = pickle.load(enc)

    
    max_len = 20
    condition = True
    while condition:
        #print(Fore.LIGHTBLUE_EX + "User: " + Style.RESET_ALL, end="")
        inp = input(Fore.LIGHTBLUE_EX + "User: " + Style.RESET_ALL)
        if inp.lower() == "quit":
            condition = False

        result = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([inp]),
                                             truncating='post', maxlen=max_len))
        tag = lbl_encoder.inverse_transform([np.argmax(result)])
        print(tag)

        for i in data['intents']:
            if i['tag'] == tag:
                print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL , np.random.choice(i['responses']))
        

print(Fore.YELLOW + "Start messaging with the bot (type quit to stop)!" + Style.RESET_ALL)
chat()