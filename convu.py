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


