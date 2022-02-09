
"""
Input: tuple (tasks, machines)
Output: tuple (max length, 2D array of task allocation per machine)
Description:
	Sorts the tasks and machines from best to worst and gives the fastest machines the worst tasks
	Returns the length of the solution and the task distribution table
"""
def SSB(tasks, machines):
	taskOrder = tasks.copy()
	machineOrder = tasks.copy()
