'''
Created on 06/02/2018

@author: Carolina
'''
def fibonacci(value):
    if (value < 2): return 1
    return_value = 0
    value_1 = 0
    value_2 = 0
    for i in range (1, value):
        value_1 = value_2
        value_2 = i
        return_value += value_1 + value_2
        print('i {} value_1 {} value_2 {} soma: {}'. format(value_1,value_2, return_value))
    return return_value
if __name__ == '__main__':
    print(fibonacci(10))
    pass