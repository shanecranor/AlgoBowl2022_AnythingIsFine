import Tools
import random
"""
Input: tuple (tasks, machines)
Output: tuple (max length, 2D array of task allocation per machine)
Description:
	Calculates average time of how long it takes all machines to do all tasks
    Input tasks into machine until it reaches close to the average time
    Place remaining tasks into machine(s) with smallest time until all tasks are assigned to a computer
"""
def ABS(tasks, machines, rand=-1, seed=-1):
    #sort all tasks and machines
    taskOrder = sortRememberOrder(tasks)
    machineOrder = sortRememberOrder(machines)
    #calculate the sum of tasks and machines
    sumT = sum(task[0] for task in taskOrder)
    sumM = sum(mach[0] for mach in machineOrder)
    # get average time
    avg = sumT / sumM
    # put tasks into each machine until computation time reaches average
    outputMatrix = []
    i = 0
    for m in machineOrder :
        arr = []
        time = 0
        while time < avg :
            arr.append(taskOrder[i])
            i = i + 1
            time = sum(k[0] for k in arr) / m[0]
        # remove last element so that time is most definitely under average time
        arr.pop()
        i = i - 1
        time = sum(k[0] for k in arr) / m[0]
        # append the tasks to outputMatrix
        outputMatrix.append([m, arr, time])
    # for remaining tasks, input them into array with smallest time
    for x in range(i, len(taskOrder)) :
        # always reset reorder output matrix so it's in computing time order
        outputMatrix.sort(key=lambda x: x[2])
        # add task to first machine in outputMatrix
        outputMatrix[0][1].append(taskOrder[x])
        # update time
        outputMatrix[0][2] = sum(k[0] for k in outputMatrix[0][1]) / outputMatrix[0][0][0]
    # reorder outputMatrix so that it's in computer input order
    outputMatrix.sort(key=lambda x: x[0][1])
	# create the output distribution in the right format
    distribution = []
    for i in range(len(machineOrder)) :
        machs = []
        for task in outputMatrix[i][1] : 
            machs.append(task[1])
        distribution.append(machs)
    # return
    return (Tools.calcTotalTime(distribution, tasks, machines), distribution)
"""
Input: list
Output: list
Description:
	sorts list based on machine speed (fastest to slowest)
"""
def sortRememberOrder(list):
	listOrder = []
	for i, item in enumerate(list):
		listOrder.append((item, i))
	def listKey(itemPair):
		return itemPair[0]*-1
	listOrder.sort(key=listKey)
	return listOrder