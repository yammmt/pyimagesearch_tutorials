# [Face detection with OpenCV and deep learning](https://pyimagesearch.com/2018/02/26/face-detection-with-opencv-and-deep-learning)

## Usage

First, download `deploy.prototxt` file and `res10_300x300_ssd_iter_140000.caffemodel` file from other repositories:

- `deploy.prototxt` file came from [opencv/opencv repository](https://github.com/opencv/opencv/blob/master/samples/dnn/face_detector/deploy.prototxt).
- `res10_300x300_ssd_iter_140000.caffemodel` file came from [opencv/opencv_3rdparty repository](https://github.com/opencv/opencv_3rdparty/tree/dnn_samples_face_detector_20170830).

Then, you can run these scripts:

```shell
python detect_faces.py --image rooster.jpg --prototxt deploy.prototxt.txt \
 --model res10_300x300_ssd_iter_140000.caffemodel
```

```shell
python detect_faces_video.py -p deploy.prototxt -m res10_300x300_ssd_iter_140000.caffemodel
```
