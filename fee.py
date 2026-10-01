str1=input("What is your name:")
str2=input("Caste:")
str3=int(input("Parents/Guardian Income:"))
a=("SC/ST")
b=("GENERAL")
c=("OBC")
A=(250000)
B=(600000)
C=(800000)
if str2==(a) and str3<=(A):
    print("Full concession")
elif str2==(a) :
    print("half concession")
elif str2==(b) and str3<=(C):
    print("EWS: Quarterly concession")
elif str2==(c) and str3<=(B):
    print("Quaterly concession")
print("Thank you:)")