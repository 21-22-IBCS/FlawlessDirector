def main():
    def make_chocolate(small,big,goal):
        how_many_big = int(goal/5)
        if(big >= how_many_big and abs((how_many_big*5)-goal) <= small):
            return abs((how_many_big*5)-goal)
        elif(big < how_many_big and abs((big*5)-goal) <= small):
            return abs((big*5)-goal)
        else:
            return -1


            


if __name__ =="__main__":
    main()
