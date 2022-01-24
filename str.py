num = 123456
reverse = 0
while num !=0:
    digit = num % 10 
    reverse = reverse * 10 + digit 
    num //= 10 

print("Reversed number:" +str(reverse))

