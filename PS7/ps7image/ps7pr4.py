#
# ps7pr4.py  (Problem Set 7, Problem 4)
#
# Images as 2-D lists  
#
# Computer Science 111
# 

from hmcpng import *

def create_uniform_image(height, width, pixel):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels have the RGB values
        given by pixel
        inputs: height and width are non-negative integers
                pixel is a 1-D list of RBG values of the form [R,G,B],
                     where each element is an integer between 0 and 255.
    """
    pixels = []

    for r in range(height):
        row = [pixel] * width
        pixels += [row]

    return pixels

def blank_image(height, width):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels are green.
        inputs: height and width are non-negative integers
    """
    all_green = create_uniform_image(height, width, [0, 255, 0])
    return all_green

def brightness(pixel):
    """ takes a pixel (an [R, G, B] list) and returns a value
        between 0 and 255 that represents the brightness of that pixel.
    """
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    return (21*red + 72*green + 7*blue) // 100

## put your functions below
def grayscale(pixels):
    """ creates and returns a new 2-D list of pixels for an image that is a 
    grayscale version of the original image.
    inputs: the 2-D list pixels
    """
    gray_one=blank_image(len(pixels),len(pixels[0]))
    for h in range(len(pixels)):
        for w in range(len(pixels[0])):
            b=brightness(pixels[h][w])
            gray_one[h][w]=[b,b,b]
    return gray_one

def mirror_vert(pixels):
    """creates and returns a new 2-D list pixels for one image in which the
    original one is mirrored vertically.
    inputs: the 2-D list pixels
    """ 
    m=len(pixels)
    n=len(pixels[0])
    mirror_one=blank_image(m,n)
    x=m//2
    if m%2!=0:
        for w in range(n):
            mirror_one[x][w]=pixels[x][w]
    for h in range(x):
        for w in range(n):
                mirror_one[h][w]=pixels[h][w]
                mirror_one[m-h-1][w]=pixels[h][w]
    return mirror_one

def flip_horiz(pixels):
    """creates and returns a new 2-D list of pixels for an image in which the
    original is flipped horizontally.
    inputs: the 2-D list pixels
    """
    flip_one=blank_image(len(pixels),len(pixels[0]))
    x=len(pixels[0])
    for h in range(len(pixels)):
        for w in range(len(pixels[0])):
            flip_one[h][w]=pixels[h][x-w-1]
    return flip_one

def reduce(pixels):
    """creates and returns a new 2-D list that represents an image that is
    half the size of the original image.
    inputs: the 2-D list pixels
    """
    m=len(pixels)//2
    n=len(pixels[0])//2
    new_reduce=blank_image(m,n)
    for r in range(m):
        for c in range(n):
            new_reduce[r][c]=pixels[2*r+1][2*c+1]
    return new_reduce


def transpose(pixels):
    """creates and returns a new 2-D list that change rxc into cxr
    inputs: the 2-D list pixels
    """
    new_transpose=blank_image(len(pixels[0]),len(pixels))
    for h in range(len(pixels)):
        for w in range(len(pixels[0])):
            new_transpose[w][h]=pixels[h][w]
    return new_transpose
