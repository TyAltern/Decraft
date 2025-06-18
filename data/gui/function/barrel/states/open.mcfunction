data modify entity @s data.open set value 1

execute as @a[scores={last_player_open_barrel=1}] run data modify storage minecraft:ui CurrentPlayer set from entity @s 
execute as @a[scores={last_player_open_barrel=1}] run function gui:utils/get_player_name
execute as @a[scores={last_player_open_barrel=1}] run data modify storage minecraft:ui CurrentPlayerName set from storage minecraft:utils get_player_name.out
# execute if score TyAlternative open_barrel matches 1 run say hi
# say Open GUI

function gui:barrel/refresh