#Write a Python program to calculate the sum of numbers between a starting and
#ending point provided by the user.

start_point=int(input("Enter the number "))
end_point=int(input("Enter the number "))

total=0
num=1
for i in range(start_point,end_point): 
    num=num+1
    total=total+num
print("Total=",total)

total=0
num=1
while start_point <=num<= end_point:
    total=total+num
    num=num+1
print("Total=",total)