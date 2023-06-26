# rotate image this is bascially for matrix so it can resemble image coordinates

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                 matrix[i][j] , matrix[j][i]= matrix[j][i] , matrix[i][j]  