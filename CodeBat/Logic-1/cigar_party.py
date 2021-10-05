def main():
    def cigar_party(cigars, is_weekend):
        if (is_weekend != True and 40 <= cigars <= 60):
            return True
        elif(is_weekend and cigars >=40):
            return True
        else:
            return False
    
if __name__=="__main__":
    main()
