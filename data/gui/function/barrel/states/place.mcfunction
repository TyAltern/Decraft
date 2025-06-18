execute at @s run setblock ~ ~ ~ minecraft:barrel[facing=up]
data modify entity @s data.open set value 0
data modify storage minecraft:ui current set value []
# say GUI placed

function gui:barrel/ui/main/open


tag @s remove positionate_gui