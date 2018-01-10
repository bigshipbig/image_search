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

    def draw_histogram(self, color="gray", range_size=1):
        """
        @Brief: draw histogram
        """
        if color == "gray":
            self.draw_gray_histogram(range_size)
        elif color == "rgb":
            self.draw_rgb_histogram(range_size)

    def draw_gray_histogram(self, range_size):
        """
        @Brief: draw gray histogram
        """
        range_num = int(256/range_size) if 256 % range_size == 0 else int(256/range_size) + 1
        gray_image = np.array(self.trans2gray())
        color_dis = np.zeros((1,range_num))
        shape = gray_image.shape
        for raw in range(shape[0]):
            for col in range(shape[1]):
                range_id = int(gray_image[raw][col]/range_size)
                color_dis[0][range_id] += 1
        x = np.arange(range_num).reshape(1,range_num)
        color_dis = color_dis/(shape[0]*shape[1]) 
        plt.bar(x[0], color_dis[0], color='black')
        plt.show()
        
    def draw_rgb_histogram(self, range_size):
        """
        @Brief: draw rgb histogram
        """
        range_num = int(256/range_size) if 256 % range_size == 0 else int(256/range_size) + 1
        rgb_image = np.array(self.image)
        color_dis = np.zeros((3,range_num))
        shape = rgb_image.shape
        for raw in range(shape[0]):
            for col in range(shape[1]):
                range_id1 = int(rgb_image[raw][col][0]/range_size)
                range_id2 = int(rgb_image[raw][col][1]/range_size)
                range_id3 = int(rgb_image[raw][col][2]/range_size)
                color_dis[0][range_id1] += 1
                color_dis[1][range_id2] += 1
                color_dis[2][range_id3] += 1
        x = np.arange(range_num).reshape(1,range_num)
        color_dis = color_dis/(shape[0]*shape[1])
        plt.bar(x[0], color_dis[0], color='r')
        plt.bar(x[0], color_dis[1], color='g')
        plt.bar(x[0], color_dis[2], color='b')
        plt.show()
    
    def calc_cdf(self, color_type='gray', range_size=1):
        """
        Brief: calculate cumulative distribution function
        """
        range_num = int(256/range_size) if 256 % range_size == 0 else int(256/range_size) + 1
        if color_type == 'gray':
            gray_img = np.array(self.trans2gray())
            x,y = gray_img.shape
            sum_grid = x * y
            count_num = np.array([0] * range_num)
            for raw in range(x):
                for col in range(y):
                    count_num[int(gray_img[raw][col]/range_size)] += 1
            res = []
            tmp = 0
            for item in count_num:
                tmp += item
                res.append(tmp*1.0/sum_grid)
            return np.array(res)
        elif color_type == 'rgb':
            rgb_img = np.array(self.image)
            x,y,z = rgb_img.shape
            sum_grid = x * y
            color_dis = np.zeros((3,range_num))
            for raw in range(x):
                for col in range(y):
                    range_id1 = int(rgb_img[raw][col][0]/range_size)
                    range_id2 = int(rgb_img[raw][col][1]/range_size)
                    range_id3 = int(rgb_img[raw][col][2]/range_size)
                    color_dis[0][range_id1] += 1
                    color_dis[1][range_id2] += 1
                    color_dis[2][range_id3] += 1
            res = []
            for i in range(3):
                tmp = 0
                tmp_res = []
                for item in color_dis[i]:
                    tmp += item
                    tmp_res.append(tmp * 1.0 / sum_grid)
                res.append(tmp_res)
            return np.array(res)
























