from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)
@app.get("/")
def index():
    return {"greeting": "They call me mellow yellow..."}

# @app.get("/predict")
# def predict(new_image): #new_image is a jpg does it need to be cleaned/resized?
#     load_model = joblib.load('model.joblib'). OR BELOW
#     load_model = tf.keras.models.load_model('saved_model/my_model')
#     print("model loaded")
#     health_predict = load_model.predict(new_image)
#     print("dtype", type(health_predict)) #check dtype
#     if health_predict[0] == 0:
#         health = "Unhealthy"
#     else:
#         health = "Healthy"
#     return {"health": health}
