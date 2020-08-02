"""
Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt


def rotate90_clockwise_ver1(matrix: np.ndarray) -> np.ndarray:
    temp = matrix.copy()
    start = 0
    end = len(matrix) - 1

    for i in range(len(matrix)):
        temp[:, end-i] = matrix[start+i, :]

    return temp


def rotate90_clockwise_ver2(matrix: np.ndarray) -> np.ndarray:
    mat = matrix.copy()
    for i in range(len(mat) // 2):
        for j in range(i, len(mat) - i - 1):
            top = mat[i][j]
            left = mat[len(mat) - 1 - j][i]
            right = mat[j][len(mat) - 1 - i]
            bottom = mat[len(mat) - 1 - i][len(mat) - 1 - j]

            temp = top
            top = left
            left = bottom
            bottom = right
            right = temp

            mat[i][j] = top
            mat[len(mat) - 1 - j][i] = left
            mat[j][len(mat) - 1 - i] = right
            mat[len(mat) - 1 - i][len(mat) - 1 - j] = bottom

    return mat



if __name__ == '__main__':
    fig = plt.figure()
    img = np.array([[1,1,1,1], [2,2,2,2],[3,3,3,3],[4,4,4,4]])
    fig.add_subplot(1, 4, 1)
    plt.imshow(img)
    img2 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    fig.add_subplot(1, 4, 2)
    plt.imshow(img2)
    img3 = rotate90_clockwise_ver1(img)
    fig.add_subplot(1, 4, 3)
    plt.imshow(img3)
    img4 = rotate90_clockwise_ver2(img)
    fig.add_subplot(1, 4, 4)
    plt.imshow(img4)
    plt.show()
