# [Eye blink detection with OpenCV, Python, and dlib](https://pyimagesearch.com/2017/04/24/eye-blink-detection-opencv-python-dlib)

## Usage

For input video stream, this code uses a built-in webcam or USB camera.
This means the argument to `-v`/`--video` is ignored.

```shell
python detect_blinks.py -p <path to facial landmark predictor>
```

As facial landmark predictor, I use `shape_predictor_68_face_landmarks.dat` file.
