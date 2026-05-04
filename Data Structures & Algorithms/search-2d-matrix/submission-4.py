class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1

        while top <= bottom:
            mid_row = (top + bottom) // 2

            if target < matrix[mid_row][0]:
                bottom = mid_row - 1
            elif target > matrix[mid_row][-1]:
                top = mid_row + 1
            else:
                break

        row =  (top + bottom) // 2
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = (l + r) // 2
            if target == matrix[row][mid]:
                return True
            elif target <= matrix[row][mid]:
                r = mid - 1
            elif target >= matrix[row][mid]:
                l = mid + 1
        return False