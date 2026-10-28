
def countdown(number): 
    '''  
    This recursive function takes a positive integer number  
    and counts the number down to zero printing each value. 
    ''' 

    if number < 0:
     return

    print(number) 
    countdown(number-1) 