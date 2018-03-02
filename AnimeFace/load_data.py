import os
from scipy.misc import imresize
from PIL import Image
import cv2
import numpy as np

def load(path='animeface-character-dataset/thumb'):
    data = []
    si = (146, 160, 3)

    for root, directory, files in os.walk(path):

        for fi in files:
            if os.path.splitext(fi)[1] == '.png':
                img = cv2.imread(os.path.join(root, fi))
                #img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
                img = imresize(img, (si[0], si[1]))
                #img = np.array(Image.fromarray(img).resize(si[0], si[1]))
                data.append(img.flatten())
            

    return data, si

def getsize(path='animeface-character-dataset/thumb'):
    x, y = 1000, 1000

    for root, directory, files in os.walk(path):

        for fi in files:
            if os.path.splitext(fi)[1] == '.png':
                img = cv2.imread(os.path.join(root, fi))
                if x > img.shape[1]:
                    x = img.shape[1]
                if y > img.shape[0]:
                    y = img.shape[0]
            

    return y, x


def img2gray(img):
    gray = np.zeros((img.shape[0], img.shape[1]))

    for i in range(len(gray)):
        for j in range(len(gray[i])):
            gray[i][j] = 0.299 * img[i][j][0] + 0.587 * img[i][j][1] + 0.114 * img[i][j][2]

    return gray

if __name__ == '__main__':
    data = load()


