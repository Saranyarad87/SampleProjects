
    
import re

class Alphanumsort():
    
    def __init__(self):
         
        self.sortedstring =''
        self.strval = input("enter alphanumeric string: \n")

# check digit
    def chk_digit(self,val):
        if (val.isdigit()):
            return int(val)
        else:
            return (val)

# split into a list
        
    def mysplit(self,s):
              
        return re.split('([0-9]+)',s)

# Split string into numbers,letters and special charachters

    def splitString_sort(self,chk_str):
        
        lower = []
        upper = []
        number = []
        specialchar = []
        
        for i in range(len(chk_str)):
                          
            if (chk_str[i].isdigit()):
                number.append(chk_str[i])
                    
            elif(chk_str[i] >= 'A' and chk_str[i] <= 'Z'): 
                
                upper += chk_str[i] 
            
            elif(chk_str[i] >= 'a' and chk_str[i] <= 'z'):
                
                lower +=chk_str[i]
            else: 
                specialchar += chk_str[i] 
       
        sort_list = list(map(int,number))
        
        if (sort_list.sort() != 0):
        
            return(sort_list),(sorted(lower,reverse=True)),(sorted(upper,reverse=True)),(sorted(specialchar,reverse=True)) 
        
        else:
            
            print ("error while sorting numbers")
  
# merge sorted list and create final alphanumeric string
    
    def create_alnumstr(self):
        
        str_to_process = self.mysplit(self.strval)
        n,a,A,s = (self.splitString_sort(str_to_process))
        numlist = list(map(str,n))
        s1 =(''.join(numlist))
        s2 =(''.join(a))
        s3 =(''.join(A))
        s4 =(''.join(s))
        final_list = s1+s2+s3+s4
        return final_list
           

# main program
            
if __name__ == '__main__':
            
    x = Alphanumsort()          
    
    print ("sorted string is: %s" %x.create_alnumstr())


