'''
Created on 06/02/2018

@author: Carolina
'''

if __name__ == '__main__':

    text = input ('Insert text:')
    dict = {}
    for word in text.split(): #other variant possible: split(\t), split(',')
        if word in dict:
            dict[word] += 1
        else: dict[word] = 1
    print (dict)
    pass