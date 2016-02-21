# To run this file, simply run
# python dp_compiler.py FILE_NAME
# at the terminal
# e.g. python dp_compiler dp.py

# To run the created dp file, run
# python dp.py INPUT
# e.g. python dp.py 100

import sys
with open(sys.argv[1]) as f:
	content = f.read()
info = content.split("___")
init = info[0]
isBase = info[1]
info = [x.strip("\n") for x in info]
base = info[2]

children = info[3]
lambdas = children.split("\n")
children = ", ".join(lambdas)

toWrite = '''
import sys
import argparse
parser = argparse.ArgumentParser()
''' + init + '''
''' + info[4] + '''
# Acc adds or subtracts or whatevers the return values of each of the subproblems
def acc(memo, children):
	mapped = [memo[child] for child in children]
	return merge(mapped)

children = [''' + children + ''']

memo = {}
''' + base + '''
''' + isBase + '''
s = [] # This is our virtual stack
s.append(init)
while len(s) > 0:
	curr = s.pop()
	if curr in memo:
		continue
	elif (isBase(curr)):
		memo[curr] = fBase(curr)
	else:
		mapped = ([f(curr) for f in children])
		mappedSet = set(mapped)
		if len(mappedSet-set(memo.keys())) > 0:
			# Instead of calling functions by adding to the actual stack,
			# we add to the our virtual stack s
			s += [curr] + mapped
			continue
		memo[curr] = acc(memo, mapped)
print(memo[init])
'''

text_file = open(sys.argv[2], "w")
text_file.write(toWrite)
text_file.close()