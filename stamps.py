parser.add_argument('--amt', type=int)
parser.add_argument('--stamps', type=str)
args = parser.parse_args()
init = (int(args.amt), tuple([int(x) for x in args.stamps.split(',')])) # ['1','2','3','4']
___
def isBase(curr):
	amt = curr[0]
	stamps = curr[1]
	return amt <= 0 or len(stamps) == 0
___
def fBase(curr):
	amt = curr[0]
	if (amt == 0):
		return 0
	return sys.maxsize
___
lambda curr: (curr[0]-curr[1][-1],  curr[1])
lambda curr: (curr[0], tuple(list(curr[1])[:-1]))
___
def merge(subproblems):
	if(subproblems[0] < subproblems[1]):
		return subproblems[0]+1
	return subproblems[1]