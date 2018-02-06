import utils
import sys 
if __name__ == '__main__':
    vect_float = []
    len_vect = 0
    max = None
    min = None
    sum = 0
    while True:
        number = input("Float number")
        number = utils.is_float(number)
        if number!= None:
            if (number == 0.0): break
            len_vect += 1
            if (max == None or max < number): max = number
            if (min == None or min > number): min = number
            sum += number
            
    if (len_vect == 0):
        print ("No values in vector")
        sys.exit(0)
        
    print('Max: {} Min: {} Average: {}'.format(max, min, sum/len_vect))
    pass