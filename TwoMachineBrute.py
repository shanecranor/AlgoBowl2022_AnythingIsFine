"""
IDEA:
This is really bad, it only works for two machines.
But basically this program generates all the possible permutations of a given list.
Then do a for loop to run through the list of two machines, figure out the cost of the
current permutation on machine_one and machine_two, then return the max of the two cost

"""

from Tools import combinationCompiler


def TMB(tasksList, machinesList):

    # Step 1: create a list of all possible combinations of tasks
    combinationLists = []
    ccombinationLists = combinationCompiler(tasksList)

    # Step 2: run Algorithm for the two machines
    for machine in machinesList:
        for combination in combinationLists:
            pass