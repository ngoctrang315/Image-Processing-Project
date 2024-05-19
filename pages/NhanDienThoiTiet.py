import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import matplotlib.pyplot as plt
import os
import json
import streamlit as st
import cv2
from tempfile import NamedTemporaryFile

# Load the model from the .h5 file
model = tf.keras.models.load_model(r"C:\Users\ngchn\Downloads\weather\WeatherImageRecognition-main\model_DenseNet201.h5")

# Load the class indices from the saved file
with open(r"C:\Users\ngchn\Downloads\weather\WeatherImageRecognition-main\class_indices.json", 'r') as f:
    class_indices = json.load(f)

# Function to preprocess the image
def preprocess_image(image_path, target_size=(100, 100)):
    img = load_img(image_path, target_size=target_size)  # Load image
    img_array = img_to_array(img)  # Convert image to array
    img_array = np.expand_dims(img_array, axis=0)  # Expand dimensions to match model input
    img_array = tf.keras.applications.densenet.preprocess_input(img_array)  # Preprocess for DenseNet
    return img_array

# Function to predict the class of the image
def predict_image_class(image_path, model):
    img_array = preprocess_image(image_path)
    prediction = model.predict(img_array)
    predicted_class_index = np.argmax(prediction, axis=1)[0]
    predicted_class_label = class_indices.get(str(predicted_class_index), "Unknown")
    return predicted_class_label

# Function to display the image with prediction
def display_image_with_prediction(image_path, predicted_class_label):
    img = load_img(image_path)
    plt.imshow(img)
    plt.title(f"Predicted: {predicted_class_label}")
    plt.axis('off')
    st.pyplot(plt)

# File uploader
image_file = st.file_uploader("Upload Your Image", type=['jpg', 'png', 'jpeg', 'tif'])

if image_file is not None:
    # Save the uploaded file to a temporary file
    with NamedTemporaryFile(delete=False, suffix=image_file.name.split('.')[-1]) as temp_file:
        temp_file.write(image_file.getbuffer())
        temp_image_path = temp_file.name

    # Predict the class of the image
    predicted_class_label = predict_image_class(temp_image_path, model)

    # Display the predicted class
    st.write(f"Predicted class: {predicted_class_label}")

    # Display the image with the prediction
    display_image_with_prediction(temp_image_path, predicted_class_label)