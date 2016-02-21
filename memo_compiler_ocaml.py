# To run this file, run
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
children = "; ".join(lambdas)
merge = info[4]
output = info[5]
toWrite = '''
''' + init + '''
''' + merge + '''
(* Acc adds or subtracts or whatevers the return values of each of the subproblems*)
let acc (memo,children) =
	let f child =
		(Hashtbl.find memo child)
	in
	merge (List.map f children)
;;

let rec mapFunctions fl a =
	match fl with
	| h::t ->
		(h a)::(mapFunctions t a)
	| [] ->
		[]
;;

let rec isContained l memo =
	match l with
	| h::t ->
		if Hashtbl.mem memo h then
			isContained t memo
		else
			false
	| [] ->
		true
;;

let rec addAll l s =
	match l with
	| h::t ->
		let add = Stack.push h s in
		addAll t s
	| [] ->
		s
;;

''' + base + '''
''' + isBase + '''

let children = [''' + children + '''];;
let memo = Hashtbl.create 44;;

let s = Stack.create();; (*This is our virtual stack*)
Stack.push init s;; 

while (not (Stack.is_empty s)) do
	let curr = Stack.pop s in
	if ((Hashtbl.mem memo curr) == false) then (
		if isBase curr then
			let insertBase = Hashtbl.add memo curr ( (fBase curr)) in
			()
		else
			let mapped = mapFunctions children curr in
			(* If the subproblems are not already in memo... *)
			if isContained mapped memo then
				let insertCurr = Hashtbl.add memo curr ( (acc (memo,mapped))) in
				()
			else
				(* Instead of calling functions by adding to the actual stack,
				# we add to the our virtual stack s *)
				let addCurr = Stack.push curr s in
				let addMapped = addAll mapped s in
				()
	) else
		()
	
done;;
Printf.printf "''' + output + '''" (Hashtbl.find memo init);;
print_newline();;
'''

text_file = open(sys.argv[2], "w")
text_file.write(toWrite)
text_file.close()