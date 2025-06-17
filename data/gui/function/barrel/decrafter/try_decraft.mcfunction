data modify storage minecraft:ui decraft.player set from storage minecraft:ui CurrentPlayerName

execute at @s if data block ~ ~ ~ Items[{Slot:1b,id:"minecraft:oak_fence",count:3}] run return run function gui:barrel/decrafter/decraft_recipes/oak_fence


return 0