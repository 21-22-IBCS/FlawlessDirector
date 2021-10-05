def main():
    def front3(yep):
        if (len(yep) < 3):
            final = yep + yep + yep
            return final
        else:
            ok = yep[0] + yep[1] + yep[2]
            ok += ok + ok
            return ok
            


if __name__ == "__main__":
    main()
