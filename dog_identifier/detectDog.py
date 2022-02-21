# pip install opencv-python
# pip install keras
# pip install tqdm
# pip install pillow
import cv2
# import PIL
# from PIL import image
# Load pre-trained classifier for dog detection (xml file)
# face_cascade = cv2.CascadeClassifier('')

# All imports
import tensorflow
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
# from keras.applications.resnet50 import ResNet50
from tensorflow.keras.applications.resnet50 import ResNet50
from keras.preprocessing import image
from tqdm import tqdm
import numpy as np

ResNet50_model = ResNet50(weights='imagenet')


def path_to_tensor(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    return np.expand_dims(x, axis=0)


def resnet50_predict_labels(img_path):
    img = preprocess_input(path_to_tensor(img_path))
    return np.argmax(ResNet50_model.predict(img))


def dog_detector(img_path):
    prediction = resnet50_predict_labels(img_path)
    return ((prediction <= 268) & (prediction >= 151))


# print(dog_detector('sunflower.jpg'))
