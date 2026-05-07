import streamlit as st
from PIL import Image
import numpy as np

# Title
st.title("Brain Tumor MRI Detection")

# Description
st.write("Upload an MRI image for prediction")

# Upload image
uploaded_file = st.file_uploader("Choose an MRI Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:

    # Open image
    image = Image.open(uploaded_file)

    # Display image
    st.image(image, caption="Uploaded MRI Image", use_container_width=True)

    # Convert image to array
    img_array = np.array(image)

    # Dummy prediction logic
    prediction = np.random.choice(["Tumor Detected", "No Tumor Detected"])

    # Button
    if st.button("Predict"):
        st.subheader("Prediction Result")
        st.success(prediction)
