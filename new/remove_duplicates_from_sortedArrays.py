class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        size = len(nums)
        insertIndex = 1
        """
        number 0 is already unique
        from slot 1 to the whole size
        if nums i is not the same as -i make the insertIndex one more
        return
        """
        for i in range(1, size):
            if nums[i - 1] != nums[i]:
                nums[insertIndex] = nums [i]
                insertIndex = insertIndex + 1
        return insertIndex
