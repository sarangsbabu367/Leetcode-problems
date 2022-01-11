class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        pascal_rows = [[1]]
        
        for index in range(1, rowIndex+1):
            pascal_row = [0]*(index + 1)
            pascal_row[0] = pascal_row[-1] = 1
                
            for row_index in range(1, index):
                pascal_row[row_index] = (
                    pascal_rows[index-1][row_index-1]
                    + pascal_rows[index-1][row_index]
                )
            pascal_rows.append(pascal_row)
        return pascal_rows[-1]