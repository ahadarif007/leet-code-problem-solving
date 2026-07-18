class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #  declaring an empty map 
        prevMap = {}

        # Iterate through the array with both index and value
        for i,n in enumerate(nums):
            # Calculate the number needed to reach the target sum
            diff = target - n 
            # If the complement was already seen, return its index and current index
            if diff in prevMap:
                return [prevMap[diff] , i]
            # Store the current number with its index for future lookups
            prevMap[n] = i


        