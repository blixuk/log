#!/usr/bin/env python3

from datetime import datetime
import fileinput
import argparse
import os

def readInput():
	# assign fileinput.input to input variable for handling stdin input
	with fileinput.input('-') as input:
		# create new variable 'data' for storing stdin input
		data = f'{getDateTime()}\n\n' # add current time and date
		for line in input: # loop through all line in the stdin input
			data = data + line # keep appending each new line
		return data # return the data

def writeFile(filePath, stdin, verbose):
	# open a new file at 'filePath' for writing stdin data
	with open(filePath, 'w') as file:
		file.write(stdin) # write all stdin data to file
	if verbose: # if verbose is true; print file path
		print(filePath)

def getDateTime(form = 0):
	now = datetime.now() # get current date and time
	if form == 0:
		# return formmated date and time (Hour:Minute:Second | Day/Month/Year)
		return now.strftime("%H:%M:%S | %d/%m/%Y")
	elif form == 1:
		# return formmated date and time (Hour-Minute-Second_Day-Month-Year)
		# for using as file name
		return now.strftime("%H-%M-%S_%d-%m-%Y")

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('-n', '--name', type=str, help="output file name")
	parser.add_argument('-p', '--path', type=str, help="output file path")
	parser.add_argument('-v', '--verbose', action='store_true', help="return output file path")
	args = parser.parse_args()

	if args.name:
		# if args.name has value; assign it to 'fileName'
		fileName = args.name
	else:
		# if args.name has no value; assign current date and time to 'fileName'
		fileName = getDateTime(1)

	if args.path:
		# if args.path has value; assign it to 'newDirectory'
		newDirectory = os.path.dirname(args.path)
		# combine direcotry path 'filePath' with 'fileName' to write file
		filePath = os.path.join(newDirectory, f'{fileName}.log')
	else:
		# if args.path has no value; assign current working directory
		currentDirectory = os.getcwd()
		# combine direcotry path 'filePath' with 'fileName' to write file
		filePath = os.path.join(currentDirectory, f'{fileName}.log')

	# write a new log file with all assigned paramaters
	writeFile(filePath, readInput(), args.verbose)