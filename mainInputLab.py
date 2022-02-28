import time
import Parser
import Algorithms.SortAndBin as SortAndBin
import Algorithms.Dumb as Dumb
import Tools
import InputCreation
import Algorithms.BinAndSort as BinAndSort
import Algorithms.AverageBinSort as AverageBinSort
import multiprocessing


def createInputWrapper(seed):
	distribution, tasks, machines = InputCreation.createBetterOptimalInput(1000, 50, 9550, seed, True, False,  False, True, 50)#+(seed%600))
	if not Tools.validateInput(tasks,machines):
		return (0,0,0,0,0)
	SABperf, SABdist = SortAndBin.SAB(tasks,machines)
	return (SABperf, distribution, tasks, machines, seed)

if __name__ == "__main__":
	SABperf, distribution, tasks, machines, seed = createInputWrapper(678771)
	InputCreation.createInputFile(tasks, machines, "seed_678771_max_dificil.txt")
	Parser.generateOutputFile(9550.0, distribution, "seed_678771_OPT_SOLUTION")
	quit()
	num = 1650000
	startingPoint = 950000
	#163520
	#460445
	#678771
	stops = 25
	best = []
	for i in range(stops):
		startSeed = startingPoint+int((num-startingPoint)/stops)*i
		start = time.time() 
		m  = multiprocessing.Pool(processes=64).map(createInputWrapper, range(startSeed, startSeed + int((num-startingPoint)/stops)))
		end = time.time()

		print(f"{startSeed}/{num} time to generate {int((num-startingPoint)/stops)} inputs = {end-start}")
		performance, distribution, tasks, machines, seed = max(m, key=lambda i: i[0])
		Parser.printBriefRunInfo("Local Best", performance)
		print(seed)
		best.append((performance, distribution, tasks, machines, seed))
		performance, distribution, tasks, machines, seed = max(best, key=lambda i: i[0])
		Parser.printBriefRunInfo("Global Best", performance)
		print(seed)
		print()
