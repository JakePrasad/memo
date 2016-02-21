
import sys
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--amt', type=int)
parser.add_argument('--stamps', type=str)
args = parser.parse_args()
init = (int(args.amt), tuple([int(x) for x in args.stamps.split(',')])) # ['1','2','3','4']

def merge(subproblems):
	if(subproblems[0] < subproblems[1]):
		return subproblems[0]+1
	return subproblems[1]
# Acc adds or subtracts or whatevers the return values of each of the subproblems
def acc(memo, children):
	mapped = [memo[child] for child in children]
	return merge(mapped)

children = [lambda curr: (curr[0]-curr[1][-1],  curr[1]), lambda curr: (curr[0], tuple(list(curr[1])[:-1]))]

memo = {}
def fBase(curr):
	amt = curr[0]
	if (amt == 0):
		return 0
	return sys.maxsize

def isBase(curr):
	amt = curr[0]
	stamps = curr[1]
	return amt <= 0 or len(stamps) == 0

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
