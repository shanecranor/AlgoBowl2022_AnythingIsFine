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
def generateOutputFile(performance, distribution):
	# TODO: write a version of this that outputs as a string and or prints to a file
	print(f"Printing Output File:")
	print(performance)
	for i, machine in enumerate(distribution):
		for task in machine:
			print(task, end =' ')
		print()
