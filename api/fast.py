from fastapi import FastAPI, File, UploadFile
from PIL import Image
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
from tensorflow.keras import models
import tensorflow_hub as hub
from lemon_project.crop import crop_img

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

pred_model = models.load_model('model')
print("model loaded")

#tensorflow_hub model = 'SSD MobileNet V1 FPN 640x640'
model_handle = 'https://tfhub.dev/tensorflow/ssd_mobilenet_v1/fpn_640x640/1'
crop_model = hub.load(model_handle)

@app.get("/")
def index():
    return {"greeting": "They call me mellow yellow..."}


@app.post("/predict")
def predict(file: UploadFile = File(...)): #new_image is a jpg does it need to be cleaned/resized?
    image = Image.open(file.file).resize((640,640))
    image = crop_img(np.array(image),model=crop_model)
    image = Image.fromarray(image).resize((256,256))
    # print("image shape", image.shape)
    x_image = np.expand_dims(np.array(image),axis=0)
    print("image ready...", x_image.shape)

    health_predict = pred_model.predict(x_image)
    print("dtype", type(health_predict), health_predict[0][0]) #check dtype

    return {"health": float(health_predict[0][0])}
