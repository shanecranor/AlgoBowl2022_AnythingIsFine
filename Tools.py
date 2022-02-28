import itertools 		# for permuting
import statistics
import random
import math
from tkinter import W


"""
Input: list of tasks and machines
Output: true if valid false if invalid
Description:
	Prints if an input does not match the spec
"""
def validateInput(tasks, machines):
	if tasks is None or machines is None:
		return False
	if len(tasks) > 1000:
		print(F"There are {len(tasks)} tasks in this input, max possible is 1000")
		return False
	if len(machines) > 50:
		print(F"There are {len(machines)} in this input, max possible is 50")
		return False
	for task in tasks:
		if task < 1:
			print(F"{task} is not a valid task length")
			return False
		if task > 10000:
			print(F"{task} is not a valid task length")
			return False
	for machine in machines:
		if machine < 1:
			print(F"{machine} is not a valid machine speed")
			return False
		if machine > 20:
			print(F"{machine} is not a valid machine speed")
			return False
	return True
"""
Input: distribution, list of tasks, list of machines
Output: machine that takes the longest
Description:
	Loops through each machine in the distribution and find out which one ends last
	distribution = 
"""
def calcTotalTime(distribution, tasks, machines):
	timesArr = [0]*len(machines)
	for i, machine in enumerate(distribution):
		#TODO: use numpy for faster addition  (probably not a huge bottleneck tho)
		#https://stackoverflow.com/questions/47734392/python-numpy-array-sum-over-certain-indices
		timesArr[i] = sum(tasks[k] for k in machine)/machines[i]
	return max(timesArr)


def generateTimesArr(distribution, tasks, machines):
	timesArr = [0]*len(machines)
	for i, machine in enumerate(distribution):
		#TODO: use numpy for faster addition  (probably not a huge bottleneck tho)
		#https://stackoverflow.com/questions/47734392/python-numpy-array-sum-over-certain-indices
		timesArr[i] = sum(tasks[k] for k in machine)/machines[i]
	return timesArr

def printStats(timesArr):
	print(
		f"""STATS:
	Longest machine: Machine {timesArr.index(max(timesArr))} with a time of: {max(timesArr)} time units
	Average machine time: {sum(timesArr)/len(timesArr)}
	Shortest machine: {min(timesArr)}
	Range: {max(timesArr)-min(timesArr)}
	Standard deviation: {statistics.stdev(timesArr)}
		"""
	)

def printStats(distribution, tasks, machines):
	timesArr = generateTimesArr(distribution, tasks, machines)
	print(
		f"""STATS:
	Longest machine: Machine {timesArr.index(max(timesArr))} with a time of: {max(timesArr)} time units
	Average machine time: {sum(timesArr)/len(timesArr)}
	Shortest machine: {min(timesArr)}
	Range: {max(timesArr)-min(timesArr)}
	Standard deviation: {statistics.stdev(timesArr)}
		"""
	)


def getStats(timesArr):
	longest = (timesArr.index(max(timesArr)), max(timesArr)) #longest machines index, and it's time
	avg = sum(timesArr)/len(timesArr)
	shortest = min(timesArr)
	range = longest[1]-shortest
	std = statistics.stdev(timesArr)
	return longest, avg, shortest, range, std

def printDetailedStats(distribution, tasks, machines):
	timesArr = generateTimesArr(distribution, tasks, machines)
	for i in range(len(timesArr)):
		if timesArr[i] == 0:
			print(f"Machine {i}: \t Speed:{machines[i]} No tasks alloted")
		else:
			print(f"Machine {i}: \t Speed:{machines[i]} \t Runtime: {round(timesArr[i],2)} \t shortest task = {min(tasks[i] for i in machine)} longest task = {max(tasks[i] for i in machine)}")
		#print(f"{machines[i]}, {timesArr[i]}, {min(tasks[i] for i in machine)}")
	printStats(timesArr)

"""
result: the answer the algorithm got
listOfLists: a 2D array of all the lists of tasks assigned to each machine, in order from first machine to last

"""

def createOutputFile(result, listOfLists, filePath):
	# first, create a blank text file
	# Might need to ask about file path stuff??
	with open(filePath, 'w') as f:
		# write the result at the top
		f.write(result)

		# write all the tasks assigned to each machine in order 
		for list in listOfLists:
			for task in list:
				f.write(task.rstrip("\n"))
				if task != list[-1]:
					f.write(" ".rstrip("\n"))
			f.write("\n")

	# close the file
	f.close()




"""
Input: tasksList
Output: A list of permuted tasksLists
Description:
	Use the itertools module to create a list of all permutations
	of inputted tasksList

	in-depth explanation found here:
	https://www.kite.com/python/answers/how-to-find-all-combinations-of-a-list-in-python
"""
def combinationCompiler(tasksList):
	# create a list to hold the permuted lists
	permutedLists = []
	for r in range(len(tasksList)+1):
		# permute the current combination
		combinationObject = itertools.combinations(tasksList, r)

		# add current combination to a list
		currentCombination = list(combinationObject)
		# add currentCombination to big list
		permutedLists.append(currentCombination)

	return permutedLists

