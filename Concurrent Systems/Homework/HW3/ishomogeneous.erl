-module(test2).
-export([is_homogeneous/1]).

is_homogeneous([]) -> true;
is_homogeneous([H|T]) -> is_homogeneous(H,T).

is_homogeneous(H,[H|T]) -> true and is_homogeneous(H,T);
is_homogeneous(_,[_|_]) -> false;
is_homogeneous(_, []) -> true.
