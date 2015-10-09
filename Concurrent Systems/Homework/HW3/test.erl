-module(test).
-export([my_length/1]).

my_length([]) -> 0;
my_length([_H | T]) -> 1 + my_length(T).

