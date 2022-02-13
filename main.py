

import Parser
import SortAndBin
import Dumb
tasks, machines = Parser.parseInputFile('inputs/randomMax.txt')
# print("printing tasks, machines:\n", tasks, machines)
performance, distribution = SortAndBin.SSB(tasks,machines)

Parser.printBriefRunInfo("SSB", performance)
