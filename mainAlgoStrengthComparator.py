import time
import multiprocessing
import Parser
import SortAndBin
import Dumb
import Tools
import matplotlib.pyplot as plt
import numpy as np
import statistics
"""
Used to create graphs of standard deviation in tasks vs variablility in output.
Mostly just ugly placeholder code
"""
#load input file  outside of if __name__ = main so we can run the wrapper function in parallel

#tasks, machines = Parser.parseInputFile('inputs/randomMax.txt')
#wrapper for sort and bin function to allow multiprocessing
def Sab(s):
	return SortAndBin.SAB(s[0], s[1], rand=1000, seed=s[2])

if __name__ == "__main__":
	#number of random sequences to try
	iters = 1000
	results = []
	# create 1000 inputs
	tasks, machines = Tools.createInput(1000,50,0,69)
	print(machines)
	tasks, machines = Tools.createInput(1000,50,2,69) 
	print(machines)

	for i in range(0,1000):
		f2 = open("outputsave.txt", "a")
		tasks, machines = Tools.createInput(1000,50,i,69)
		if i % 10 == 0:
			print(F"SEED = {i}")
		#time and run iters multithreaded iterations
		start = time.time() 
		inputs = tuple(zip([tasks]*iters, [machines]*iters, range(iters)))
	
		m = multiprocessing.Pool(processes=64).map(Sab, inputs)
		end = time.time()
		#print("total time= ", end-start)
		randPerformance, distribution = min(m, key=lambda i: i[0])
		performance, distribution = SortAndBin.SAB(tasks, machines)
		# Parser.printBriefRunInfo("SAB", performance)
		# Parser.printBriefRunInfo("RandSAB", randPerformance)
		results.append((performance, randPerformance, i , (performance-randPerformance)/performance, statistics.stdev(tasks)/statistics.mean(tasks)))
		r=results[-1]
		f2.write(f"{round(r[0],2)}, {round(r[1],2)}, {round(r[2],2)}, {round(r[3],5)}, {round(r[4],4)}\n")
		f2.close()
	results.sort(key=lambda x: (x[0]-x[1])/x[0])
	out = ""
	f2.close()
	for r in results:
		out += f"{round(r[0],2)}, {round(r[1],2)}, {round(r[2],2)}, {round(r[3],5)}, {round(r[4],4)}\n"
	f = open("output.txt", "w")
	f.write(out)
	f.close
	# worst = Tools.createInput(100,5,511)
	# best = Tools.createInput(100,5,561)

	# plt.hist(best[0],bins=100, range = (0,10000))
	# plt.hist(worst[0],bins=100, range = (0,10000))
	# #print(best[0])
	# plt.show()
	
	# plt.hist(best[1],bins=20, range = (0,20))
	# plt.hist(worst[1],bins=20, range = (0,20))
	# print(best[0])
	# plt.show()
	# input("exit")
	#print detailed stats
	#Tools.printDetailedStats(distribution, tasks, machines)
	#
	# really good seeds for rand=1000 and file = randomMax.txt
	#s = 1337
	#s=1692
	
	#simple single threaded approach:
	
