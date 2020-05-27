import unittest
import neural_net_cell_segmenter.ground_truth_preprocess
import numpy as np


class PadWith(unittest.TestCase):
    def test_pad_outer(self):
        a = np.zeros((2, 2))
        padded_array = np.pad(a, 1, neural_net_cell_segmenter.ground_truth_preprocess.pad_with)

        # Test 1: outer edge is -1
        self.assertEqual(padded_array[0, 0], -1)

    def test_pad_inner(self):
        a = np.zeros((2, 2))
        padded_array = np.pad(a, 1, neural_net_cell_segmenter.ground_truth_preprocess.pad_with)

        # Test 2: inner array is not changed
        self.assertEqual(padded_array[1, 1], 0)


class PreprocessGroundTruth(unittest.TestCase):
    def test_ground_truth_preprocess_min(self):
        file_name = 'gonzalez'
        skeleton = neural_net_cell_segmenter.ground_truth_preprocess.preprocess_ground_truth(file_name)

        # Test 1: min value is 0
        self.assertEqual(np.min(skeleton), 0)

    def test_ground_truth_preprocess_max(self):
        file_name = 'gonzalez'
        skeleton = neural_net_cell_segmenter.ground_truth_preprocess.preprocess_ground_truth(file_name)

        # Test 2: max value is 255
        self.assertEqual(np.max(skeleton), 255)


if __name__ == '__main__':
    unittest.main()
