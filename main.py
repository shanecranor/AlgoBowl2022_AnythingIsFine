import time
import Parser
import SortAndBin
import Dumb
import Tools
import BinAndSort
import AverageBinSort

tasks, machines = Parser.parseInputFile('inputs/AnotherDemo.txt')
performance1, distribution1 = SortAndBin.SAB(tasks,machines)
Parser.printBriefRunInfo("SAB", performance1)
#Tools.printDetailedStats(distribution1, tasks, machines)

performance2, distribution2 = BinAndSort.BAS(tasks,machines)
Parser.printBriefRunInfo("BAS", performance2)
#Tools.printDetailedStats(distribution2, tasks, machines)

performance3, distribution3 = AverageBinSort.ABS(tasks,machines)
Parser.printBriefRunInfo("ABS", performance3)
#Tools.printDetailedStats(distribution3, tasks, machines)

performance4, distribution4 = PercentageBinSort.PBS(tasks,machines)
Parser.printBriefRunInfo("PBS", performance4)
#Tools.printDetailedStats(distribution4, tasks, machines)

# find best performance and print result
num = Parser.printMinPerf([performance1, performance2, performance3, performance4])
# print to output file
if (num == 1) : Parser.generateOutputFile(performance1, distribution1)
if (num == 2) : Parser.generateOutputFile(performance2, distribution2)
if (num == 3) : Parser.generateOutputFile(performance3, distribution3)

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