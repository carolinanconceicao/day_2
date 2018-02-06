'''
Created on 06/02/2018

@author: Carolina
'''
import utils
if __name__ == '__main__':
    while True:
        value = input("Introduce an integer number")
        value = utils.is_number(value)
        if value != None: break
    if ((value % 2) == 0): print ('even')
    else: print ('odd')
    
    
    pass