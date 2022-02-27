import importlib
from importlib.resources import path
from multiprocessing.spawn import import_main_path
import os
from pydoc import importfile
import difflib
import sys
import numpy as np




def file_read(fname):
        content_array = []
        with open(fname) as f:
                   
                for line in f:
                        content_array.append(line)
                print(content_array)


file_read('test.txt')

initialArray = np.array([file_read('test.txt')])
  

print("Our Initial Array: ", str(initialArray))
print("Original type: " + str(type(initialArray[0])))
  

finalArray = np.asarray(initialArray, dtype = np.float64, 
                        order ='C')
  

print("Our Final Array: ", str(finalArray))
print(list(map(float, initialArray)))


