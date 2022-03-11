from tkinter import Image
from tensorflow.keras.models import load_model

def run_model(image):
    image=os.listdir(image)
    image=np.array(image)
    image=np.expand_dims(image,axis=0)
    s_model = load_model("modelfix.h5")
    prediction=s_model.predict(image)
    print(prediction)
    