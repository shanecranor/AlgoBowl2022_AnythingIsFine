import time
import Parser
import SortAndBin
import Dumb
import Tools
import InputCreation
import BinAndSort
import AverageBinSort
import multiprocessing


def createInputWrapper(seed):
	distribution, tasks, machines = InputCreation.createBetterOptimalInput(1000, 50, 9550, seed, True, False,  False, True, 50)#+(seed%600))
	if not Tools.validateInput(tasks,machines):
		return (0,0,0,0,0)
	SABperf, SABdist = SortAndBin.SAB(tasks,machines)
	return (SABperf, distribution, tasks, machines, seed)

if __name__ == "__main__":
	#SABperf, distribution, tasks, machines, seed = createInputWrapper(54714)
	#InputCreation.createInputFile(tasks, machines, "seed_54714_max_dificil.txt")

	num = 10000
	start = time.time() 
	m = multiprocessing.Pool(processes=64).map(createInputWrapper, range(53000, num))
	end = time.time()
	print(f"time to generate {num} inputs = {end-start}")
	performance, distribution, tasks, machines, seed = max(m, key=lambda i: i[0])
	Parser.printBriefRunInfo("RandBAS", performance)
	print(seed)
