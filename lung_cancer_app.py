import streamlit as st
from PIL import Image
import numpy as np

# Title
st.title("Lung Cancer Disease Identification")

# Description
st.write("Upload a lung CT/X-ray image for prediction")

# Upload image
uploaded_file = st.file_uploader(
    "Choose a Lung Image",
    type=["jpg", "png", "jpeg"]
)

if uploaded_file is not None:

    # Open image
    image = Image.open(uploaded_file)

    # Display image
    st.image(
        image,
        caption="Uploaded Lung Image",
        use_container_width=True
    )

    # Convert image to array
    img_array = np.array(image)

    # Dummy prediction logic
    prediction = np.random.choice([
        "Lung Cancer Detected",
        "No Lung Cancer Detected"
    ])

    # Predict button
    if st.button("Predict"):
        st.subheader("Prediction Result")
        st.success(prediction)
