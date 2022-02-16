import time
import multiprocessing
import Parser
import SortAndBin
import Dumb
import Tools
#load input file  outside of if __name__ = main so we can run the wrapper function in parallel

#tasks, machines = Parser.parseInputFile('inputs/randomMax.txt')
#wrapper for sort and bin function to allow multiprocessing
def Sab(s):
	return SortAndBin.SAB(s[0], s[1], rand=1000, seed=s[2])

if __name__ == "__main__":
	#number of random sequences to try
	iters = 1000
	# create 1000 inputs
	for i in range(1000):
		tasks, machines = Tools.createInput(1000,5,i)
		print(F"SEED = {i}")
		#time and run iters multithreaded iterations
		start = time.time() 
		inputs = tuple(zip([tasks]*iters, [machines]*iters, range(iters)))
	
		m = multiprocessing.Pool(processes=16).map(Sab, inputs)
		end = time.time()
		#print("total time= ", end-start)
		randPerformance, distribution = min(m, key=lambda i: i[0])
		performance, distribution = SortAndBin.SAB(tasks, machines)
		Parser.printBriefRunInfo("SAB", performance)
		Parser.printBriefRunInfo("RandSAB", randPerformance)

	#print detailed stats
	#Tools.printDetailedStats(distribution, tasks, machines)
	#
	# really good seeds for rand=1000 and file = randomMax.txt
	#s = 1337
	#s=1692
	
	#simple single threaded approach:
	
