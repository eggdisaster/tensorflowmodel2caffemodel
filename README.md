# tensorflowmodel2caffemodel

## Install caffe and tensorflow is necessary.

## Prepare prototxt and tensorflow model.
Download C3D-tensorflow finetuning model [c3d_ucf_model-3999](https://www.dropbox.com/sh/zxytvmis1o6ps3b/AACcAJRV6fO-Ol2UTOUVCwHZa?dl=0)
Our model is finetuned from [sports1m_finetuning_ucf101.model](https://www.dropbox.com/sh/8wcjrcadx4r31ux/AAAkz3dQ706pPO8ZavrztRCca?dl=0) in [C3D-tensorflow](https://github.com/hx173149/C3D-tensorflow)


## Read tensor values from tensorflow model.
1.Copy the tensorflow finetuning model(contain .data .index, .meta, checkpoint) into `./tfmodel/`.
2.Run `read_tfmodel.py`
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
### 1.Read caffe model from [conv3d_deepnetA_sport1m_iter_1900000](https://www.dropbox.com/s/mihrgqarchxd643/conv3d_deepnetA_sport1m_iter_1900000?dl=0).
Replace all the `write_model` by `read_model` in `CMakeLists.txt` and change 'include_directories' to your Caffe path.
run
```
$ cmake .
$ make
$ ./read_model
```
You can run `delete_data.py` to generate a smaller file without data.
Here we provide a example model without data as `conv3d_deepnetA_sport1m_iter_1900000_without_data.txt`

### 2.Split the prototxt to insert data in order.
layer1_part1.prototxt
```
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
```
data_weight.prototxt

```
    data: 0.8835785389
    ...
    data: 0.9576351643
```
layer1_part2.prototxt
```
  }
```
...

### 3.Record the index one by one in `index.txt`.

### 4.Concatenate the prototxt file by running
```
$ bash ss.sh
```

## Transfer model.prototxt to caffe.caffemodel
Replace all the `read_model` by `write_model` in `CMakeLists.txt` and change 'include_directories' to your Caffe path.
run
```
$ cmake .
$ make
$ ./write_model
```


## References:
https://blog.csdn.net/wc781708249/article/details/78040735
https://blog.csdn.net/jiongnima/article/details/78382972