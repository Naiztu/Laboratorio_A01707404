"""
By José Ángel Rico Mendieta
"""
import numpy as np #libreria numpy

def padd_mat(matriz, kernel):
    """Agrega padding"""
    m_row, m_col = matrix.shape
    k_row, k_col = kernel.shape

    padd_height = int((k_row - 1) / 2)
    padd_width = int((k_col - 1) / 2)

    padded= np.zeros((m_row + (2 * padd_height), m_col + (2 * padd_width)))

    padded[padd_height:padded.shape[0] - padd_height, padd_width:padded.shape[1] - padd_width] = matriz

    return padded