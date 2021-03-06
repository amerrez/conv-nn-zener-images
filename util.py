import glob
import os
import numpy as np
from PIL import Image
import sys
# import matplotlib.pyplot as plt



letter_output = {'O': [1.0, 0.0, 0.0, 0.0, 0.0],
                 'P': [0.0, 1.0, 0.0, 0.0, 0.0],
                 'Q': [0.0, 0.0, 1.0, 0.0, 0.0],
                 'S': [0.0, 0.0, 0.0, 1.0, 0.0],
                 'W': [0.0, 0.0, 0.0, 0.0, 1.0]}


def load_layers_definition(network_description):
    """Return a dictionary of layer_def, with the key is the index of the layer
        value is an array [feature_size, num_feature]
        For example: l = {1: [5, 4], 2:[6, 8], 3:[6,16], 4:[64]}
    """
    if os.path.isfile(network_description):
        layers = dict()  # Using dictionaries in python
        with open(network_description) as nd_file:
            layer_index = 1
            for line in nd_file:
                fn = map(int, line.rstrip('\n').split(" "))
                layers[layer_index] = fn
                layer_index += 1
        return layers
    else:
        IOError('Network description file does not exist')


def load_images(data_folder, letter):
    """Load the images in data folder and return matrix of pixels
    and matrix output letter as defined above"""
    files = glob.glob(os.path.join(data_folder, '*.png'))
    x = []
    y = []
    for f in files:
        if os.path.isfile(f):
            img = Image.open(f).convert('L')
            pixel_array = np.copy(list(img.getdata()))
            # black and white image has 1 channel
            pixel_array = pixel_array.reshape(img.size[1], img.size[0])
            x.append(pixel_array)
            filename = os.path.basename(f)
            # filename format xx_L.png, for example "12_O.PNG". So letter O is
            # at 4th position from the right(from the end of the string)
            # string[-5] will get character at 4th position started from the
            # end of the string
            letter_from_filename = filename[-5]
            if letter is not None:
                if letter == letter_from_filename:
                    y.append(1.0)
                else:
                    y.append(0.0)
    return x, y
