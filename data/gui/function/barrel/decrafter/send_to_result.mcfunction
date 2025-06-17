# say inside
# data modify storage minecraft:ui decraft.output_0 set from storage minecraft:ui decraft.output[0]
# function gui:barrel/decrafter/test_if_in_result with storage minecraft:ui decraft.output_0
# execute if function gui:barrel/decrafter/is_result_empty run say hi
$execute if score decraft_number decraft matches 1 run function gui:utils/give {player:$(player),items:$(output)}
$execute if score decraft_number decraft matches 4 run function gui:utils/give {player:$(player),items:$(output)}
$execute if score decraft_number decraft matches 4 run function gui:utils/give {player:$(player),items:$(output)}
$execute if score decraft_number decraft matches 4 run function gui:utils/give {player:$(player),items:$(output)}
$execute if score decraft_number decraft matches 4 run function gui:utils/give {player:$(player),items:$(output)}
$execute if score decraft_number decraft matches 16 run function gui:utils/give {player:$(player),items:$(output)}
$execute if score decraft_number decraft matches 16 run function gui:utils/give {player:$(player),items:$(output)}
$execute if score decraft_number decraft matches 16 run function gui:utils/give {player:$(player),items:$(output)}
$execute if score decraft_number decraft matches 16 run function gui:utils/give {player:$(player),items:$(output)}
$execute if score decraft_number decraft matches 16 run function gui:utils/give {player:$(player),items:$(output)}
$execute if score decraft_number decraft matches 16 run function gui:utils/give {player:$(player),items:$(output)}
$execute if score decraft_number decraft matches 16 run function gui:utils/give {player:$(player),items:$(output)}
$execute if score decraft_number decraft matches 16 run function gui:utils/give {player:$(player),items:$(output)}
$execute if score decraft_number decraft matches 16 run function gui:utils/give {player:$(player),items:$(output)}
$execute if score decraft_number decraft matches 16 run function gui:utils/give {player:$(player),items:$(output)}
$execute if score decraft_number decraft matches 16 run function gui:utils/give {player:$(player),items:$(output)}
$execute if score decraft_number decraft matches 16 run function gui:utils/give {player:$(player),items:$(output)}
$execute if score decraft_number decraft matches 16 run function gui:utils/give {player:$(player),items:$(output)}
$execute if score decraft_number decraft matches 16 run function gui:utils/give {player:$(player),items:$(output)}
$execute if score decraft_number decraft matches 16 run function gui:utils/give {player:$(player),items:$(output)}
$execute if score decraft_number decraft matches 16 run function gui:utils/give {player:$(player),items:$(output)}


function gui:barrel/refresh