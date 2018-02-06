'''
Created on 06/02/2018

@author: Carolina
'''
import utils
import time
def count_down(value):
    for i in range (value, 0, -1):
        print (i)
        time.sleep(1)
    print ('final')
if __name__ == '__main__':
    while True:
        value = input("Introduce an integer number")
        value = utils.is_number(value)
        if value!= None and (value > 0): break

#call countdown
    count_down(value)
    pass