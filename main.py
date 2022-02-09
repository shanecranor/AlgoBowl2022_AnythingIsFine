

import Parser
import SortAndBin
import Dumb
tasks, machines = Parser.parseInputFile('inputs/tinydemo.txt')
# print("printing tasks, machines:\n", tasks, machines)
performance, distribution = Dumb.DUMB(tasks,machines)
Parser.printRunInfo("DUMB", performance, distribution)
