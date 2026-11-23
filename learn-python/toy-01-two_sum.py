class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}  # value -> index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        

if __name__ == "__main__":
    print(Solution().twoSum([2, 7, 11, 15], 9))
