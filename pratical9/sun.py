def check_if_valid(s):
    l=[]

        
    for i in s:
        if i not in ['}',')',']','>']:
            l.append(i)
        elif i in['}',')',']','>']:
            if not l:
                return 0
            elif ((i==')' and l[-1]!='(') or (i=='}' and l[-1]!='{') or (i==']' and l[-1]!='[') or (i=='>' and l[-1]!='<')):
                return 0
            l.pop()

    if len(l)==0:
        return 1
    return 0

    

def get_valid_invalid_text_count(l):
    valid_count_sum=0
    invalid_count_sum=0
   
    for i in l:
        if type(i) in [int,float]:
            continue
               
        if type(i)==str:
            valid_count_sum+=check_if_valid(i)
        else:
            invalid_count_sum+=+1
               
        if type(i) in [list,set,tuple]:
            valid_count,invalid_count=get_valid_invalid_text_count(i)  
            valid_count_sum+=valid_count
            invalid_count_sum+=invalid_count

       
        
    return valid_count_sum,invalid_count_sum
    

print(get_valid_invalid_text_count(['[{(',"(())",[45,("()")]]))


                   