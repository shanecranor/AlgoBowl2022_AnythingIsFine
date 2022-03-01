import outputValidator
import Parser
import random
"""
shuffle input and output files
"""

def shuffleMachines(inputfile, outputfile) : 
    # get input and outputs
    inTask, inMach = Parser.parseInputFile(inputfile)
    outOpt, outDist = outputValidator.parseOutput(outputfile)
    #print(inMach, outDist)
    # shuffle machines around
    for i in range(len(inMach) - 1) : 
        j = random.randint(0, i+1)
        inMach[i], inMach[j] = inMach[j], inMach[i]
        outDist[i], outDist[j] = outDist[j], outDist[i]
    # print shuffled arrs to text files
    ## input
    #print(inMach)
    infile = open("inputs/SeedNewInput.txt", "w")
    infile.write( str(len(inTask)) + "\n" + str(len(inMach)) + "\n")
    for task in inTask :
        infile.write( str(task) + " ")
    infile.write("\n")
    for mach in inMach :
        infile.write( str(mach) + " ")

    ## output
    #print(outDist)
    outfile = open("outputs/SeedNewOutput.txt", "w")
    deciPerf = "{:.2f}".format(round(outOpt,2))
    outfile.write(str(deciPerf) + "\n")
    for i, mach in enumerate(outDist) : 
        for task in mach : 
            outfile.write( str(task) + " " )
        outfile.write("\n")



# UNCOMMENT FOR SEED
shuffleMachines('inputs/seed_678771_max_dificil.txt', 'outputs/seed_678771_OPT_SOLUTION.txt')
# TESTING
#shuffleMachines('inputs/AnotherDemo.txt', 'outputs/output.txt')