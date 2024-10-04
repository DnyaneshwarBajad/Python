def get_ss_sl_i(l):
	temp=[]
	for i in l:
		if type(i) in [int,float]:
			temp.append(i)
		elif type(i) in [list,set,tuple]:
			temp.extend(get_ss_sl_i(i))
		else:
 			pass
	return temp
 	 
 
 	
def get_ss_sl(s=get_ss_sl_i([1,54,67,45,[12,2],['sggs',0,[9999,68.5]]])):
	s.sort()
	return s[1],s[-2]
	
print(get_ss_sl())
	
