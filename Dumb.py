"""
Input: list of tasks, list of machines
Output: tuple (max length, 2D array of task allocation per machine)
Description:
	puts all the tasks on the fastest machine
	Returns the length of the solution and the task distribution table
"""
def DUMB(tasks, machines):
	#create empty output distribution
	distribution = []
	for i in range(len(machines)):
		distribution.append([])

	#find fastest machine
	fastestIndex, fastestSpeed = (0, machines[0])
	for i, machine in enumerate(machines):
		if machine > fastestSpeed:
			fastestIndex, fastestSpeed = (i, machine)

	#put all tasks on the fastest machine
	for i in range(len(tasks)):
		distribution[fastestIndex].append(i)
	return (calcTotalTime(distribution, tasks, machines), distribution)


"""
Input: distribution, list of tasks, list of machines
Output: machine that takes the longest
Description:
	Loops through each machine in the distribution and find out which one ends last
"""
def calcTotalTime(distribution, tasks, machines):
	timesArr = [0]*len(machines)
	for i, machine in enumerate(distribution):
		#TODO: use numpy for faster addition  (probably not a huge bottleneck tho)
		#https://stackoverflow.com/questions/47734392/python-numpy-array-sum-over-certain-indices
		timesArr[i] = sum(tasks[i] for i in machine)/machines[i]
	return max(timesArr)

