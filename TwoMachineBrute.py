"""
IDEA:
This is really bad, it only works for two machines.
But basically this program generates all the possible permutations of a given list.
Then do a for loop to run through the list of two machines, figure out the cost of the
current permutation on machine_one and machine_two, then return the max of the two cost

"""

from Tools import combinationCompiler

# Main function
def TMB(tasksList, machinesList):

    # Step 1: create a list of all possible combinations of tasks
    combinationLists = []
    ccombinationLists = combinationCompiler(tasksList)

    # Step 2: run Algorithm for the two machines, filling out resultsList
    totalTime = 0
    for task in tasksList:
        totalTime += task

    resultsList = []
    currentResult = 0
    for machine in machinesList:
        for combination in combinationLists:
            currentResult = runBruteAlg(combination, machine, machinesList, totalTime)
            resultsList.append(currentResult)

    # Step 3: figure out the minimum result, return it
    minResult = resultsList[0]
    for result in resultsList:
        if(result < minResult):
            minResult = result
    
    return minResult

# Helper function that runs the actual algorithm
"""
currentCombination: the current combination of tasks that the for loop in TMB is on
currentMachine: the current machine that the for loop in TMB is on
machinesList: the list of two machines
totalTime: the sum of all the tasks' times

"""
def runBruteAlg(currentCombination, currentMachine, machinesList, totalTime):
    # Step 1: calculate the two speeds of the given combination
    firstSpeed = 0
    for task in currentCombination:
        firstSpeed += task

    secondSpeed = totalTime - firstSpeed

    # Step 2: calculate the individual times
    firstTime = firstSpeed / currentMachine

    secondTime = 0
    if(currentMachine == machinesList[0]):
        secondTime = secondSpeed / machinesList[1]
    else:
        secondTime = secondSpeed / machinesList[0]

    # Step 3: return the max of firstTime and secondTime
    if(firstTime > secondTime):
        return firstTime
    else:
        return secondTime