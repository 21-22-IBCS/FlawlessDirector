def main():
    def non_start(a,b):
        final = ""
        new = ["",""]
        ok = [list(a),list(b)]
        for i in range(0,2):
            if(i==0):
                for j in range(0,2):
                    ok[j].pop(0)
                    continue
            

            new[i] = new[i].join(ok[i])
            final += new[i]

        
        return final



    


if __name__=="__main__":
    main()
