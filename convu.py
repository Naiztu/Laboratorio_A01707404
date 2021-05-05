"""
By José Ángel Rico Mendieta
"""
import numpy as np #libreria numpy

def multi_mat(matriz, kernel):
    """ Multiplica las dos matrices
    Solo la matriz de mismas dimensiones iguales que el kernel """
  
    # Dimensiones de la matriz (filas, columnas)
    m_row, m_col = matriz.shape 

    # Acumulador 
    sum = 0  
    # Iterador de filas
    for row in range(m_row): 

        # Iterador de columnas
        for col in range(m_col): 

            # producto punto de cada elemento de la matriz con la del kernel
            sum += matriz[row, col] * kernel[row,col] 

    # return acumulador
    return sum 

def convolution(img, kernel):
    """ Convolución de la matriz imagen con su respectivo kernel """
    # Dimensiones de la matriz imagen y kernel (filas, columnas)
    img_row, img_col = img.shape 
    k_row, k_col = kernel.shape 

    # Inicialización de matriz resultado con las dimensiones correspondientes 
    mat_aux = np.zeros((img_row-2, img_col-2))

    # Iterador de filas
    for row in range (mat_aux.shape[0]):

        # Iterador de columnas
        for col in range (mat_aux.shape[1]):

            # Cálculo de los elementos de la matriz resultado
            mat_aux[row, col] = multi_mat(img[row: row + k_row, col: col + k_col], kernel)
    
    # return resultado
    return mat_aux

def main():
    #Caso de prueba propuesto en la actividad de convolución a mano
    mat = np.array(([1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [0, 0, 1, 16, 17, 18], [0, 1, 0, 7, 23, 24], [1, 7, 6, 5, 4, 3]))
    ker = np.array(([1, 1, 1], [0, 0, 0], [2, 10, 3]))
    print(convolution(mat,ker))
main()

