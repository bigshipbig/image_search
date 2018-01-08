import sys
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

"""
@Brief: draw the histogram of the picture
"""

class PictureHistogram():
    """
    @Brief: The class of getting histogram of picture
    """
    def __init__(self, Img):
        """
        @Brief: init this class
        """
        self.image = Img

    def trans2gray(self):
        """
        @Brief: get the gray picture
        """
        return self.image.convert('L')

    def show_origin_picture(self):
        """
        @Brief: show original picture
        """
        self.image.show()

    def draw_histogram(self, color="gray"):
        """
        @Brief: draw histogram
        """
        if color == "gray":
            self.draw_gray_histogram()
        elif color == "rgb":
            self.draw_rgb_histogram()

    def draw_gray_histogram(self):
        """
        @Brief: draw gray histogram
        """
        gray_image = np.array(self.trans2gray())
        color_dis = np.zeros((1,256))
        shape = gray_image.shape
        for raw in range(shape[0]):
            for col in range(shape[1]):
                color_dis[0][gray_image[raw][col]] += 1
        x = np.arange(256).reshape(1,256)
        color_dis = color_dis/(shape[0]*shape[1]) 
        plt.bar(x[0], color_dis[0], color='black')
        plt.show()
        
    def draw_rgb_histogram(self):
        """
        @Brief: draw rgb histogram
        """
        gray_image = np.array(self.image)
        color_dis = np.zeros((3,256))
        shape = gray_image.shape
        for raw in range(shape[0]):
            for col in range(shape[1]):
                color_dis[0][gray_image[raw][col][0]] += 1
                color_dis[1][gray_image[raw][col][1]] += 1
                color_dis[2][gray_image[raw][col][2]] += 1
        x = np.arange(256).reshape(1,256)
        color_dis = color_dis/(shape[0]*shape[1]) 
        plt.bar(x[0], color_dis[0], color='r')
        plt.bar(x[0], color_dis[1], color='g')
        plt.bar(x[0], color_dis[2], color='b')
        plt.show()


if __name__ == '__main__':
    img = Image.open(sys.argv[1])
    rgblist = np.array(img)
    Ph = PictureHistogram(img)
    gray_image = Ph.trans2gray()
    gray_image.show()
    Ph.draw_histogram(color="gray")
    Ph.draw_histogram(color="rgb")
