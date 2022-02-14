import statistics
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


def printDetailedStats(distribution, tasks, machines):
	timesArr = [0]*len(machines)
	for i, machine in enumerate(distribution):
		#TODO: use numpy for faster addition  (probably not a huge bottleneck tho)
		#https://stackoverflow.com/questions/47734392/python-numpy-array-sum-over-certain-indices
		timesArr[i] = sum(tasks[i] for i in machine)/machines[i]
		print(f"Machine {i}: \t Speed:{machines[i]} \t Runtime: {round(timesArr[i],2)} \t shortest task = {min(tasks[i] for i in machine)} longest task = {max(tasks[i] for i in machine)}")
		#print(f"{machines[i]}, {timesArr[i]}, {min(tasks[i] for i in machine)}")
	print(
		f"""STATS:
	Longest machine: Machine {timesArr.index(max(timesArr))} with a time of: {max(timesArr)} time units
	Average machine time: {sum(timesArr)/len(timesArr)}
	Shortest machine: {min(timesArr)}
	Range: {max(timesArr)-min(timesArr)}
	Standard deviation: {statistics.stdev(timesArr)}
		"""
	)
	return