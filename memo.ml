
let init = (int_of_string(Sys.argv.(1)));;

let rec sum l =
	match l with
	| h::t ->
		h + (sum t)
	| [] ->
		0
;;
let merge subproblems = 
	sum subproblems
;;
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

let fBase curr =
	curr
;;

let isBase curr =
	curr == 0 || curr == 1
;;


let children = [(fun n -> n - 1); (fun n -> n - 2)];;
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
Printf.printf "%d" (Hashtbl.find memo init);;
print_newline();;
