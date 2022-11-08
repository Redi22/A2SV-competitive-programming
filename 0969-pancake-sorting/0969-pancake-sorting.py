class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        desired_position = n - 1
        flips = []
        sorted_arr = sorted(arr)
        
        while arr != sorted_arr and desired_position > 0:
            index = arr.index(desired_position + 1)
            flips.append(index + 1)
            flips.append(desired_position + 1)
            arr[:index + 1] = arr[:index + 1][::-1]
            arr[:desired_position + 1] = arr[:desired_position + 1][::-1]
            desired_position -= 1
             
        return flips
            