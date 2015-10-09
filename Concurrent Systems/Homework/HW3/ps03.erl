%% ps03.erl
%% Alexander Gould
%% COMP50CP - Mark Sheldon

-module(ps03).
-export([is_homogeneous/1, get_roots/3]).

is_homogeneous([]) -> true;
is_homogeneous([H|T]) -> is_homogeneous(H,T).

is_homogeneous(H,[H|T]) -> true and is_homogeneous(H,T);
is_homogeneous(_,[_|_]) -> false;
is_homogeneous(_, []) -> true.

%%%%%%%%%

get_roots(0,_,_) -> error;
get_roots(A,B,C) -> get_roots_help(A, B, B*B-4*A*C).

get_roots_help(A,B,0) -> [-B/(2*A)];
get_roots_help(A,B,D) when D > 0 ->
    S = math:sqrt(D),
    [(-B+S)/(2*A),(-B-S)/(2*A)];
get_roots_help(_,_,_) -> [].
