%% db.erl
%% Alexander Gould
%% COMP50CP - Mark Sheldon

-module(db).
-export([new/0, destroy/1, write/3, delete/2, read/2, match/2]).

new() -> [].

destroy(_) -> [].

write(Key, Element, Db) -> [{Key, Element} | Db].

delete(Key, Db) -> delete(Key,Db,[]).
delete(K2,[H|T],R) -> {K,_} = H,
if K2 == K -> delete(K,T,R); true -> delete(K,T,[H|R]) end;
delete(_,_,R) -> R.

read(Key, [H|T]) -> {K,V} = H,
if Key == K -> {ok, V}; true -> read(Key, T) end;
read(_, []) -> {error, instance}.

match(Element, Db) -> match(Element,Db,[]).
match(E,[H|T],R) -> {K,V} = H,
if V == E -> match(E, T, [K|R]); true -> match(E,T,R) end;
match(_,_,R) -> R.
