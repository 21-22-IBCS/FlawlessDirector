def main():
    def array_front9(nums):
        for i in range(0, 4):
            try:
                if(nums[i] == 9):
                    return True

            except IndexError:
                return False
                
        return False




if __name__ == "__main__":
    main()
