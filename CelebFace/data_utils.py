import os
import cv2
import numpy as np


def load(path='dataImages/', img_count=200):
    data = []
    images = os.listdir(path=path)
    size = 0

    for i in range(img_count):
        img = cv2.imread(os.path.join(path, images[i]))
        #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        if i==0:
            size = img.shape
        data.append(img.flatten())

    return size, data




def img2gray(img):
    gray = np.zeros((img.shape[0], img.shape[1]))

    for i in range(len(gray)):
        for j in range(len(gray[i])):
            gray[i][j] = 0.299 * img[i][j][0] + 0.587 * img[i][j][1] + 0.114 * img[i][j][2]

    return gray

if __name__ == '__main__':
    data = load()