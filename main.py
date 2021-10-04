import cv2
import numpy as np
from matplotlib import pyplot as plt


def convert_to_grayscale(path):
    img = cv2.imread(path)
    H, W, RGB = img.shape[:3]
    gray = np.zeros((H, W), np.uint8)
    for i in range(H):
        for j in range(W):
            gray[i, j] = np.sum(img[i, j]) / 3
    return gray


def find_image_entropy(grey_img):
    print(grey_img)


if __name__ == '__main__':
    greyImg = convert_to_grayscale('img.png')
    plt.imshow(greyImg, cmap=plt.get_cmap('gray'))
    plt.show()
