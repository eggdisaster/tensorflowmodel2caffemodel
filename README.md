# tensorflowmodel2caffemodel

This is a repository trying to convert tensorflow model to caffe model in 3D ConvNet.
Our model is finetuned from [sports1m_finetuning_ucf101.model](https://www.dropbox.com/sh/8wcjrcadx4r31ux/AAAkz3dQ706pPO8ZavrztRCca?dl=0) in [C3D-tensorflow](https://github.com/hx173149/C3D-tensorflow).


## Requirements:
- Install caffe and tensorflow is necessary.
- Prepare a tensorflow model or download our [c3d_ucf_model-3999](https://www.dropbox.com/sh/zxytvmis1o6ps3b/AACcAJRV6fO-Ol2UTOUVCwHZa?dl=0) finetuning model.



## Read tensor values from tensorflow model
- Copy the tensorflow finetuning model (including .data, .index, .meta, checkpoint) to `./tfmodel/`.
- Run `read_tfmodel.py`.

Tensor's values will be saved in `./prototxt/` respectively like this:
```
    data: 0.8835785389
    data: 0.9362567067
    ...
    data: 0.9228050709
    data: 0.9576351643
```

## Prepare the model.prototxt
If you are familiar with caffe and prepare the prototxt by yourself, please skip first step.

1. Read caffe model from [conv3d_deepnetA_sport1m_iter_1900000](https://www.dropbox.com/s/mihrgqarchxd643/conv3d_deepnetA_sport1m_iter_1900000?dl=0).
    - Replace all the 'write_model' by 'read_model' in `CMakeLists.txt`.
    - Change 'include_directories' to your Caffe path.
    - run
```
$ cmake .
$ make
$ ./read_model
```
- Note:
    1. You can run `delete_data.py` to generate a smaller file without data.
    2. Here we provide a example model without data as `conv3d_deepnetA_sport1m_iter_1900000_without_data.txt`

2. Split the prototxt to insert data in order.

```
# layer1_part1.prototxt
layers {
  bottom: "data"
  top: "conv1a"
  name: "conv1a"
  type: VIDEO_DATA
  blobs {
    num: 64
    channels: 3
    length: 3
    height: 3
    width: 3
# data_weight.prototxt
    data: 0.2204105258
    ...
    data: 0.0074834488
# layer1_part2.prototxt
  }
  blobs {
    num: 1
    channels: 1
    length: 1
    height: 1
    width: 64
# data_biases.prototxt
    data: -0.1619068235
    ...
    data: 0.5050196052
# layer1_part3.prototxt
  }
  blobs_lr: 1
  blobs_lr: 2
  weight_decay: 1
  weight_decay: 0
  convolution_param {
    num_output: 64
    pad: 1
    kernel_size: 3
    kernel_depth: 3
    weight_filler {

      type: "gaussian"
      std: 0.01
    }
    bias_filler {
      type: "constant"
      value: 0
    }
    temporal_pad: 1
  }
}
```

3. Record the index one by one in `index.txt`.

4. Concatenate the prototxt file by running
```
$ bash ss.sh
```

## Transfer model.prototxt to caffe.caffemodel
- Replace all the 'read_model' by 'write_model' in `CMakeLists.txt`.
- Change 'include_directories' to your Caffe path.
- run
```
$ cmake .
$ make
$ ./write_model
```


## References:
- Read and save tensorflow var name and value. https://blog.csdn.net/wc781708249/article/details/78040735
- Read and write caffemodel. https://blog.csdn.net/jiongnima/article/details/72904526