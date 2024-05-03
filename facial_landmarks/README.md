# [Facial landmarks with dlib, OpenCV, and Python](https://pyimagesearch.com/2017/04/03/facial-landmarks-dlib-opencv-python/)

## Usage

For shape predictor, the original tutorial uses `shape_predictor_68_face_landmarks.dat` file.

```shell
python facial_landmarks.py -p <path to shape predictor> -i <path to image file>
```

## dlib on mac

In my environment (macOS 14.4.1), I failed to install `dlib` Python package.

To fix the error I had encountered, I had to remove (or rename) `/usr/local/include` directory.
For details, see [Stack Overflow](https://stackoverflow.com/questions/77250743/mac-xcode-g-cannot-compile-even-a-basic-c-program-issues-with-standard-libr).
