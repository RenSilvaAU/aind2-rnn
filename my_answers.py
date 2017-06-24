import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import keras


# TODO: fill out the function below that transforms the input series 
# and window-size into a set of input/output pairs for use with our RNN model
def window_transform_series(series,window_size):
    # containers for input/output pairs
    X = []
    y = []

    # TODO #1: Implement a function to window time series  
    for i in range(0,len(series)-window_size):
        newX = []
        for j in range(0,window_size):
            newX.append(series[i+j])
        X.append(newX)
        y.append(series[i+window_size])
    
    # TODO #1 >>> end 

    # reshape each 
    X = np.asarray(X)
    X.shape = (np.shape(X)[0:2])
    y = np.asarray(y)
    y.shape = (len(y),1)
    
    return X,y

# TODO: build an RNN to perform regression on our time series input/output data
def build_part1_RNN(step_size, window_size):
    model = Sequential()
    model.add(SimpleRNN(3,input_shape = (window_size,1),activation='linear'))
    model.add(Dense(1))


### TODO: list all unique characters in the text and remove any non-english ones
def clean_text(text):
    # find all unique characters in the text
    chars = sorted(list(set(text)))
    print('Unique Chars: P{} '.format(chars)    
    unwanted = [char for char in chars if char > 'z']
    print('Unwanted: P{} '.format(unwanted))

    # remove as many non-english characters and character sequences as you can 
    sb = len(text)
    for char in unwanted:
        text = text.replace(char,'')
    sf = len(text)
    print('Removed {} unwanted sequences'.format(sb-sf))
        
    # shorten any extra dead space created above
    text = text.replace('  ',' ')


### TODO: fill out the function below that transforms the input text and window-size into a set of input/output pairs for use with our RNN model
def window_transform_text(text,window_size,step_size):
    # containers for input/output pairs
    inputs = []
    outputs = []
    
    i = 0
    
    while i < ( len(text) - window_size ):
        new_input = text[i:i+window_size]
        inputs.append(new_input)
        outputs.append(text[i+window_size])     
        i += step_size 
        
    
    return inputs,outputs
