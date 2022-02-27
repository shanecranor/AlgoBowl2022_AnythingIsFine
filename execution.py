import time as t
import numpy as np
t1 = t.process_time()
start = t.perf_counter()
for i in np.arange(0, 10**8, 1, dtype=np.int64):
    k = i * i
t2 = t.process_time()
end = t.perf_counter()
spend_1 = t2 - t1
spend_2 = end - start
print(" time.process_time(): {}".format(spend_1))
print(" time.perf_counter(): {}".format(spend_2))
