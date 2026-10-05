# typecasting is converting one data type into another using functions like 
#int(),float(),str(),ord(),hex(),oct(),tuple(),set(),list(),dict()etc
# ye sarey functions hai
#  use kiya tha ye calculator mai to convert string to int
# example 
a="2"
c="4"
print(int(a)+int(c))
# example
string="8"
number=2
x=int(string)
print(x+number)
# ye upar wale ko explicit typecast bolte hai as ham khudse code karke change karey hai data type
#next is implicit type cast jo khud python karta hai as datatype ke order hote hai so lower order se higher order pe chaley jata hai 
m=2.9
# ye float hai 
n=8
# ye int hai
print(m+n)
# result hame 10.9 milega jo float hai so string converted to float automatically
