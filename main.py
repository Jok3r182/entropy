import os

import cv2
import numpy as np
from matplotlib import pyplot as plt


def find_probabilities(grey_img):
    frequencies = np.zeros(256, np.uint8)
    H, W = grey_img.shape[:2]
    for i in range(H):
        for j in range(W):
            frequencies[grey_img[i, j]] += 1
    probabilities = [frequency / np.sum(frequencies) for frequency in frequencies]
    return [prob for prob in probabilities if prob > 0]


def calculate_entropy(probabilities):
    return np.sum([prob * np.log2(1.0 / prob) for prob in probabilities])


def convert_to_grayscale(path):
    img = cv2.imread(path)
    H, W = img.shape[:2]
    gray = np.zeros((H, W), np.uint8)
    for i in range(H):
        for j in range(W):
            gray[i, j] = np.sum(img[i, j]) / 3
    return gray


if __name__ == '__main__':
    for image_path in os.listdir('data'):
        input_path = os.path.join('data', image_path)
        greyImg = convert_to_grayscale(input_path)
        imgPixelProbabilities = find_probabilities(greyImg)

        print(image_path + ": " + str(calculate_entropy(imgPixelProbabilities)))
        plt.imshow(greyImg, cmap=plt.get_cmap('gray'))
        plt.show()
