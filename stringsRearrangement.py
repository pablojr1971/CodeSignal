def stringsRearrangement(inputArray):
    nl=sorted(inputArray)
    r=len(nl[0])
    print(nl)
    for x in range(len(nl)-1):
        print(x)
        count=0
        for p in range(r):
            if nl[x][p]!=nl[x+1][p]:
                count+=1
        if count!=1:
            return False

    return True


print(stringsRearrangement(["ff",
                            "gf",
                            "af",
                            "ar",
                            "hf"]))

                            #If you're stuck, make sure ["abc","bac","bbc","bbe","bbd"] returns false.
