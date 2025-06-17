execute at @s run data modify block ~ ~ ~ Items set from storage minecraft:ui current
execute at @s run data modify storage minecraft:ui current set from block ~ ~ ~ Items
data modify entity @s data.previous set from storage minecraft:ui current