let init = 500000;;
___
let isBase curr =
	curr == 0 || curr == 1
;;
___
let fBase curr =
	curr
;;
___
(fun n -> n - 1)
(fun n -> n - 2)
___
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
___
%d