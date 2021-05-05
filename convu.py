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
def main():
    mat = np.array(([11, 12, 13], [21, 22, 23], [31, 32, 33]))
    ker = np.array(([1, 0, 1], [1, 1, 1], [0, 1, 0]))
    print(multi_mat(mat,ker))
main()

