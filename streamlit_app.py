import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf

# Load the trained model
MODEL = tf.keras.models.load_model("saved_models/CNN_PlantVillage.h5")

CLASS_NAMES = ['Pepper bell Bacterial_spot',
               'Pepper bell healthy',
               'Potato Early blight',
               'Potato Late blight',
               'Potato healthy',
               'Tomato Bacterial spot',
               'Tomato Early blight',
               'Tomato Late blight',
               'Tomato Leaf Mold',
               'Tomato Septoria leaf spot',
               'Tomato Spider mites Two spotted spider mite',
               'Tomato Target Spot',
               'Tomato YellowLeaf Curl Virus',
               'Tomato mosaic virus',
               'Tomato healthy']

def read_file_as_image(data) -> np.ndarray:
    image = Image.open(data)
    image = image.resize((150, 150))  # Resize image to 150x150 pixels
    image = np.array(image)
    return image

def predict(image: np.ndarray):
    img_batch = np.expand_dims(image, 0)
    predictions = MODEL.predict(img_batch)
    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])
    confidence_percentage = f"{confidence * 100:.2f}%"
    return predicted_class, confidence_percentage

st.title("Plant Disease Classification")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    
    image = read_file_as_image(uploaded_file)
    predicted_class, confidence_percentage = predict(image)
    
    st.write(f"**Prediction:** {predicted_class}")
    st.write(f"**Confidence:** {confidence_percentage}")
