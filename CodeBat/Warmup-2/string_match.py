def main():

    def string_match(a,b):
        count = 0
        for i in range (0, len(a)-1):
            subA = a[i] + a[i+1]
            for j in range(0, len(b)-1):
                subB = b[j] + b[j+1]
                if(subA == subB and i == j):
                    count += 1

        return count


if __name__ == "__main__":
    main()
