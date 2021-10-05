def main():
    def front_back(yep):
        if(len(yep) <= 1):
            return yep
        ok = list(yep)
        ok[0],ok[len(ok)-1] = ok[len(ok)-1], ok[0]
        final  = ""
        return (final.join(ok))



if __name__ == "__main__":
    main()
