%% db.erl
%% Alexander Gould
%% COMP50CP - Mark Sheldon

-module(db).
-export([]).

new() -> [].
destroy(Db) -> [].
write(Key, Element, Db) -> [{Key, Element} | Db].
delete(Key, Db) ->
