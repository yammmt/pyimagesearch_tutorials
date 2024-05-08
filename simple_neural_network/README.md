# [A simple neural network with Python and Keras](https://pyimagesearch.com/2016/09/26/a-simple-neural-network-with-python-and-keras)

## Usage

Before running, you have to download image files from Kaggle.
For details, see the original tutorial.

```shell
python simple_neural_network.py --dataset kaggle_dogs_vs_cats --model output/simple_neural_network.hdf5
```

```shell
python test_network.py --model output/simple_neural_network.hdf5 --test-image test_images
```

## Differences from the original one

The original `simple_neural_network.py` code does NOT work because of the major
update of Keras. OMG.

Don't worry. I fixed them.
My `simple_neural_network.py` code works (perhaps) fine.
