class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top_row = 0
        bottom_row = len(matrix) - 1
        target_row = -1
        while top_row <= bottom_row:
            mid = (top_row + bottom_row) // 2
            if target < matrix[mid][0]:
                bottom_row = mid - 1
            elif target > matrix[mid][len(matrix[0]) - 1]:
                top_row = mid + 1
            else:
                target_row = mid
                break
        
        if target_row == -1:
            return False
        
        left = 0
        right = len(matrix[0]) - 1
        while left <= right:
            mid = (left + right) // 2
            if target > matrix[target_row][mid]:
                left = mid + 1
            elif target < matrix[target_row][mid]:
                right = mid - 1
            elif target == matrix[target_row][mid]:
                return True
        
        return False

        




        

