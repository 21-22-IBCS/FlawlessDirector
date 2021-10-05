def main():
    def left2(yep):
        arr = list(yep)
        arr.append(arr.pop(0))
        arr.append(arr.pop(0))
        final = ""
        return final.join(arr)

        

if __name__=="__main__":
    main()
