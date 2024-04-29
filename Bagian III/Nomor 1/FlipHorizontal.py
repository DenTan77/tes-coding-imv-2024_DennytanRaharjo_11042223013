import math
import os
import random
import re
import sys

def simple_image_flip(row_len, col_len, image, direction):
    if direction == 'horizontal':
        for i in range (row_len):
            for j in range (col_len//2):
                temp = image[i][j]
                image[i][j] = image[i][col_len-j-1]
                image[i][col_len-j-1] = temp
        return image
    elif direction == 'vertical':
        for j in range (col_len):
            for i in range (row_len//2):
                temp = image[i][j]
                image[i][j] = image[row_len-i-1][j]
                image[row_len-i-1][j] = temp
        return image
    elif direction == 'transpose':
        for i in range(col_len):
            for j in range(row_len):
        return image
    else
        return image

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    row_len = int(first_multiple_input[0])

    col_len = int(first_multiple_input[1])

    direction = input()

    image = []

    for _ in range(row_len):
        image.append(list(map(int, input().rstrip().split())))

    result = simple_image_flip(row_len, col_len, image, direction)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
