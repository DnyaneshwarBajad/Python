import random
def guess_the_number():
	x=random.randint(1,20)
	chances=5
	while chances>0:
		y=int(input("enter your guess: "))
		if y==x:
			print("Correct!")
			return True
		elif y>x:
			print("too large, enter smaller no")
			chances-=1
		else:
			print("too small, enter larger no")
			chances-=1
	else:
		print("Oops! chances are finished")
	return False

guess_the_number()