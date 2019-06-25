
#Bubble sort in python
#owner: Saranya Radhakrishnan
#ver:Python3

import unittest

class Bsort():
    
    def __init__(self):
        
        self.str_format = 0
        self.str_to_sort = ''
        self.str_length = 0
        self.sort_list=  []
        self.order = ' '
        
    def bubble_sort(self,sortme,order,strlen):
        
        try:
            
        # iterate through the list and swap values 
       
            if (order.lower() in ['d','n']):
               
                for x in range (strlen-1):
                    for y in range (strlen-x-1):
                        if sortme[y] < sortme[y+1]:
                            sortme[y],sortme[y+1] = sortme[y+1],sortme[y]

                return (sortme)
                
            elif (order.lower() in ['a','y']): 
                
                for x in range (strlen-1):
                    for y in range (strlen-x-1):
                        if sortme[y] > sortme[y+1]:
                            sortme[y],sortme[y+1] = sortme[y+1],sortme[y]
               
                return (sortme)
           
            else:
                
                raise Exception
            
        except:
            
            return False
        
    def getinfo(self,userstring,option,order):
        
        try:
            
            self.str_format = option
            self.str_to_sort = userstring
            self.order = order
            
            if ( self.str_format == '1'):
                
               
                temp_list=  self.str_to_sort.split()
                self.sort_list = list(map(int,temp_list))
                self.str_length = len(self.sort_list)
                
                if (self.order.lower() in ['a','d']):
                    pass
                else:
                    raise Exception
                    
               
            elif (self.str_format == '2'):
                
                
                self.sort_list=  self.str_to_sort.split()
                self.str_length = len(self.sort_list)
                
        
                if (self.order.lower() in ['y','n']):
                    pass
                else:
                    raise Exception
                    
            else:
                
                print ("Please select option 1 or 2 to try out the sorting.")
                raise Exception
            
            return (self.bubble_sort(self.sort_list,self.order,self.str_length))
            
        except:
            
            #print ("Please re-run the program with valid input.")
            return False
    
    

class Testfunctions(unittest.TestCase): 
      
    def setUp(self): 
        
        self.x = Bsort()
        pass
  
    # Validate buube sort algorithm
    def testcase1(self): 
        
        print ("TC1 - Testing with numbers with inalid sorting order")
        self.assertFalse(self.x.getinfo('4 5 6 3 4 2','1','r'))
    
    def testcase2(self): 
        
        print ("TC2 - Testing with numbers to sort in ascending order")
        list2 = self.x.getinfo('4 5 6 3 4 2','1','A')
        self.assertEqual(list2, [2, 3, 4, 4, 5, 6])
    
    def testcase3(self): 
        print ("TC3 - Testing with numbers to sort in descending order")
        list3 = self.x.getinfo('4 5 6 3 4 2','1','d')
        self.assertEqual(list3, [6, 5, 4, 4, 3, 2])
    
    def testcase4(self): 
        print ("TC4 - Testing with double and triple digit numbers to sort in ascending order")
        list4 = self.x.getinfo('455 57 32 8 782','1','a')
        self.assertEqual(list4, [8, 32, 57, 455, 782])
    
    def testcase5(self): 
        print ("TC5 - Testing with alphabets with invalid answer to y/n question")
        self.assertFalse(self.x.getinfo('a b s c h e','2','t'))
    
    def testcase6(self): 
        print ("TC6 - Testing with alphabets sorted alphabetically")
        list5 = self.x.getinfo('a b s c h e','2','y')
        self.assertEqual(list5,['a','b','c','e','h','s'])
    
    def testcase7(self): 
        print ("TC7 - Testing with alphabets sorted non-alphabetically")   
        list6 = self.x.getinfo('a b s c h r e','2','n')    
        self.assertEqual(list6,['s', 'r', 'h', 'e', 'c', 'b', 'a']) 
    
    def testcase8(self): 
        print ("TC8 - Testing with words sorted alphabetically") 
        list7 = self.x.getinfo('hat bun sun cat rain','2','y')
        self.assertEqual(list7,['bun', 'cat', 'hat', 'rain', 'sun'])
    
    def testcase9(self): 
        print ("TC9 - Testing with Invalid format selection instead of 1 for nmber and 2 for alphabets" )
        self.assertFalse(self.x.getinfo('4 3 5 6 ','2','a'))
       

# main program


if __name__ == '__main__':
       

        unittest.main()
       
    
    
    
    
    

