def main():
    def max_end3(nums):
        large = 0
        if(nums[0] > nums[len(nums)-1]):
            large = nums[0]
        else:
            large = nums[len(nums)-1]
        for i in range(0, len(nums)):
            nums[i] = large
        return nums

if __name__ == "__main__":
    main()
