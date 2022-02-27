from collections import Counter


with open( '/Users/student/Downloads/inputfile1.txt', 'r') as f:
     data = f.read()  
print(data)
first_line = f.readline()
print(first_line)
print(float(first_line))
