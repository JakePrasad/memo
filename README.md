# memo

Two versions of the code - one in Python and one in OCaml

## Python

### Usage

#### Fib

python memo_compiler.py fib.py memo.py

python memo.py --n 7

#### Stamps

python memo_compiler.py stamps.py memo.py
python memo.py --amt 13 --stamps 1,12

### fib.py/stamps.py

#### Format

initialization instructions

\___

How to check for base case

\___

What to do if we encounter a base case

\___

The subproblems (separated by new lines)

\___

How to merge the subproblems together



## Ocaml

The ocaml version is used for comparing performance with C++

### Usage

python memo\_compiler_ocaml.py fib.ml memo.ml

ocaml memo.ml 7

### fib.ml

Format of the file extends fib.py by adding the type of the output at the end