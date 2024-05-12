# [Deep Learning with OpenCV](https://pyimagesearch.com/2017/08/21/deep-learning-with-opencv)

## Usage

You can download these files from the outside of this repository:

- `bvlc_googlenet.prototxt` file from [opencv repository](https://github.com/opencv/opencv_extra/blob/4.x/testdata/dnn/bvlc_googlenet.prototxt)
- `bvlc_googlenet.caffemodel` file from [GoogleNet publication](https://github.com/BVLC/caffe/blob/master/models/bvlc_googlenet/readme.md)
  - The above link is for GitHub repository which includes descriptions of this
- `csynset_words.txt` file via [caffe repository](https://github.com/BVLC/caffe/blob/master/data/ilsvrc12/get_ilsvrc_aux.sh)
  - >`wget -c http://dl.caffe.berkeleyvision.org/caffe_ilsvrc12.tar.gz`

Note that the above links for `master` blob, not for the specific commit,
may not be valid in the future.

```shell
python deep_learning_with_opencv.py --image images/jemma.png \
    --prototxt bvlc_googlenet.prototxt \
    --model bvlc_googlenet.caffemodel --labels synset_words.txt
```
