import Parser
import SortAndBin
import Dumb
import Tools
tasks, machines = Parser.parseInputFile('inputs/randomMax.txt')
#print(tasks, "\n", machines)
# print("printing tasks, machines:\n", tasks, machines)
performance, distribution = SortAndBin.SAB(tasks,machines)
Parser.printBriefRunInfo("SAB", performance)
Tools.printDetailedStats(distribution, tasks, machines)