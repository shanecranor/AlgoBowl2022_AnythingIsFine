import Tools
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
	return (Tools.calcTotalTime(distribution, tasks, machines), distribution)



