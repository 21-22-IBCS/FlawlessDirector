def main():
    def front_times(yep,n):
        final = ""
        if(len(yep) < 3):
            for i in range(0,n):
                final += yep

            return final
        else:
            arr = list(yep)
            newString = arr[0] + arr[1] + arr[2]
            final = ""
            for i in  range(0,n):
                final += newString

            return final


if __name__ == "__main__":
    main()
