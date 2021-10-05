def main():
    
    
    def make_bricks(small,big,goal):
        min_big_needed = int(goal/5)
        if((big >= min_big_needed and (min_big_needed*5)+small >= goal)):
            return True
        elif(big < min_big_needed and (big*5)+small >= goal):
            return True
        else:
            return False
            
        
            



if __name__=="__main__":
    main()
