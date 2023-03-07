"""
Python 3
Kelompok 3
Aljabar Matrix Linear
"""
import sys

class EliminasiGauss:
    def __init__(self, Matrix_Size) -> None:
        self.matrix         : list  = []
        self.Matrix_Size    : int   = Matrix_Size
        self.createMatrix(self.Matrix_Size)
    
    def upRows(self, div : list = None) -> None:
        self.matrix.append(div)

    def createMatrix(self, matrix_size : int) -> None:
        print(f"Matriks Anda berukuran {matrix_size}x{matrix_size + 1}")
        for  _ in range(matrix_size):
            Row = [int(x) for x in input().split()]
            self.upRows(Row)

    def zeroLeft(self, columnDiv : int) -> None:
        headRow = self.matrix[columnDiv]
        for row in range(columnDiv + 1, self.Matrix_Size):
            toZeroConstant = self.division(self.matrix[row][columnDiv] , headRow[columnDiv])
            newRow = self.roundRow([self.matrix[row][x] - headRow[x] * toZeroConstant for x in range(self.Matrix_Size+1)])
            self.matrix[row] = newRow

    def zeroRight(self, columnDiv : int) -> None:
        columnDiv = self.Matrix_Size - columnDiv - 1
        headRow = self.matrix[columnDiv]
        for row in range(columnDiv - 1, -1, -1):
            toZeroConstant = self.division(self.matrix[row][columnDiv] , headRow[columnDiv])
            newRow = self.roundRow([self.matrix[row][x] - headRow[x] * toZeroConstant for x in range(self.Matrix_Size+1)])
            self.matrix[row] = newRow

    def division(self, x1, x2, precision : float = 0.00001):
        result = x1 / x2
        if 0.0000000001 > result % 1 > -0.0000000001:
            result = int(result)
            return result
        else:
            return x1 / x2

    def roundRow(self, Row) -> list:
        tempRow = []
        for col in Row:
            if 0.0000000001 > col % 1 > -0.0000000001:
                tempRow.append(int(col))
            else:
                tempRow.append(round(col, 3))
        return tempRow
    
    def rowEsselon(self) -> None:
        for esselon in range(self.Matrix_Size):
            self.matrix[esselon][self.Matrix_Size] = self.division(self.matrix[esselon][self.Matrix_Size] , self.matrix[esselon][esselon])
            self.matrix[esselon][esselon] = 1

    def solve(self) -> None:
        for row in range(self.Matrix_Size):
            self.zeroLeft(row)
        for row in range(self.Matrix_Size):
            self.zeroRight(row)
        self.rowEsselon()
        

    def display(self) -> None:
        for row in self.matrix:
            for div in row:
                print(div, end="\t")
            print(" ")
    
    def printAnswer(self, digit : int = 2):
        list_Answer = []
        for row in range(self.Matrix_Size):
            list_Answer.append(round(self.matrix[row][-1], digit))
        print('Solusi dari permasalahan adalah')
        for x in range(len(list_Answer)):
            print(f'    x{x} = {list_Answer[x]}')


if __name__ == "__main__":
    print("Operasi Eliminasi Gauss-Jordan -- Kelompok 3 AVM")
    try:
        matrix = EliminasiGauss(int(input("Banyak Baris Matrix Anda : ")))
        matrix.solve()
    except Exception as e:
        print("\nTerjadi Error :")
        print(e)
    else:
        print("HASIL GAUSS-JORDAN ELIMINATION")
        matrix.display()
        print()
        matrix.printAnswer()
    finally:
        print()
        print("Program Telah Selesai")
        sys.exit(0)
    
