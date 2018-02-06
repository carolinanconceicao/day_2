'''
Created on 06/02/2018

@author: Carolina
'''
import utils
import sys 
if __name__ == '__main__':
    vect_float = []
    while True:
        number = input("Float number")
        number = utils.is_float(number)
        if number!= None:
            if (number == 0.0): break
            vect_float.append(number)
    if (len(vect_float)==0):
        print ("No values in vector")
        sys.exit(0)
    print(vect_float)
    max = None
    min = None
    sum = 0
    for value in vect_float:
        if (max == None or max < value): max = value
        if (min == None or min > value): min = value
        sum += value
    print('Max:{} Min:{} Average{}'.format(max, min, sum/len(vect_float)))
    pass
