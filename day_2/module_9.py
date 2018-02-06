'''
Created on 06/02/2018

@author: Carolina
'''

if __name__ == '__main__':
    text = input("Insert text:")
    dict = {}
    #print char_1
    for char_1 in text:
        print (char_1.isalpha()) ##go to the begining of lopp
        if (not char_1) in dict:
        if (char_1) in dict:
            dict[char_1] += 1
        else:
            dict[char_1] = 1
    #sort keys
    for key in sorted (dict.keys()):
        print (key, dict[key])
    print (dict)
    pass