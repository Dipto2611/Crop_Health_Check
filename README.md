# 🌿 AI-Based Plant Leaf Disease Detection System

This project presents a web-based deep learning application designed to classify plant leaf images as **Healthy** or **Diseased** using a Convolutional Neural Network (CNN). The goal of this system is to demonstrate how Artificial Intelligence can assist in early plant disease detection through an accessible and user-friendly interface.

## 📌 Project Highlights

- Developed a CNN-based binary image classification model for plant leaf health detection.
- Trained the model on labeled plant leaf images resized to 224×224 pixels.
- Used **Binary Crossentropy** as the loss function and **Adam** as the optimizer.
- Saved the trained model in `.h5` format for deployment.
- Integrated the model into a **Flask-based web application**.
- Built a simple HTML interface allowing users to upload images and receive instant predictions.
- Displays prediction result along with confidence percentage.
- Demonstrates real-world application of AI in agriculture.

## 🛠 Technologies Used

- Python  
- TensorFlow / Keras  
- Flask  
- HTML & CSS  
- NumPy  
- Pillow  

## 🚀 How It Works

1. User uploads a plant leaf image.
2. The image is resized and normalized.
3. The preprocessed image is passed to the trained CNN model.
4. The model predicts whether the leaf is Healthy or Diseased.
5. The result is displayed on the web interface in real time.

This project showcases end-to-end implementation of an AI solution — from model training to web deployment — highlighting practical application of deep learning in solving real-world agricultural problems.

## UI
![alt text](<pic1.png>) 
![alt text](<pic2.png>)
![alt text](<pic3.png>)