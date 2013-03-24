import argparse

def multi_input(msg):
	print msg
	text = ""
	stopword = "Q"
	while True:
		line = raw_input()
		if line.strip() == stopword:
			break
		text += "%s\n" % line
	return text

print "We are going to add a Pattern!"
#Pattern name 
s1 = raw_input ("Please add Pattern Name: ")
print "The " ,s1, " Pattern has been added!"
#Pattern definition
s2 = multi_input("Please add the {pattern_name} problem description. Type Q to end input.".format(pattern_name=s1))
print "You added the following problem discription to the " +s1+ " Pattern:\n" + s2
#Where to use the pattern
s3 = multi_input("Please describe the solution {pattern_name} is solving. Type Q to end input.".format(pattern_name=s1))
print s3
#
s3 = multi_input("Please describe the solution {pattern_name} is solving. Type Q to end input.".format(pattern_name=s1))
print s3