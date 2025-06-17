execute if entity @s[tag=positionate_gui] run function gui:barrel/states/place
execute at @s unless block ~ ~ ~ minecraft:barrel run function gui:barrel/states/break
execute at @s if block ~ ~ ~ minecraft:barrel[open=true] if entity @s[nbt={data:{open:0}}] run function gui:barrel/states/open 
execute at @s if block ~ ~ ~ minecraft:barrel[open=false] if entity @s[nbt={data:{open:1}}] run function gui:barrel/states/close 

data modify storage minecraft:ui previous set from entity @s data.previous
execute at @s run data modify storage minecraft:ui current set from block ~ ~ ~ Items

execute store result score #bool gui run data modify entity @s data.previous set from storage minecraft:ui current

execute if score #bool gui matches 1 run function gui:barrel/interactions/on_change with storage minecraft:ui

# data modify storage minecraft:ui SwapHandDetection.ItemMemory set from storage minecraft:ui CurrentPlayer.equipment.offhand
