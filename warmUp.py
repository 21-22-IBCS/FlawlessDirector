import math

def convert(rad):
    return (rad*180)/math.pi
    

def checkIE(x):
    x = x.lower()
    for i in range(0,len(x)-1):
        if(x[i] == "i" and i == 0 and x[i+1] == "e"):
            return True
        elif(x[i] == "i" and x[i+1] == "e" and x[i-1] != "c"):
            return True
        elif(x[i] == "e" and i != 0 and x[i-1] == "c" and x[i+1] == "i"):
            return True

    if(x.count("i") == 0 and x.count("e") == 0):
        return True

    return False
            
def coupon(x):
    if (x >= 100):
        return x - (x * 0.15)
    

def main():
    print(checkIE("nope"))


if __name__ == "__main__":
    main()
