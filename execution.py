import time
start = time.time()
a = 0
for i in range(1000):
    a += (i**100)
end = time.time()
print("The time of execution of above program is :", end-start)
