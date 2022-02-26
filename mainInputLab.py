import time
import Parser
import SortAndBin
import Dumb
import Tools
import InputCreation
import BinAndSort
import AverageBinSort
for i in range(100):
	distribution, tasks, machines = InputCreation.createBetterOptimalInput(1000, 50, 5000 + (i * 70), i+1)
	print(i)
	Parser.printBriefRunInfo("OPT", Tools.calcTotalTime(distribution,tasks,machines))
	range = Tools.getStats(Tools.generateTimesArr(distribution,tasks, machines))[3]
	if( range != 0):
		print("not optimal")
		continue

	Tools.validateInput(tasks,machines)
	performance1, distribution1 = SortAndBin.SAB(tasks,machines)
	Parser.printBriefRunInfo("SAB", performance1)
	#Tools.printDetailedStats(distribution1, tasks, machines)

	performance2, distribution2 = BinAndSort.BAS(tasks,machines)
	Parser.printBriefRunInfo("BAS", performance2)
	#Tools.printDetailedStats(distribution2, tasks, machines)

	performance3, distribution3 = AverageBinSort.ABS(tasks,machines)
	Parser.printBriefRunInfo("ABS", performance3)
	#Tools.printDetailedStats(distribution3, tasks, machines)

# # find best performance and print result
# num = Parser.printMinPerf([performance1, performance2, performance3])
# # print to output file
# if (num == 0) : Parser.generateOutputFile(performance1, distribution1)
# if (num == 1) : Parser.generateOutputFile(performance2, distribution2)
# if (num == 2) : Parser.generateOutputFile(performance3, distribution3)

### Code for performance testings using time.time()
# start = time.time() 
# for i in range(100):
# 	performance, distribution = SortAndBin.SAB(tasks,machines)
# end = time.time()
# print("total time= ", end-start)
# for i in range(100):
# 	performance, distribution = BinAndSort.BAS(tasks,machines)
# 	#Parser.printBriefRunInfo("BAS", performance)
# end = time.time()
# print("total time= ", end-start)