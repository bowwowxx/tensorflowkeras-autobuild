import sys
import argparse
from vgg16 import VGG16
import numpy as np
from keras.preprocessing import image
from imagenet_utils import preprocess_input,decode_predictions

model = VGG16(weights='imagenet', include_top=True, input_tensor=None, input_shape=None)

a = argparse.ArgumentParser()
a.add_argument("--image", help="path to image")
args = a.parse_args()
if args.image is None:
    a.print_help()
    sys.exit(1)

if args.image is not None:
    img_path = args.image
    # img_path = 'elephant.jpg'
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    print('Input image shape:', x.shape)

    preds = model.predict(x)
    print('Predicted:', decode_predictions(preds))

