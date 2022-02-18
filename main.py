import time
import Parser
import SortAndBin
import Dumb
import Tools
import BinAndSort




tasks, machines = Parser.parseInputFile('inputs/randomMax.txt')
performance, distribution = SortAndBin.SAB(tasks,machines)
Parser.printBriefRunInfo("SAB", performance)

performance, distribution = BinAndSort.BAS(tasks,machines)
Parser.printBriefRunInfo("BAS", performance)
Tools.printDetailedStats(distribution,tasks, machines)


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