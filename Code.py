from google.colab import files
import zipfile


# Upload the ZIP file to Google Colab
uploaded = files.upload()


# Specify the name of the uploaded ZIP file
zip_file_name = "camouflage.v5i.yolov8.zip"


# Unzip the file
with zipfile.ZipFile(zip_file_name, 'r') as zip_ref:
    zip_ref.extractall("/content/drive/MyDrive/Dip")


!pip install ultralytics

from ultralytics import YOLO

!yolo task=detect mode=train model=yolov8l.pt data=/content/drive/MyDrive/Dip/data.yaml epochs=50 imgsz=640

from ultralytics import YOLO
import cv2
import math
model=YOLO("/content/drive/MyDrive/DIP_Project/Aadditya/best(1).pt")
coco_classes =['Human', 'animal-human-detection']

results=model("/content/drive/MyDrive/DIP_Project/Aadditya/images.jpeg")

type(results)

results[0]

results_image = results[0]


output_image = results_image.render()


# Save the output image to disk
output_image.save("output_image.jpg")


# Download the output image file
from google.colab import files
files.download("output_image.jpg")
