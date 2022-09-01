import tensorflow as tf

import numpy as np



def crop_img(image,model):
    X = np.expand_dims(image, axis = 0)

    # running inference
    results = model(X)

    first_lemon_id = np.argwhere(results['detection_classes'].numpy()[0] == 55)[0][0] # class 55 = orange

    bbox = (results['detection_boxes'][0][first_lemon_id] * 640).numpy().astype(int)

    ymin, xmin, ymax, xmax = bbox

    padding = 8
    new_img = X[0][ymin-padding:ymax+padding, xmin-padding:xmax+padding]

    return new_img
