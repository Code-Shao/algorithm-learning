from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_matrix = len(matrix)
        column_matrix = len(matrix[0])
        num = row_matrix*column_matrix
        left = 0
        right = num - 1
        while left <= right:
            mid = (right + left) // 2
            row = mid // column_matrix
            column = mid % column_matrix
            if matrix[row][column] > target:
                right = mid - 1
            elif matrix[row][column] < target:
                left = left + 1
            else:
                return True
        return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 7

sol = Solution()
print(sol.searchMatrix(matrix, target))
