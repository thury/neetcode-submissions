class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(numbers)-1
        while target != numbers[p1] + numbers[p2]:
            actSum = numbers[p1] + numbers[p2]
            if actSum > target:
                p2 = p2 - 1
            else:
                p1 = p1 + 1

        return [p1+1, p2+1]