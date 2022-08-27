from PIL import Image
import numpy as np
import os
from tensorflow import keras
from keras.engine import base_layer

K = keras.backend

def mask_lemon(lemon_array,bc_array):
    lemon_mask=lemon_array.sum(axis=2)>50
    current_mask=bc_array.copy()
    current_mask[lemon_mask,:]=0
    final_img_array=current_mask+lemon_array
    return final_img_array


class BackgroundClear(base_layer.BaseRandomLayer):

    def __init__(self, random_bc_path):
        super(BackgroundClear, self).__init__()
        self.bc_img_list = [np.array(Image.open(f"{random_bc_path}/{image_path}").resize(self.original_shape[:2])) for image_path in os.listdir(random_bc_path)]

    def build(self, input_shape):
        self.original_shape = input_shape

    #@tf.function
    def call(self, inputs, is_training=None):

        is_training = K.learning_phase()

        if is_training is 1 or is_training is True:
            rng = np.random.default_rng()
            int_list=rng.integers(low=0, high=len(self.bc_img_list), size=inputs.shape[0])
            masked_img=np.array([mask_lemon(img.numpy(),self.bc_img_list[bc_id]) for img,bc_id in zip(inputs,int_list)])
            return masked_img
        else:
            return inputs
