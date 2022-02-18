import time
import multiprocessing
import Parser
import SortAndBin
import BinAndSort
import Dumb
import Tools
"""
Used to run multi core tests of algorithms that need to run multiple times 
"""
#load input file  outside of if __name__ = main so we can run the wrapper function in parallel
tasks, machines = Parser.parseInputFile('inputs/gen_algoinput.txt')

#wrapper for sort and bin function to allow multiprocessing
def Sab(s):
	return SortAndBin.SAB(tasks, machines, rand=1000, seed=s)
def Bas(s):
	return BinAndSort.BAS(tasks, machines, rand=1000, seed=s)

if __name__ == "__main__":
	#time and run 1000 multithreaded iterations
	start = time.time() 
	performance, distribution = SortAndBin.SAB(tasks, machines)
	end = time.time()
	print("algo run time= ", end-start)
	Parser.printBriefRunInfo("SAB", performance)
	print()

	start = time.time() 
	m = multiprocessing.Pool(processes=64).map(Bas, range(1000))
	end = time.time()
	print("algo run time= ", end-start)
	performance, distribution = min(m, key=lambda i: i[0])
	Parser.printBriefRunInfo("RandBAS", performance)
	print()

	start = time.time() 
	m = multiprocessing.Pool(processes=64).map(Sab, range(500000))
	end = time.time()
	print("algo run time= ", end-start)
	performance, distribution = min(m, key=lambda i: i[0])
	Parser.printBriefRunInfo("RandSAB", performance)
	
	#print detailed stats
	#Tools.printDetailedStats(distribution, tasks, machines)
	#
	# really good seeds for rand=1000 and file = randomMax.txt
	#s = 1337
	#s=1692
	
	#simple single threaded approach:
	
	"""
	s=0
	best = SortAndBin.SAB(tasks,machines, rand=1000, seed=s)
	start = time.time()
	for i in range(1000):
		performance, distribution = SortAndBin.SAB(tasks,machines, rand=1000, seed=s)
		if(performance <= best[0]):
			best = performance,distribution
		s+= 1
	end = time.time()
	print("total time= ", end-start)
	performance, distribution = best
	Parser.printBriefRunInfo("SAB", performance)
	#Tools.printDetailedStats(distribution, tasks, machines)
	"""