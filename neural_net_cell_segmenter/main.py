from PIL import Image
from ground_truth_preprocess import preprocess_ground_truth


def main():
    """main function that carries out all functions in pipeline"""

    # read in image as np array
    read_raw()
    preprocess_ground_truth('gonzalez')
    # send np array to neural network
    # retrieve output np array
    # convert output np array to mask
    # use opencv to perform watershed segmentation on the image
    # save segmented image


def read_raw():
    im = Image.open('data/raw/gonzalez.tif')
    # im.show()


if __name__ == '__main__':
    main()
