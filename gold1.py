import subprocess
subprocess.call("cls",shell=True)
from module import *
data="=======================================================================\n"
sabad=0
s1=0; s2=0; s3=0
while True:
    # tala=input("Enter Tala : ")
    tala=Get_Name("Enter Tala :")
    if tala=="":
        break
    vazn=Get_Float("Vazn:",0.05,1000)
    price=Get_Float("Price:",5000,30000)
    karmoz=Get_Float("Karmozd:",0,20)
    tax=Get_Float("Tax:",0,100)
    sabad+=1
    h1=price * vazn       ;s1+=h1    #  10,000
    h2=h1 * karmoz / 100  ;s2+=h2    #  200
    h3=h1 * tax /  100    ;s3+=h3    #  400
    sum=s1 + s2  +s3 

    data+="{0:3d}-{1:20s}{2:12.1f}{3:12.1f}{4:12.1f}{5:12.1f}{6:12.1f}".format(sabad,tala,vazn,price,h1,h2,h3)+"\n"

data+="=======================================================================\n"
if sabad!=0:
    customer=Get_Name("Customer Name : ")
    mobile=Get_Int("Mobile :",9000000000,9999999999)
    data="\t\t\t{0:20s}{1:15d}".format(customer,mobile)+"\n"+data
    data+="Sum:{0:12.1f}  Karmozd:{1:12.1f}   Tax:{2:12.1f}".format(s1,s2,s3)+"\n"
    data+=str(sum)
    print(data)



