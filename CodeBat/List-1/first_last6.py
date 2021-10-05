def main():
    def first_last6(nums):
        for i in range(0,len(nums)):
            if(nums[i] == 6 and (i == 0 or i == len(nums)-1)):
                return True

        return False


if __name__ == "__main__":
    main()
