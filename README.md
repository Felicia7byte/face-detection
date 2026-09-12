# face-detection
A simple face detection application built with Python, OpenCV, and Streamlit using the Haar Cascade classifier.
# Features
- Upload JPG, JPEG, or PNG images
- Detect faces in uploaded images
- Draw bounding boxes around detected faces
- Display the original and processed images
- Show the total number of detected faces
- Simple and interactive interface built with Streamlit
# Tech Stack
Python, Streamlit, OpenCV, Pillow, NumPy, Haar Cascade Classifier
# How It Works
Upload Image → Convert Image to NumPy Array → Convert to Grayscale → Haar Cascade Face Detection → Draw Bounding Boxes → Detection Result

The image is first converted from a PIL image into a NumPy array and then converted from RGB to BGR format for OpenCV processing. The image is converted to grayscale before the Haar Cascade classifier detects faces. For each detected face, the application draws a bounding box around the detected region and displays the total number of detected faces.
# Detection Method
Haar Cascade Classifier
# Live Demo
https://face-detection-haarcascades.streamlit.app/
