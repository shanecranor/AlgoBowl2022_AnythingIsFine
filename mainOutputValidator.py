import outputValidator
import os

for file in os.listdir("uploaded_output"):
	inputIndex = file[-7:-4]
	outputValidator.validateOutputFile(
		f"real_inputs/input_group{inputIndex}.txt",
		f"uploaded_output/{file}"
	)
