import tensorflow as tf
import numpy as np
import os

logdir = './tfmodels/'
savedir = './prototxt/'

from tensorflow.python import pywrap_tensorflow
ckpt = tf.train.get_checkpoint_state(logdir)
reader = pywrap_tensorflow.NewCheckpointReader(ckpt.model_checkpoint_path)
var_to_shape_map = reader.get_variable_to_shape_map()

if not os.path.exists(savedir):
    os.makedirs(savedir)

def value_reshape(value):
    from functools import reduce
    v_1d = value.reshape(reduce(lambda x, y: x * y, value.shape))
    return v_1d

def fwrite(fname, value):
    f = open(fname, 'w')
    for vv in value_reshape(value):
        f.write('    data: %.10f' % vv)
        f.write('\n')
    f.close()


for key, size in var_to_shape_map.items():
    print("tensor_name: ", key)
    print("tensor_size: ", size)
    value = np.array(reader.get_tensor(key))
    fname = key
    fname = savedir + fname.replace('/', '_') + '.prototxt'
    if value.ndim == 1:
        fwrite(fname, value)
    elif value.ndim == 2:
        # convert value.shape from [ I, O ] to [ O, I ]
        value = np.swapaxes(value, 0, 1)
        fwrite(fname, value)
    elif value.ndim == 5:
        # convert value.shape from [ L, H, W, I, O ] to [ O, I, L, H, W ]
        value = np.swapaxes(value, 0, 2)  # swap L, W
        value = np.swapaxes(value, 1, 3)  # swap H, I
        value = np.swapaxes(value, 0, 4)  # swap W, O
        fwrite(fname, value)


