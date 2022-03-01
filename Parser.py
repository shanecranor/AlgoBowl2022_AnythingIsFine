"""
Input: file name
Output: tuple (tasks, machines)
Description:
	Returns a tuple containing a list of machines and a list of tasks
"""
def parseInputFile(fileName):
	#read the file and separate each line into an element of a list
	fileLines = open(fileName, 'r').read().split('\n')
	#remove comments from file if they exist
	for i, line in enumerate(fileLines):
		fileLines[i] = line.split('//')[0] 
	n = int(fileLines[0])
	m = int(fileLines[1])
	tasks = [int(task) for task in fileLines[2].split()]
	machines =  [int(machine) for machine in fileLines[3].split()]
	#check to make sure the numbers add up
	if n != len(tasks):
		print(f"n is defined as {n}, however there are {len(tasks)} tasks listed")
		if m == len(tasks): return # don't return if there is another error
	if m != len(machines):
		print(f"m is defined as {m}, however there are {len(machines)} machines listed")
		return
	return (tasks, machines)

"""
Input: Algorithm name, longest running cpu, distribution
Output: None
Description:
	Prints out which tasks are done by which machine
"""
def printLongRunInfo(name, performance, distribution):
	printBriefRunInfo(name,performance)
	printDistribution(distribution)

"""
Input: Algorithm name, longest running cpu, distribution
Output: None
Description:
	Prints out the performance numbers
"""
def printBriefRunInfo(name, performance):
	print(f"Algorithm {name} used {performance} time units")

"""
Input: distribution
Output: None
Description:
	Prints out a readable version of the output txt
"""
def printDistribution(distribution):
	print(f"Printing Distribution:")
	for i, machine in enumerate(distribution):
		print(f"machine {i}: {machine}")

"""
Input: distribution
Output: 
Description:
	prints a submitable output file
"""
def generateOutputFile(performance, distribution, fileName="outputs/output.txt"):
	print(f"Printing Output File:")
	file = open(fileName, "w")
	#print(performance)
	deciPerf = "{:.2f}".format(round(performance,2))
	file.write(str(deciPerf) + "\n")
	for i, machine in enumerate(distribution):
		machine.sort()
		for task in machine:
			#print(task, end =' ')
			file.write(str(task+1) + " ")
		#print()
		file.write('\n')

"""
Input: list of performance times
Output: which machine results in less amount of time 
Description:
	Goes through the performances list and output which algorithm came up with best results
	Prints list of algorithm name and it's time in order from least to greatest
	Returns algorithm index associated with te minimum algorithm
"""
def printMinPerf(performances):
	# create corresponding indecies for each algorithm
	perfList = []
	i = 0
	for p in performances :
		perfList.append((p, i))
		i = i + 1
	# sort from least to greatest
	perfList.sort(key = lambda x: x[0])
	# print out results
	print("\nSorted order of the Algorithms------")
	algo = ""
	for k in range(len(perfList)) : 
		if perfList[k][1] == 0: algo = "SortAndBin"
		if perfList[k][1] == 1: algo = "BinAndSort"
		if perfList[k][1] == 2: algo = "AvgBinSort"
		print("Algorithm {0} :\t {1}".format(algo, perfList[k][0]))
	return 	perfList[0][1]
	
"""
Input: list of performance times
Output: which machine results in less amount of time 
Description:
"""
def getMinPerf(performances):
	# create corresponding indecies for each algorithm
	perfList = []
	i = 0
	for p in performances :
		perfList.append((p, i))
		i = i + 1
	# sort from least to greatest
	perfList.sort(key = lambda x: x[0])

	return 	perfList[0][1]