import time
def a1(l):
	even_count=0
	odd_count=0
	for i in l:
		if i%2==0:
			even_count+=1
		else:
			odd_count+=1
	return even_count,odd_count
	
def a2(l):
	even_count=0
	
	for i in l:
		even_count+=i%2==0 
		
	return even_count,len(l)-even_count
	
def a3(l):
	even_count=0
	
	for i in l:
		even_count+=i&1==0
		
	return even_count,len(l)-even_count

def a4(numbers):
    even_count = sum(1 for num in numbers if num % 2 == 0)
    odd_count = len(numbers) - even_count  
    return odd_count, even_count

def  check_performance(approaches):
	time_taken=[]
	l=[1,2,3,4,5,6,7]
	for approach in approaches:
		temp_time=[]
		for _ in range(100):
			start_time=time.time_ns()
			approach(l)
			end_time=time.time_ns()
			temp_time.append(end_time-start_time)
		time_taken.append(sum(temp_time)/100)
	return  list(zip(approaches,time_taken))
	
def give_percentage(a1,l):
    for i in range(len(l)):
        res=((l[i]-a1)/a1)*100
        if res<0:
            print(f"approach {i+2} takes {abs(res):.2f}% less time than approach 1")
        else:
            print(f"approach {i+2} takes {res:.2f}% more time than approach 1")

per=check_performance([a1,a2,a3,a4])
l=[]
for i in range(1,len(per)):
    l.append(per[i][1])
give_percentage(per[0][1],l)
