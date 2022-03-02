import Tools
import InputCreation
import Parser

def parseOutput(filename):
	f = open(filename)
	s = f.read().split("\n")
	expectedPerformance = float(s[0])
	distribution = []
	for line in s[1:-1]:
		distribution.append([])
		for num in line.split():
			distribution[-1].append(int(num)) 
	return (expectedPerformance, distribution)

def isDupes(distribution):
	seen = []
	for line in distribution:
		for item in line:
			if item in seen:
				print(f"{item} is a duplicate")
				return True
			else:
				seen.append(item)
	return False

def isMissingTasks(distribution, tasks):
	seen = []
	for	line in distribution:
		for item in line:
			seen.append(item)
	for i in range(len(tasks)): 
		if i not in seen:
			print(f"{i} not in output :/")
			return True
	return False
	
def isValidOutputFile(infilename, outfilename):
	tasks, machines = Parser.parseInputFile(infilename)
	if not Tools.validateInput(tasks, machines):
		print("Invalid Input")
		return False
	expectedPerformance, distribution = parseOutput(outfilename)
	distribution = fixOutputFileDistribution(distribution)
	performance = round(Tools.calcTotalTime(distribution, tasks, machines),2)
	if(expectedPerformance != performance):
		print(f"performance is incorrect, actual = {expectedPerformance} file stated performance {performance}")
		return False
	if(isMissingTasks(distribution, tasks)):
		print("output is missing tasks")
		return False
	if(isDupes(distribution)):
		print("output has a duplicate task")
		return False
	return True
	
def validateOutputFile(infilename, outfilename):
	if(isValidOutputFile(infilename, outfilename)):
		print(f"file {outfilename} is valid output for {infilename}!")
	else:
		print(f"ERROR: file {outfilename} is NOT valid output for {infilename}!")

def fixOutputFileDistribution(distribution) : 
	newDist = []
	for mach in distribution : 
		temp = []
		for task in mach :
			#print(task)
			temp.append(task - 1)
			#print(str(task) + "\n")
		newDist.append(temp)
	return newDist
