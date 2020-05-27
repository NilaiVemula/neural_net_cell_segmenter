# Neural Net Cell Segmenter
Goal: develop a tool using machine learning to segment images of packed epithelial cell layers (for future use in pycellfit)

Project started in May 2020 by Nilai Vemula

## Development:
- Status: Planning and Brainstorming

## To-do List:
- [ ] Background Research
- [ ] Make a FCN or other type of neural network in TensorFlow
- [ ] Write scripts to pre-process and post-process images
- [ ] Create a training set of images from the ECAD dataset (provided by James White)
- [ ] Train neural network
- [ ] Evaluate accuracy of model and continue training
- [ ] Collect code as a package

## Brainstorming and Background Research
- CSML: [Paper pre-print](https://www.biorxiv.org/content/10.1101/288720v1) & [GitHub](https://github.com/rickyota/CSML)
- Instance Segmentation: [DeepMask Review](https://towardsdatascience.com/review-deepmask-instance-segmentation-30327a072339)
- Semantic Segmentation: [FCN Review](https://towardsdatascience.com/review-fcn-semantic-segmentation-eb8c9b50d2d1)
- Tensorflow: [FCN in Tensorflow](https://towardsdatascience.com/implementing-a-fully-convolutional-network-fcn-in-tensorflow-2-3c46fb61de3b)
- FCN in Tensorflow for Segmentation: [GitHub](https://github.com/sagieppel/Fully-convolutional-neural-network-FCN-for-semantic-segmentation-Tensorflow-implementation)

## Requirements
This project should require numpy and tensorflow for developing the neural network as well as Pillow and opencv for
 some image processing. A full list of requirements is present in `requirements.txt` and should be used with a
  virtual environment based on Python 3.8.

## Test Data
For testing data, we are using a variety of images (some from James White). Each raw tif image is found in `data/raw
`. Each raw image is then loaded into SeedWaterSegmenter and is manually segmented using a watershed method. The
 output files from SeedWaterSegmenter are located in `data/ground_truth/<name_of_raw_tif>`. The watershed-segmented
  file is located in `data/ground_truth/<name_of_raw_tif>/Segments/Segment_0_000.tif`. This file is then converted to
   a black and white mesh by the `neural_net_cell_segmenter/ground_truth_preprocess.py` script. The mesh is saved in
    `data/ground_truth/<name_of_raw_tif>_mask.tif`.
