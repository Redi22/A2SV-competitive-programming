class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        for i in range(len(arr)):
            diff = abs(x-arr[i])
            arr[i] = f'{diff}_{arr[i]}'
        arr.sort(key=lambda x:int(x.split('_')[0]))   # sort by diff
        arr = [int(x.split('_')[1]) for x in arr[:k]] # get first k nums and sort again 
        arr.sort()
        return arr