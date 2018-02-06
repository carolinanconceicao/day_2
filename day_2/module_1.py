'''
Created on 06/02/2018

@author: Carolina
'''
def is_number(valor):
    try:
        return int(valor)
    except:
        return None
    
if __name__ == '__main__':
    
    while True:
        first_number = input("First number")
        first_number = is_number(first_number)
        if (is_number(first_number) != None): break
        
    while True:
        second_number = input("Second number")
        second_number = is_number(second_number)
        if(is_number(first_number) != None): break
    if (first_number == second_number): print ('EQUAL')
    elif (first_number > second_number):print ('HIGUER: {}'. format(first_number))
    else: print('HIGUER'.format(second_number))
    
    pass
