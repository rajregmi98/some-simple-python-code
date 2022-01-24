def fino(n):
	if(n<=1):
		return n
	else:
		return (fino(n-1) + fino(n-2))

nt = 10
if nt <= 0:
	print("Enter positive number")
else:
	for i in range(nt):
		print(fino(i))

