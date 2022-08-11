import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
from matplotlib import image
import os
from tensorflow.keras import utils, layers, models, optimizers, losses, metrics
from tensorflow.keras.backend import expand_dims
from tensorflow.keras.callbacks import EarlyStopping

train_data = utils.image_dataset_from_directory('../raw_data/Test_lemon', seed = 1,validation_split = 0.2, subset = 'training')
validation_data = utils.image_dataset_from_directory('../raw_data/Test_lemon', seed =1, validation_split = 0.2, subset = 'validation')

def initialize_model():

    model = models.Sequential()
    
    ### Resizing layer before Model
    model.add(layers.Resizing(128,128, input_shape=(256, 256, 3)))

    ### First Convolution & MaxPooling
    model.add(layers.Conv2D(8, (28,28), activation='relu', padding='same', input_shape=(128,128, 3)))
    model.add(layers.MaxPool2D(pool_size=(2,2)))
    
    ### Second Convolution & MaxPooling
    model.add(layers.Conv2D(16, (3,3), activation='relu'))
    model.add(layers.MaxPool2D(pool_size=(2,2)))
    
    ## Extra Layers just for fun ##
    model.add(layers.Conv2D(64, (3,3), activation='relu'))
    model.add(layers.MaxPool2D(pool_size=(2,2)))
    
    model.add(layers.Conv2D(64, (3,3), activation='relu'))
    model.add(layers.MaxPool2D(pool_size=(2,2)))
    
    ### Flattening
    model.add(layers.Flatten())
    
    ### One Fully Connected layer - "Fully Connected" is equivalent to saying "Dense"
    model.add(layers.Dense(10, activation='relu'))
    
    ### Last layer - Classification Layer with 10 outputs corresponding to 10 digits
    model.add(layers.Dense(1, activation='sigmoid'))
    
    ### Model compilation
    model.compile(loss='binary_crossentropy',  #'sparse_categorical_crossentropy'
                  optimizer='adam', 
                  metrics=['accuracy'])
    return model

model = initialize_model()

es = EarlyStopping()

histroy = model.fit(train_data, 
          batch_size=2, 
          epochs=5,
          validation_data = validation_data
          )

print(model.evaluate(train_data, verbose=0))

# models.save_model(model, 'basic_model_02')


