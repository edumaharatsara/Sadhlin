def  Get_Int(msg,r1,r2):
    while True:
        try:
            data=int(input(msg))
            if data>=r1 and data<=r2:
                break
            else:
                print("Range ",r1, "  - ",r2)
        except:
            print("Havaset Kojast")
    return data

def  Get_Float(msg,r1,r2):
    while True:
        try:
            data=float(input(msg))
            if data>=r1 and data<=r2:
                break
            else:
                print("Range ",r1, "  - ",r2)
        except:
            print("Havaset Kojast")
    return data


def Get_Name(msg):
    while True:
        s=input(msg)
        if s=="":
            return s
        if not(s[0]>="A" and s[0]<="Z"):
            print("First Char A-Z !")
            continue

        if s.count("  ")>=1:
            print("Space Error")
            continue

        if len(s)<3 or len(s)>30:
            print("Len Error 3-30 !")        
            continue

        karam=True ; ch=""
        for i in s :
            if not(i==" " or i>="a" and i<="z"  or i>="A" and i<="Z"):
                karam=False
                ch=i
        if karam==False:
            print("invalid Char ",ch)
            continue
        return s
            
def Set_Float(n,r1,r2):
    try:
        n=float(n)
        if n>=r1 and n<=r2:
            return n
        else:
            return -1
    except:
        return -1

def Set_Int(n,r1,r2):
    try:
        n=int(n)
        if n>=r1 and n<=r2:
            return n
        else:
            return -1
    except:
        return -1




