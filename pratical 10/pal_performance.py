import time

def normal_method_palindrome(l):
 	i=0
 	j=len(l)-1
 	while(i<j):
 		if l[i]!=l[j]:
 			return False
 		i+=1
 		j-=1
 	return True
 	
def Normal_method_palindrome(l):
	ans=0
	temp=l
	while l>0:
		rem=l%10
		ans=ans*10+rem 
		l//=10
	if temp==ans:
		return True
	return False

def give_counter(l):
	counter=0
	while l>0:
		l//=10
		counter+=1
	return counter
	
def palindrome_counter(l):
	counter=0
	for i in l:
		if type(i)==int:
			if ((give_counter(i)%5)==3):
				counter+=Normal_method_palindrome(i)
		elif type(i)==str:
			if len(i)%5==3:
				counter+=normal_method_palindrome
		elif type(i) in [list,set,tuple]:
			counter+=palindrome_counter(i)
		else:
			pass
	return counter	
	
	

def optimized_counter(l):
	counter=0
	for i in l:
		if type(i)==str:
			if len(i)%5==3:
				if i==i[::-1]:
					counter+=1
		elif type(i)==int:
			x=str(i)
			if len(x)%5==3:
				if (x==x[::-1]):
					counter+=1
		elif type(i) in [set,list,tuple]:
			counter+=optimized_counter(i)
		else:
			pass
	return counter

def is_pali(l):
	count=0
	for i in l:
		if isinstance(i,(set,list,tuple)):
			count+=is_pali(i)
		elif type(i)==int:
			i=str(i)
		count+=type(i)==str and len(i)%5==3 and i==i[::-1]
	return count


def  check_performance(approaches):
	time_taken=[]
	l=[111,222,23,'sggs']
	for approach in approaches:
		temp_time=[]
		for _ in range(100):
			start_time=time.time()
			approach(l)
			end_time=time.time()
			temp_time.append(end_time-start_time)
		time_taken.append(sum(temp_time)/100)
	return  list(zip(approaches,time_taken))
	
print(check_performance([palindrome_counter,optimized_counter,is_pali]))
			
			
		
						
							
