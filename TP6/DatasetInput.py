import imp


import matplotlib.pyplot as plt
import cv2
import numpy as np
import os

class DatasetInput:
    def __init__(self, path):
        self.path = path
        self.images = self.readImages(self.path)

    def readImages(self, path):
        imagesA = []
        imagesB = []
        images = []
        for file in os.listdir(path + "/A"):
            if file.endswith(".jpeg"):
                imgData = plt.imread(os.path.join(path + "/A", file))
                imgData = (imgData, 0)
                imagesA.append(imgData)
        for file in os.listdir(path + "/B"):
            if file.endswith(".jpeg"):
                imgData = plt.imread(os.path.join(path + "/B", file))
                imgData = (imgData, 1)
                imagesB.append(imgData)        
        for i in range(len(imagesA)):
            images.append(imagesA[i])
            images.append(imagesB[i])
        return images