#loops: for and while
#for loop works on iteration.I have to command it to loop
#  something and also provide how many number of times to loop

# range function: range(start,stop,step)
#for loop with numbers 
# range(10,101,1)
# for i in range(5,51,5):
#     print(i)
# a=int(input("num:"))
# for i in range(a,a*10+1,a):
#     print(i)
#for loop with string 
# b="Baka"
# for i in b:
#      print(i)
# for i in range(0,len(b),1):
#     print(i)
# #prints the number of characters 
# for i in range(0,len(b),2):
#     print(b[i])
# #prints the characters
# for i in range(0,len(b),1):
#     print(f"{i}:{b[i]}")
# # you can also do this

# conditions for looping : break ,continue and else
#1st break: breaks the loop on a specified iteration if identified 
# for i in range(1,11):
#     if i==7:
#         break
#     print(i)
#prints 1-6 numbers 
#2 nd continue: skips the specified iteration 
# for i in range(3,9,1):
#     if i==6 :
#         continue
#     print(i)
# #skips 6 and print 3 to 9
# #3rd else: not the else used with if. It is used with break to execute a
# #command if break doesnt work 
# for i in range(3,9,1):
#     if i==10 :#not in the range so break will not work
#         break
#     print(i)
# else :#for and else statement should be in same line
#     print("no break")

#Questions: 1
# a=int(input("num:"))
# b="Hello World"
# for i in range(0,a,1):
#     print(b)
#2
# a=int(input("num:"))
# for i in range(1,a+1):
#     print(i)
#3
# a=int(input("num:"))
# for i in range(a,0,-1):
#     print(i)
#4
# a=int(input("num:"))
# for q in range(1,11,1):
#     print(f"{a}x{q}={a*q}")
#5
# a=int(input("num:"))
# print(a*(a+1)/2)
# a=int(input("num:"))
# s=0
# for i in range(1,a+1):
#     s=s+i
# print(s)
#6
# a=int(input("num:"))
# m=1
# for i in range(1,a+1):
#     m=m*i
# print(m)
#7
# a=int(input("starting num:"))
# b=int(input("ending num:"))
# s1=0
# s2=0
# if a%2==0 :
#     for i in range(a,b+1,2):
#         s1=s1+i
#     print(f"even sum={s1}")
# else :
#     for i in range(a,b+1,2):
#         s1=s1+i
#     print(f"odd sum={s1}")
# #above is my method. below iwill do sir method 
# a=int(input("starting num:"))
# b=int(input("ending num:"))
# s1=0
# s2=0
# for i in range(a,b+1):
#     if i%2==0 :
#         s1=s1+i
#     else:
#         s2=s2+i
# print(f"even sum={s1}",f"odd sum={s2}")
#8
# a=int(input("num:"))
# for i in range(1,a+1):
#     if a%i==0 :
#         print(i)
#9
# a=int(input("num:"))
# s=0
# for i in range(1,a):
#     if a%i==0 :
#      s=s+i
# if s==a:
#    print("perfect number ")
# else: print("not perfect number ")
#10
# a=int(input("num:"))
# b=0
# for i in range(1,a):
#     if a%i==0:
#      b=b+i
# if b==1:
#     print("prime number ")
# else :print("composite number ")
#11
# a=input("word:") 
# rev=""
# for i in range(len(a)-1,-1,-1):
#     rev=rev+a[i]
# print(rev)
#12 palindrome = reverse of a word is the same word 
# a=input("word:") 
# rev=""
# for i in range(len(a)-1,-1,-1):
#       rev=rev+a[i]
# if rev==a:
#       print("palindrome ")
# else:print("not palindrome ")
#13
# a=input("word:")
# print(ord("9"))
# l=0
# n=0
# s=0
# for i in a:
#     if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122):
#         l=l+1
#     elif (ord(i))>=48 and ord(i)<=57:
#         n=n+1
#     else: print(f"num of special characters:{len(i)}")
# print(f"num of letters:{l}")
# print(f"num of digits:{n}")

#while loop : works infinitely until the condition is true
#works on a condition ie we have to use if,else statement 
# while True:
#     print("hello")
# print from 1 to 20
# a=0
# while a!=20:
#     a+=1
#     print(a)

#1
# a=int(input("num:"))
# while a>0 :
#      print(a%10)
#      a=a//10

#2
# rev=0
# a=int(input("num:"))
# while a>0 :
#     rev=rev*10+a%10
#     a=a//10
    
# print(rev)

#3
a=int(input("num:"))
b=a#we made a copy of "a" bcz we are operating on "a" and making it 0 to stop the while loop
#so during if statement 0 will be taken inplace of "a"
rev=0
while a>0 :
     rev=rev*10+a%10
     a=a//10
if b==rev:
 print("palindrome")
else: print("not palindrome")
      
      




        












