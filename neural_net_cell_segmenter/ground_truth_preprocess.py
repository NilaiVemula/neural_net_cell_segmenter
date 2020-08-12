from inspect import currentframe, getframeinfo
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# constant value that the image array is padded with
PAD_VALUE = -1


def pad_with(vector, pad_width, iaxis, kwargs):
    """helper function that is called by np.pad to surround a nparray with a constant value
    Example: [[0,0],[0,0]] becomes [[-1,-1,-1, -1],[-1, 0, 0, -1],[-1, 0, 0, -1],[-1,-1,-1, -1]]
    """
    pad_value = kwargs.get('padder', PAD_VALUE)
    vector[:pad_width[0]] = pad_value
    vector[-pad_width[1]:] = pad_value


def preprocess_ground_truth(watershed_file_name):
    """preprocess ground truth segmented watershed from SeedWaterSegmenter into black and white mask

    :param watershed_file_name: name of the watershed segmented image (without any extensions or other folder names
    :type watershed_file_name: str
    :return: skeleton: np array where entire array is zeros except for the cell membranes with have values of 255
    :rtype: numpy.ndarray
    """
    # getting script location of package
    script_location = getframeinfo(currentframe()).filename
    parent = Path(script_location).resolve().parent

    # locating input file
    file = parent.joinpath('data/ground_truth', watershed_file_name, 'Segments/Segment_0_000.tif')
    # file = '../data/ground_truth/gonzalez/Segments/Segment_0_000.tif'

    # open the watershed segmented image
    # im = Image.open(file)
    # im.show()

    # read in watershed segmented image as a np array
    array_of_pixels = plt.imread(fname=file, format="tif")
    # print(array_of_pixels)
    # plot watershed image in matplotlib
    # plt.imshow(array_of_pixels, interpolation="nearest")
    # plt.show()
    # print(array_of_pixels.shape)

    # create a one pixel wide padding around the edge of the image for easy iteration
    padded_array = np.pad(array_of_pixels, 1, pad_with)
    # print(padded_array.shape)

    # initialize a new nparray to hold skeleton segmented image (mask)
    skeleton = np.zeros(array_of_pixels.shape)
    # print(skeleton.shape)

    # if a pixel neighbors a pixel of a different value, consider it a boundary point and add it to the skeleton image
    for row in range(1, padded_array.shape[0] - 1):
        for col in range(1, padded_array.shape[1] - 1):

            neighboring_values = [padded_array[row, col],
                                  padded_array[row, col + 1],
                                  padded_array[row + 1, col],
                                  padded_array[row + 1, col + 1]]

            # remove duplicates
            neighboring_values = list(set(neighboring_values))

            # remove padded value if in list of neighboring values
            try:
                neighboring_values.remove(PAD_VALUE)
            except ValueError:
                pass

            if len(neighboring_values) >= 2:
                skeleton[row - 1, col - 1] = 255

    # plot skeleton segmented image
    # plt.imshow(skeleton, interpolation="nearest", cmap='gray', vmin=0, vmax=255)
    # plt.show()

    # save skeleton segmented image
    im = Image.fromarray(skeleton)
    mask_name = watershed_file_name + '_mask' + '.tif'

    output_path = parent.joinpath('data/ground_truth', watershed_file_name, mask_name)
    # output_path = '../data/ground_truth/gonzalez/gonzalez_mask.tif'
    im.save(output_path)

    return skeleton
