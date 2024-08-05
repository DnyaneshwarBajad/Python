r = int(input("Enter the number of rows:"))
for i in range (1,r):
	for j in range(1,2*r):
		if i+j==r+1 or j-i==r-1:
			print("*",end='')
		else:
			print(" ",end='')
	print()

for i in range (1,r):
	for j in range(1,2*r):
		if i==j or i+j==2*r:
			print('*',end='')
			
		elif i==1 and j==r :
			print(r,end='')
		else:
			print(" ",end='')
		
	print()
for i in range(r):
  for j in range(r):
    print('*',end=' ')
  print()
