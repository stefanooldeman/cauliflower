import argparse
from cauliflower.service.cargo import CargoService


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
name = raw_input("Pattern Name: ")
problem = multi_input("Add the problem description for {pattern_name} . \
        Type Q to end input.".format(pattern_name=s1))
solution = multi_input("Describe the solution {pattern_name} is solving. \
        Type Q to end input.".format(pattern_name=s1))
consequence = multi_input("Describe the consequence of using {pattern_name}. \
        Type Q to end input.".format(pattern_name=s1))
