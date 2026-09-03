import streamlit as st
import cv2
from PIL import Image
import numpy as np

st.title("Face Detection")

upload_image = st.file_uploader("Upload the image", type=["jpg", "jpeg", "png"])

if upload_image is not None:
    image = Image.open(upload_image)

    st.image(image, use_container_width=True)

    # Convert PIL image to NumPy
    image_np = np.array(image)

    # Convert RGB to BGR for OpenCV
    image_cv = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

    # Grayscale
    gray = cv2.cvtColor(image_cv, cv2.COLOR_BGR2GRAY)

    # Load Haar Cascade
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5
    )

    # Draw rectangle
    for (x, y, w, h) in faces:
        cv2.rectangle(
            image_cv, #Target image
            (x, y), #Top-left corner point
            (x + w, y + h), #Bottom-right corner point
            (255, 0, 0), #Line color (BGR)
            2 #Line thickness
        )

    # Convert BGR to RGB
    result = cv2.cvtColor(image_cv, cv2.COLOR_BGR2RGB)

    st.subheader("Detection Result")
    st.image(result, use_container_width=True)

    st.success(f"Found {len(faces)} face/faces")
