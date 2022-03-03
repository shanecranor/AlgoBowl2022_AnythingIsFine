import outputValidator
import os

for file in os.listdir("verification_outputs"):
	inputIndex = file[-7:-4]
	outputValidator.validateOutputFile(
		f"real_inputs/input_group{inputIndex}.txt",
		f"verification_outputs/{file}",
		quiet=True
	)
