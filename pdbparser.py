from __future__ import print_function
from sys import argv 
import re

#taking in arguments and assigning them to i
i = argv

#making filenames
inputFileName = i[1]
outputFileName =inputFileName[:-3] + "xyz"
userInput = raw_input("Output file is set to %r. Type another file name to change. > " %outputFileName)
if len(userInput) > 1: # and userInput[-4:] == ".xyz":
  outputFileName = userInput
  if userInput[-4:] != ".xyz":
    outputFileName = outputFileName + ".xyz"
    print ("changed to ", outputFileName)

#opening files for read/write
f = open(inputFileName, 'r')
g = open(outputFileName, 'w')

#display sugar
print ('Reading:', inputFileName)
print ('Writing to: ', outputFileName)
print ( len(i)-2, "arguments taken in" )


#Adding file name and arguments-taken-in as comment
g.write(i[1] + " ")
g.write("Arguments: ")
for argument in i[2:]:
  g.write(argument + " ")
g.write('\n')

#Finding parameters in file
lineCount = 0
for argument in i[2:]:
  print ("Searching for ", argument, "...")
  f.seek(0) #Reset to beginning of file
  #searching file for provided arguments and writing to outputFileName
  for line in f:
    for argument in i[2:]:
      searchterm = "ATOM" + " "*(7-len(argument)) + argument
      if line.find(searchterm) != -1:
        #regular expression to populate the xyz syntax
        mainData = re.search(r'-?\d+\.\d+\s+-?\d+\.\d+\s+-?\d+\.\d+\s+', line)
        letter = re.search(r'(\w+\s)\s*$', line)
        lineToWrite = letter.group(1) + mainData.group() + "\n"
        g.write(lineToWrite)
        lineCount = lineCount + 1

#Prepending header text (number of atoms found) to destination file
g.close()
g = open(outputFileName, 'r')
temp = g.read()
g.close()
g = open(outputFileName, 'w')
g.write(str(lineCount) + '\n')
g.write(temp)

