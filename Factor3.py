import subprocess
subprocess.call("cls",shell=True)
factor="=============================================\n"
status=0 ;   jam1=0; jam2=0; jam3=0
while True:
    goods=input("Enter Goods : ")
    if goods=="":
        break
    status+=1
    price=float(input("Enter Price $ : "))
    order=int(input("Enter order # : "))
    off=float(input("Enter Off % : "))
    gheimat1=price * order         ;jam1+=gheimat1
    gheimat2 = gheimat1 * off  /100  ;jam2+=gheimat2
    gheimat3 = gheimat1 - gheimat2     ;jam3+=gheimat3
    factor+="{0:20s}{1:12.2f}{2:10d}{3:12.2f}{4:12.2f}{5:12.2f}".format(
        goods,price,order,gheimat1,gheimat2,gheimat3)+"\n"
factor+="=============================================\n"
if status!=0:
    mobile=int(input("Enter Mobile  :"))
    factor=str(mobile)+"\n"+factor+"\n"
    factor+="=============================================\n"
    factor+="{0:12.1f}$  -   {1:12.1f}      =  Pay:{2:12.1f}$ ".format(
        jam1,jam2,jam3)
    print(factor)