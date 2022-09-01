from fastapi import FastAPI, File, UploadFile
from PIL import Image
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
from tensorflow.keras import models

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

@app.get("/")
def index():
    return {"greeting": "They call me mellow yellow..."}



@app.post("/predict")
def predict(file: UploadFile = File(...)): #new_image is a jpg does it need to be cleaned/resized?
    image = Image.open(file.file).resize((256,256))
    image = np.array(image)
    print("image shape", image.shape)
    x_image = np.expand_dims(image,axis=0)
    print("image ready...", x_image.shape)

    health_predict = pred_model.predict(x_image)
    print("dtype", type(health_predict), health_predict[0][0]) #check dtype

    return {"health": float(health_predict[0][0])}
