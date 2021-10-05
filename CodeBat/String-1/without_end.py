def main():
    def without_end(yep):
        ok = list(yep)
        ok.pop(len(ok)-1)
        ok.pop(0)
        final = ""
        return final.join(ok)


if __name__=="__main__":
    main()
