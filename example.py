"""
create a text file with word on a number of lines
1. open the text file and print out 'f.read()'. What does it look like?
2. use a for loop to print out each line individually. 'for line in f:'
3. print our words only with "m", or some other specific letter.
"""

# with open("Some_file.txt", 'r') as f:
#	print(f.read())


#2 

#with open("Some_file.txt", 'r') as f:
#	for line in f:
#		print(line)


#3 to print the line it will give skip another line for each word

#4 with open("Some_file.txt", 'r') as f:
#	for line in f:
#		print(line.strip())

#4 print words only with m

#with open("Some_file.txt", 'r') as f:
#	for line in f:
#		if line.startswith("m"):
#			print(line.strip()) 

#5 to check for both upper case and lower case letter

#with open("Some_file.txt", 'r') as f:
#	for line in f:
#		if line.lower().startswith("m"):
#			print(line.strip()) 

