'''
Created on 06/02/2018

@author: Carolina
'''
import utils
import os
import sys
if __name__ == '__main__':
    file_name = input('file to sum: ')
# Uma forma de ver se o ficheiro existe:
#    if(not os.path.exists(file_name)):
#         print("File {} does not exist".format(file_name))
#         sys.exit(1)  
    soma=0
#Outra forma de ver se o ficheiro existe:
    try:
        with open(file_name) as handle_in:
            for line in handle_in: #read line by line
                value = utils.is_number(line) #test integer
                if (value != None): soma += value
    except:
        print("File {} does not exist".format(file_name))
        sys.exit(1)

    print ('Sum:{}'.format(soma))

    pass