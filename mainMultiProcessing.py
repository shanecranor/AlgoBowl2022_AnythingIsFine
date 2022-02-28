import time
import multiprocessing
import Parser
import Algorithms.SortAndBin as SortAndBin
import Algorithms.BinAndSort as BinAndSort
import Algorithms.AverageBinSort as AverageBinSort
import Algorithms.Dumb as Dumb
import Tools
import InputCreation
"""
Used to run multi core tests of algorithms that need to run multiple times 
"""
#load input file  outside of if __name__ = main so we can run the wrapper function in parallel
tasks, machines = Parser.parseInputFile('inputs/seed_678771_max_dificil.txt')


#wrapper for sort and bin function to allow multiprocessing
def Sab(s):
	performance, distribution = SortAndBin.SAB(tasks, machines, rand=1000, seed=s)
	return performance, distribution, s
def Bas(s):
	performance, distribution = BinAndSort.BAS(tasks, machines, rand=1000, seed=s)
	return performance, distribution, s

if __name__ == "__main__":
	#time and run 1000 multithreaded iterations
	start = time.time() 
	performance, distribution = SortAndBin.SAB(tasks, machines)
	end = time.time()
	print("algo run time= ", end-start)
	Parser.printBriefRunInfo("SAB", performance)
	print()

	start = time.time() 
	performance, distribution = AverageBinSort.ABS(tasks, machines)
	end = time.time()
	print("algo run time= ", end-start)
	Parser.printBriefRunInfo("ABS", performance)
	print() 

	start = time.time() 
	m = multiprocessing.Pool(processes=64).map(Bas, range(20000))
	end = time.time()
	print("algo run time= ", end-start)
	performance, distribution, seed = min(m, key=lambda i: i[0])
	Parser.printBriefRunInfo("RandBAS", performance)
	print("seed:",seed,"\n")

	start = time.time() 
	m = multiprocessing.Pool(processes=64).map(Sab, range(1000))
	end = time.time()
	print("algo run time= ", end-start)
	performance, distribution, seed = min(m, key=lambda i: i[0])
	Parser.printBriefRunInfo("RandSAB", performance)
	print("seed:",seed,"\n")
	

	#print detailed stats
	#Tools.printDetailedStats(distribution, tasks, machines)

	
