class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Solution 1: Brute Force
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]== target:
        #             return[i,j]
        #
        # solution = Solution()
        #
        # result = solution.twoSum([5,7,7,8,9], 14)
        # print(result)
        #         Solution 2: Two-pass Hash Table
        num_hashtable = {}  # Create a hash table
        n = len(nums)
        for i in range(n):
            num_hashtable[nums[i]] = i  # Add number in list and its indies into dict
            complement = target - nums[i]
            if complement in num_hashtable and num_hashtable[complement] != i:
                return [i, num_hashtable[complement]]


solution = Solution()
result = solution.twoSum([2, 7, 9, 16], 16)
print(result)
