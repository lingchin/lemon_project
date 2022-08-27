import numpy as np
from PIL import Image


def mask_lemon_file(file_name,bc_file_name):
    lemon_image=Image.open(file_name).resize((500,500))
    background_image=Image.open(bc_file_name).resize((500,500))
    lemon_array=np.array(lemon_image)
    bc_array=np.array(background_image)
    lemon_array.sum(axis=2).shape
    lemon_mask=lemon_array.sum(axis=2)>50
    bc_array[lemon_mask,:]=0
    final_img=Image.fromarray(bc_array+lemon_array)
    return final_img

def strip_black_from_image(img):

    x_id = np.argwhere(np.max(img, axis = (1, 2)) > 0).reshape(-1)

    strip_img = img[x_id]

    y_id = np.argwhere(np.max(strip_img, axis = (0, 2)) > 0).reshape(-1)

    return strip_img[:, y_id]
