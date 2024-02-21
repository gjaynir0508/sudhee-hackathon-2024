import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.models import Model
import keras
from keras.applications.resnet50 import preprocess_input, decode_predictions
import os
import numpy as np
savedModel=load_model('<modelname>') #ends with .h5
def pipeline(dir,model):
    if os.path.isfile(dir):
        try:
            img = keras.utils.load_img(dir, target_size=(300, 300))
            x = keras.utils.img_to_array(img)
            x = np.expand_dims(x, axis=0)
            x = preprocess_input(x)
            res = model.predict(x)
            return np.argmax(res)
        except (OSError, Exception) as e:
            print('Problematic file:', dir, 'Error:', e)
