def main():
    def squirrel_play(temp,is_summer):
        if(is_summer != True and 60 <= temp <= 90):
            return True
        elif(is_summer and 60 <= temp <= 100):
            return True
        else:
            return False

if __name__ == "__main__":
    main()
