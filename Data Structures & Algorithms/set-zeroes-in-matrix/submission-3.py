class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        
        def set_rows(r,c):
            nonlocal rows
            for i in range(rows):
                if matrix[i][c] != 0 :
                    matrix[i][c] = True
        
        def set_cols(r,c):
            nonlocal cols
            for j in range(cols):
                if matrix[r][j] != 0 :
                    matrix[r][j] = True
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0 :
                    set_rows(i,j)
                    set_cols(i,j)
                    matrix[i][j] = True
                    # print(matrix)
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == True and type(matrix[i][j]) == bool :
                    matrix[i][j] = 0
