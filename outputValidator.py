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
	
def validateOutputFile(infilename, outfilename):
	tasks, machines = Parser.parseInputFile(infilename)
	if not Tools.validateInput(tasks, machines):
		print("Invalid Input")
		return False
	expectedPerformance, distribution = parseOutput(outfilename)
	performance = Tools.calcTotalTime(distribution, tasks, machines)
	if(expectedPerformance != performance):
		print("performance is incorrect")
		return False
	if(isMissingTasks(distribution, tasks)):
		print("output is missing tasks")
		return False
	if(isDupes(distribution)):
		print("output has a duplicate task")
		return False
	return True

if(validateOutputFile("seed_678771_max_dificil.txt","seed_678771_OPT_SOLUTION")):
	print("file is valid!")
else:
	print("file is invalid :/")
