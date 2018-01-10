import sys
from PIL import Image
import PictureHistogram as pichis
"""
Brief: UnitTest PictureHistogram
"""

if __name__ == '__main__':
    img = Image.open(sys.argv[1])
    Ph = pichis.PictureHistogram(img)
    gray_image = Ph.trans2gray()
    gray_image.show()
    Ph.draw_histogram(color="gray")
    Ph.draw_histogram(color="gray", range_size=50)
    Ph.draw_histogram(color="rgb", range_size=20)
