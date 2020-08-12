import numpy as np
from PIL import Image

def main():
    original_image = Image.open('data/raw/gonzalez.tif')
    original_image_array = np.asarray(original_image)
    print(original_image_array)

    mask_image = Image.open('data/ground_truth/gonzalez/gonzalez_mask.tif')
    mask_image_array = np.asarray(mask_image)
    print(mask_image_array)

if __name__ == '__main__':
    main()