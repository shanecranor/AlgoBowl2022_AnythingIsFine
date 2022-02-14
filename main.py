import time
import Parser
import SortAndBin
import Dumb
import Tools


tasks, machines = Parser.parseInputFile('inputs/randomMax.txt')
performance, distribution = SortAndBin.SAB(tasks,machines)
Parser.printBriefRunInfo("SAB", performance)
Tools.printDetailedStats(distribution, tasks, machines)
