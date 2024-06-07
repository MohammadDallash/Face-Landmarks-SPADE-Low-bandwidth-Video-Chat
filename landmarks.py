import dlib
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from time import time
import cv2


# Set the confidence threshold
confidence_threshold = 0.5

# Create a FaceDetector object with the specified model
base_options = python.BaseOptions(model_asset_path='detector.tflite')
options = vision.FaceDetectorOptions(base_options=base_options)
detector = vision.FaceDetector.create_from_options(options)

img_path = 'fam.jpg'

orig_image = cv2.imread(img_path)
image = cv2.cvtColor(orig_image, cv2.COLOR_BGR2RGB)

mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image)

start_time = time()
detection_result = detector.detect(mp_image)
print("Time to detect face: ", round(1000*(time() - start_time), 2), " ms")

# Load the landmark predictor model
landmark_model_path = 'shape_predictor_68_face_landmarks.dat'
landmark_predictor = dlib.shape_predictor(landmark_model_path)

for detection in detection_result.detections:
    if detection.categories[0].score >= confidence_threshold:
        bbox = detection.bounding_box
        start_point = bbox.origin_x, bbox.origin_y
        end_point = bbox.origin_x + bbox.width, bbox.origin_y + bbox.height

        # Draw the face rectangle
        cv2.rectangle(orig_image, start_point, end_point, (255, 0, 0), 1)

        face = dlib.rectangle(start_point[0], start_point[1], end_point[0], end_point[1])

        start_time = time()
        # Get the landmarks
        landmarks = landmark_predictor(image, face)
        print("Time to get landmarks: ", round (1000*(time() - start_time), 2), "ms")

        # Extract the x and y coordinates of the landmarks
        landmarks_list = [(p.x, p.y) for p in landmarks.parts()]

        # Draw landmarks on the image
        for (x, y) in landmarks_list:
            cv2.circle(orig_image, (x, y), 1, (0, 255, 0), -1)

# Save the output image with landmarks drawn
output_img_path = 'output_with_landmarks.png'
cv2.imwrite(output_img_path, orig_image)

print(f"Output image saved to {output_img_path}")
