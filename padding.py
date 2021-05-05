"""
By José Ángel Rico Mendieta
"""
import numpy as np #libreria numpy

def padd_mat(matriz):
    """Agrega padding"""

    m_row = np.size(matriz, 0)
    m_col = np.size(matriz, 1)

    img = np.zeros((m_row+2,m_col+2))
    for row in range(m_row):
        for col in range(m_col):
            img[row+1, col+1] = matriz[row, col]
    return img
