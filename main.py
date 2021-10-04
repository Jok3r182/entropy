from PIL import Image
import numpy as np
from matplotlib import pyplot as plt


def convert_to_grayscale(path):
    img = Image.open(path)
    return np.dot(img[..., :3], [0.299, 0.587, 0.144])


def find_image_entropy(grey_img):
    print(grey_img)


if __name__ == '__main__':
    greyImg = convert_to_grayscale('img.png')
    plt.imshow(greyImg, cmap=plt.get_cmap('gray'))
    plt.show()
