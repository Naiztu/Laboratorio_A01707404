"""
By José Ángel Rico Mendieta
"""
import numpy as np #libreria numpy

def multi_mat(matriz, kernel):
    """Multiplica las dos matrices"""

    m_row = np.size(matriz, 0)
    m_col = np.size(matriz, 1)

    sum = 0
    for row in range(m_row):
        for col in range(m_col):
            sum += matriz[row, col] * kernel[row,col]
    return sum 

def convolution(img, kernel):
    img_row, img_col = img.shape
    k_row, k_col = kernel.shape

    mat_aux = np.zeros((img_row-2, img_col-2))

    for row in range (mat_aux.shape[0]):
        for col in range (mat_aux.shape[1]):
            mat_aux[row, col] = multi_mat(img[row: row + k_row, col: col + k_col], kernel)
    return mat_aux


