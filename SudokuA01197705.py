def lineIsValid(linea):
    for i in range(9):
        #simplemente revisamos que no existan casillas vacias
        if(linea[i]==0):
            return False
    return True

def sudokuValidator(tablero):
    #checar filas
    #recorremos la matriz con dos ciclos, i y j 
    for i in range(9):
        linea = [0,0,0,0,0,0,0,0,0]
        for j in range(9):
            linea[tablero[i][j]-1] = 1
        #validamos que la fila sea valida con la función auxiliar "lineIsValid"
        if not lineIsValid(linea):
            #si la linea no es valida, terminamos de revisar y devolvemos falso
            return False

    #checar columnas (de manera similar a la que checamos filas)
    for j in range(9):
        columna =  [0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0]
        for i in range(9):
            columna[tablero[j][i]-1] = 1
        if not lineIsValid(columna):
            return False

    #checar secciones de 3*3 (esta parte es mucho mas tricky)
    indicesEnJ = [0,0,0,3,3,3,6,6,6]
    indicesEnK = [0,3,6,0,3,6,0,3,6]
    #se usan las matrices de coordenadas para navegar en en el sudoku como si fueran 9 bloques de 3*3
    for startIndex in range(9):
        linea = [0,0,0,0,0,0,0,0,0]
        #con los ciclos j,k se revisan cada uno de los 9 bloques de 3*3 con una tecnica
    
        for j in range(3):
            for k in range(3):
                linea[tablero[j+indicesEnJ[startIndex]][k+indicesEnK[startIndex]]-1] = 1
        if not lineIsValid(linea):
            return False
    return True


sudoku = [[8,2,5,4,7,1,3,9,6],
          [1,9,4,3,2,6,5,7,8],
          [3,7,6,9,8,5,2,4,1],
          [5,1,9,7,4,3,8,6,2],
          [6,3,2,5,9,8,4,1,7],
          [4,8,7,6,1,2,9,3,5],
          [2,6,3,1,5,9,7,8,4],
          [9,4,8,2,6,7,1,5,3],
          [7,5,1,8,3,4,6,2,9]]

sudokuCorrecto = [[8,2,7,1,5,4,3,9,6],
                  [9,6,5,3,2,7,1,4,8],
                  [3,4,1,6,8,9,7,5,2],
                  [5,9,3,4,6,8,2,7,1],
                  [4,7,2,5,1,3,6,8,9],
                  [6,1,8,9,7,2,4,3,5],
                  [7,8,6,2,3,5,9,1,4],
                  [1,5,4,7,9,6,8,2,3],
                  [2,3,9,8,4,1,5,6,7]]

sudokuIncorrecto = [[8,2,2,1,3,4,3,9,1],
                  [9,1,3,3,2,2,1,4,8],
                  [3,4,1,1,8,9,2,3,2],
                  [3,9,3,4,1,8,2,2,1],
                  [4,2,2,3,1,3,1,8,9],
                  [1,1,8,9,2,2,4,3,3],
                  [2,8,1,2,3,3,9,1,4],
                  [1,3,4,2,9,1,8,2,3],
                  [2,3,9,8,4,1,3,1,2]]

sudokuIncorrecto2 = [[1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9]]

sudokuIncorrecto3 = [[1,1,1,1,1,1,1,1,1],
                     [2,2,2,2,2,2,2,2,2],
                     [3,3,3,3,3,3,3,3,3],
                     [4,4,4,4,4,4,4,4,4],
                     [5,5,5,5,5,5,5,5,5],
                     [6,6,6,6,6,6,6,6,6],
                     [7,7,7,7,7,7,7,7,7],
                     [8,8,8,8,8,8,8,8,8],
                     [9,9,9,9,9,9,9,9,9]]

sudokuIncorrecto4 = [[1,2,3,4,5,6,7,8,9],
                     [9,1,2,3,4,5,6,7,8],
                     [8,9,1,2,3,4,5,6,7],
                     [7,8,9,1,2,3,4,5,6],
                     [6,7,8,9,1,2,3,4,5],
                     [5,6,7,8,9,1,2,3,4],
                     [4,5,6,7,8,9,1,2,3],
                     [3,4,5,6,7,8,9,1,2],
                     [2,3,4,5,6,7,8,9,1]]

print(sudokuValidator(sudoku))
print(sudokuValidator(sudokuCorrecto))
print(sudokuValidator(sudokuIncorrecto))
print(sudokuValidator(sudokuIncorrecto2))
print(sudokuValidator(sudokuIncorrecto3))
print(sudokuValidator(sudokuIncorrecto4))




