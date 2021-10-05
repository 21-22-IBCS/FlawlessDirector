def main():
    def missing_char(yep, n):
        part = yep.partition(yep[n])
        new = part[0] + part[2]
        return new
        


if __name__ == "__main__":
    main()
