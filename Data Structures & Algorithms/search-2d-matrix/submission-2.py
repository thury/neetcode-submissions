from math import ceil 
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 1:
            for i in matrix[0]:
                if i == target:
                    return True
            return False

        if matrix[ceil(len(matrix)/2)][0] < target:
            return self.searchMatrix(matrix[ceil(len(matrix)/2):], target)
        else:
            if matrix[ceil(len(matrix)/2)][0] > target:
                return self.searchMatrix(matrix[:ceil(len(matrix)/2)], target)
        
        return True
            