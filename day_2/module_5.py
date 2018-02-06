'''
Created on 06/02/2018

@author: Carolina
'''
import sys
import utils
def sum_all(value1, value2):
    soma = 0
    for i in range (value1, value2):
        soma += i
    if (value1 < value2): soma += value2
    return soma

if __name__ == '__main__':
    if(len(sys.argv) != 3):
        print('usage: module.py <int1> <int2>')
        sys.exit(0)
    print(sys.argv)
    value1 = utils.is_number(sys.argv[1])
    value2 = utils.is_number(sys.argv[2])
    if (value1 == None or value2 == None):
        print("usage: module.py <int1><int2>")
        sys.exit(0)
    print (sum_all(value1, value2))
    pass