# Armstrong Number Program
num = int(input("Enter a number: "))
sum = 0
temp = num
# count number of digits
digits = len(str(num))
while temp > 0:
    digit = temp % 10
    sum += digit ** digits
    temp //= 10
if sum == num:
    print("It is an Armstrong number")
else:
    print("It is not an Armstrong number")