#!/bin/bash

# Download the MediaPipe face detector model
echo "Downloading MediaPipe face detector model..."
wget -q -O detector.tflite https://storage.googleapis.com/mediapipe-models/face_detector/blaze_face_short_range/float16/1/blaze_face_short_range.tflite

# Download the dlib shape predictor model
model_path="shape_predictor_68_face_landmarks.dat"
if [ ! -f "$model_path" ]; then
    echo "Downloading dlib shape predictor model..."
    wget -q -O ${model_path}.bz2 http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
    bzip2 -dk ${model_path}.bz2
    rm ${model_path}.bz2
    echo "Download complete."
else
    echo "Dlib shape predictor model already exists."
fi
