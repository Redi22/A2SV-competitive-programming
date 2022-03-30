class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lessThan = []
        greaterThan = []
        equalCount = 0
        for num in nums:
            if num > pivot:
                greaterThan.append(num)
            elif num < pivot:
                lessThan.append(num)
            else:
                equalCount += 1
        return lessThan + [pivot] * equalCount + greaterThan