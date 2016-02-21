
import sys
import argparse
parser = argparse.ArgumentParser()
init = parser.add_argument('--n', type=int)
args = parser.parse_args()
init =  args.n

def merge(subproblems): return sum(subproblems)


# Format of this file
# Base values
# 
# Acc adds or subtracts or whatevers the return values of each of the subproblems
def acc(memo, children):
	mapped = [memo[child] for child in children]
	return merge(mapped)

children = [lambda n: n-1 , lambda n: n-2]

memo = {}
def fBase(curr):
	return curr

def isBase(curr):
	return curr == 0 or curr == 1

s = [] # This is our virtual stack
s.append(init)
while len(s) > 0:
	curr = s.pop()
	if curr in memo:
		continue
	elif (isBase(curr)):
		memo[curr] = fBase(curr)
	else:
		mapped = set([f(curr) for f in children])

		if len(mapped-set(memo.keys())) > 0:
			# Instead of calling functions by adding to the actual stack,
			# we add to the our virtual stack s
			s += [curr] + list(mapped)
			continue
		memo[curr] = acc(memo, mapped)
print(memo[init])
