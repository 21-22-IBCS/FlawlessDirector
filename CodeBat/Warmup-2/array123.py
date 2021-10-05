def main():
    def array123(nums):
        for i in range(0, len(nums)-2):
            if(nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3):
                return True
        return False


if __name__ == "__main__":
    main()
