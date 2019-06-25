
<<<<<<< HEAD
#Alphanumeric sort in python
#owner: Saranya Radhakrishnan
#ver:Python3

# Python code to demonstrate working of unittest 
import unittest,re

=======

#Alphanumeric sort in python
#owner: Saranya Radhakrishnan
#ver:Python3
  
import re
>>>>>>> 5d69dbcf7994f8a44168360250c5270c330998e0

class Alphanumsort():
    
    def __init__(self):
         
        self.sortedstring =''

# check digit
    def chk_digit(self,val):
        if (val.isdigit()):
            return int(val)
        else:
            return (val)

# split string into a list
        
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
            return False
  
# merge sorted list and create final alphanumeric string
    
    def create_alnumstr(self,strval):
        
        str_to_process = self.mysplit(strval)
        n,a,A,s = (self.splitString_sort(str_to_process))
        numlist = list(map(str,n))
        s1 =(''.join(numlist))
        s2 =(''.join(a))
        s3 =(''.join(A))
        s4 =(''.join(s))
        final_list = s1+s2+s3+s4
        return final_list
           

  
class Testfunctions(unittest.TestCase): 
      
    def setUp(self): 
        
        self.x = Alphanumsort()
        pass
  
    # chk_digit() works as expected
    
    def test_chk_digit(self): 
        
        print ("TC1 - Testing chk_digit module..")
        
        self.assertEqual( self.x.chk_digit('8'),int(8)) 
        
        self.assertEqual(self.x.chk_digit('t'), 't')
        
        self.assertEqual(self.x.chk_digit('&'), '&')
               
    #  mysplit() works as expected 
    def test_mysplit(self):   
        print ("TC2 - Testing mysplit module..")      
        
        newlist = self.x.mysplit('ABgt34')
        self.assertEqual(newlist, ['ABgt', '34', '']) 
            
    #  splitString_sort() works as expected
    
    def test_splitString_sort(self): 
        print ("TC3 - Testing splitString_sort module..")      
                
        y = self.x.splitString_sort(['A','B','g','t','3','4'])
        self.assertEqual(y,([3, 4], ['t', 'g'], ['B', 'A'], []))
    
    #  alphanumericsort works with 3 different inputs
    
    def test_alphanumsort(self): 
        
        print ("TC4 - Testing Alphanumeric sort with 3 different strings")
        val1 = self.x.create_alnumstr('A11a4')
        val2 = self.x.create_alnumstr('D5(2sI45')
        val3 =self.x.create_alnumstr('H78g2!')
        self.assertEqual(self.x.create_alnumstr('A11a4'),val1)
        self.assertEqual(self.x.create_alnumstr('D5(2sI45'),val2)
        self.assertEqual(self.x.create_alnumstr('H78g2!'),val3)
        #print ("Sort A11a4 : %s" %val1)
        #print ("Sort D5(2sI45 : %s" %val2)
        #print ("Sort H78g2!: %s" %val3)
        

# main program
            
if __name__ == '__main__':
    
    unittest.main()

    
   
