-module(ift).
-export([ift/2]).

ift(l,h) -> ift_help(l,[h-1]).

ift_help(0, list) -> list;
ift_help(l, [H|T]) -> ift_help(l-1, [H-1] ++ [H] ++ T).
