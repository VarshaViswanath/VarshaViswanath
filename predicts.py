import numpy as np
import os
from scipy import  misc
from keras.models import model_from_json
import pickle
import cv2

import os
from werkzeug.utils import secure_filename
#from gevent.pywsgi import WSGIServer
import numpy as np    
basepath = os.path.dirname(__file__)
classifier_f = os.path.join(basepath, 'static\\model', secure_filename('int_to_word_out.pickle'))    
# Loading int2word dict
classifier_f = open(classifier_f, "rb")
int_to_word_out = pickle.load(classifier_f)
classifier_f.close()

def load_model():
    json_file = os.path.join(basepath, 'static\\model', secure_filename('model_skin.json'))    
# Loading int2word dict
    # load json and create model
    json_file = open(json_file, 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    mdl = os.path.join(basepath, 'static\\model', secure_filename('model_skin.h5'))  
    loaded_model.load_weights(mdl)
    print("Loaded model from disk")
    return loaded_model

def pre_process(image):
    
    image = image.astype('float32')
    image = image / 255.0
    return image

def load_image(img):
    img = cv2.imread(img)
    image = cv2.resize(img, (64, 64))
    #image=np.array(misc.imread("images/"+img))
    #image = misc.imresize(image, (64, 64))
    image=np.array([image])
    image=pre_process(image)
    model=load_model()
    prediction=model.predict(image)
    print(prediction)
    print(np.max(prediction))
    return(int_to_word_out[np.argmax(prediction)])
    #return image

#load_image(img)


#print(prediction)
#print(np.max(prediction))
#print(int_to_word_out[np.argmax(prediction)])
