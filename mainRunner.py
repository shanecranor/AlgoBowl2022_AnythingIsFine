import time
import multiprocessing
import Parser
import Algorithms.SortAndBin as SortAndBin
import Algorithms.BinAndSort as BinAndSort
import Algorithms.AverageBinSort as AverageBinSort
import Algorithms.Dumb as Dumb
import Tools
import InputCreation
import os
"""
Used to run multi core tests of algorithms that need to run multiple times 
"""
#load and validate all inputs
realInputs =[]
for file in os.listdir('real_inputs'):
	tasks, machines = Parser.parseInputFile('real_inputs/' + file)
	Tools.validateInput(tasks,machines)
	perf, dist = Dumb.DUMB(tasks, machines)
	realInputs.append([tasks, machines, perf, dist, "DUMB",file])

#wrappers for random functions
def Sab(temp):
	s, index = temp
	tasks, machines = realInputs[index][0],realInputs[index][1]
	performance, distribution = SortAndBin.SAB(tasks, machines, rand=1000, seed=s)
	return performance, distribution, s
def Bas(temp):
	s, index = temp
	tasks, machines = realInputs[index][0],realInputs[index][1]
	performance, distribution = BinAndSort.BAS(tasks, machines, rand=1000, seed=s)
	return performance, distribution, s

if __name__ == "__main__":
	startSeed = 50000
	for fileIndex in range(len(realInputs)):
		tasks, machines = realInputs[fileIndex][0],realInputs[fileIndex][1]

		#RUN SORT AND BIN
		performance, distribution = SortAndBin.SAB(tasks, machines)

		Parser.printBriefRunInfo("SAB", performance)
		if realInputs[fileIndex][2] > performance:
			realInputs[fileIndex][2] = performance
			realInputs[fileIndex][3] = distribution
			realInputs[fileIndex][4] = "SAB"
		print()


		#RUN AVERAGE BIN SORT
		performance, distribution = AverageBinSort.ABS(tasks, machines)
		if realInputs[fileIndex][2] > performance:
			realInputs[fileIndex][2] = performance
			realInputs[fileIndex][3] = distribution
			realInputs[fileIndex][4] = "ABS"
		Parser.printBriefRunInfo("ABS", performance)
		print() 
		iters = 1
		#RUN RAND BAS 
		start = time.time() 
		iters = 300000
		m = multiprocessing.Pool(processes=64).map(Bas, zip(range(startSeed,startSeed+iters),[fileIndex]*iters))
		end = time.time()
		print("algo run time= ", end-start)
		performance, distribution, seed = min(m, key=lambda i: i[0])
		if realInputs[fileIndex][2] > performance:
			realInputs[fileIndex][2] = performance
			realInputs[fileIndex][3] = distribution
			realInputs[fileIndex][4] = "RandBAS"
		Parser.printBriefRunInfo("RandBAS", performance)
		print("seed:",seed,"\n")

		
		#RUN RAND SAB
		start = time.time() 
		iters = 106000
		m = multiprocessing.Pool(processes=64).map(Sab, zip(range(startSeed,startSeed+iters),[fileIndex]*iters))
		end = time.time()
		print("algo run time= ", end-start)
		performance, distribution, seed = min(m, key=lambda i: i[0])
		if realInputs[fileIndex][2] > performance:
			realInputs[fileIndex][2] = performance
			realInputs[fileIndex][3] = distribution
			realInputs[fileIndex][4] = "RandSAB"
		Parser.printBriefRunInfo("RandSAB", performance)
		print("seed:",seed,"\n")
		
		Parser.generateOutputFile(realInputs[fileIndex][2],realInputs[fileIndex][3],"real_output/OUTPUT_"+realInputs[fileIndex][4]+"_"+realInputs[fileIndex][5])

		#print detailed stats
		#Tools.printDetailedStats(distribution, tasks, machines)

	
