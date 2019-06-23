
#Bubble sort in python
#owner: Saranya Radhakrishnan
#ver:Python3

class Bsort():
    
    def __init__(self):
        
        self.str_format = 0
        self.str_to_sort = ''
        self.sort_list=  []
        self.str_length = 0
        self.order = ''
        
    def getinfo(self):
        
        try:
            
            self.str_format = input ("Welcome to the bubble sort program.What would you like to sort today? \n 1.Numbers \n 2.Alphabets \n\n")
           
        
            if ( self.str_format == '1'):
                
                self.str_to_sort = input("Please enter numbers here with spaces: ")
                sort_list=  self.str_to_sort.split()
                self.sort_list = list(map(int,sort_list))
                self.str_length = len(self.sort_list)
                self.order = input ("How would you like to sort the numbers.Please type 'a' for ascending or 'd' for descending: ")
                if (self.order.lower() in ['a','d']):
                    pass
                else:
                    print ( "sorting order selected is not valid, defaulting to ascending order")
                    self.order = 'a'
                    
               
            elif (self.str_format == '2'):
                
                self.str_to_sort = input("Please enter alphabets here with spaces: ")
                self.sort_list=  self.str_to_sort.split()
                self.str_length = len(self.sort_list)
                self.order = input ("Would you like to sort alphabetically? (y/n) :")
        
                if (self.order.lower() in ['y','n']):
                    pass
                else:
                    print ("sorting order has not been selected, defaulting to alphabetical order")
                    self.order = 'y'
                    
            else:
                
                print ("Please select option 1 or 2 to try out the sorting.")
                raise Exception
            
            return True
        except:
            print ("Please re-run the program with valid input.")
            return False
    
    def bubble_sort(self):
        
        try:
            
        # iterate through the list and swap values 
            if (self.getinfo() ==  True):
       
                if (self.order.lower() in ['d','n']):
                   
                    for x in range (self.str_length-1):
                        for y in range (self.str_length-x-1):
                            if self.sort_list[y] < self.sort_list[y+1]:
                                self.sort_list[y],self.sort_list[y+1] = self.sort_list[y+1],self.sort_list[y]

                    return (self.sort_list)
                    
                elif (self.order.lower() in ['a','y']): 
                    
                    for x in range (self.str_length-1):
                        for y in range (self.str_length-x-1):
                            if self.sort_list[y] > self.sort_list[y+1]:
                                self.sort_list[y],self.sort_list[y+1] = self.sort_list[y+1],self.sort_list[y]
                   
                    return (self.sort_list)
                
                else:
                    
                    raise Exception
            
            else:
                
                print ("Exiting...")
                raise Exception
            
        except:
            
            return False
          

#Main program

if __name__ == '__main__':
    
    try:
        
        s = Bsort()
        
        if (s.bubble_sort()):
            print ("Program execution completed")
        else:
            print ("Good Bye!")
    
    except:
        
        print ("Error occurred in main program.")
    
    
    
    

