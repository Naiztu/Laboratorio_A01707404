"""
By José Ángel Rico Mendieta
"""
import numpy as np #libreria numpy
from padding import padd_mat

def multi_mat(matriz, kernel):
    """ Multiplica las dos matrices
    Solo la matriz de mismas dimensiones iguales que el kernel """

    m_row, m_col = matriz.shape 

    sum = 0  
    for row in range(m_row): 
        for col in range(m_col): 
            sum += matriz[row, col] * kernel[row,col] 
    return sum 

def convolution(img, kernel):
    """ Convolución de la matriz imagen con su respectivo kernel 
        agregando el padding"""
    m_row, m_col = img.shape
    k_row, k_col = kernel.shape

    mat_aux = np.zeros(img.shape)

    padded = padd_mat(img,kernel)

    for i in range(m_row):
        for j in range(m_col):
            mat_aux[i, j] = multi_mat(padded[i:i + k_row, j:j + k_col],kernel)
    return mat_aux

def main():
    #Ejemplo
    mat = np.array(([1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [0, 0, 1, 16, 17, 18], [0, 1, 0, 7, 23, 24], [1, 7, 6, 5, 4, 3]))
    ker = np.array(([1, 1, 1], [0, 0, 0], [2, 10, 3]))
    print(convolution(mat,ker))
main()

