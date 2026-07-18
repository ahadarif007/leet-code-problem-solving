class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Store each number and its index while iterating through the array.
        # The dictionary allows O(1) lookup to check if the required complement exists.
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


        