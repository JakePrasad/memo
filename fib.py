init = parser.add_argument('--n', type=int)
args = parser.parse_args()
init =  args.n
___
def isBase(curr):
	return curr == 0 or curr == 1
___
def fBase(curr):
	return curr
___
lambda n: n-1 
lambda n: n-2
___
def merge(subproblems): return sum(subproblems)


# Format of this file
# Base values
# ___
# Subproblems - n is the current number
# ___
# Function to merge the subproblems together