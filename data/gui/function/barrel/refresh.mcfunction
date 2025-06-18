
scoreboard players set sum conditions 0
execute at @s unless items block ~ ~ ~ container.18 * run scoreboard players add sum conditions 1
execute at @s unless items block ~ ~ ~ container.19 * run scoreboard players add sum conditions 1
execute at @s unless items block ~ ~ ~ container.20 * run scoreboard players add sum conditions 1

execute if score sum conditions matches 3 run data modify storage minecraft:ui SelectedItem set value {Slot:1b,id:"minecraft:barrier","components":{"minecraft:custom_data":{ui_item:1,actions:{}}}}
function gui:barrel/decrafter/try_decraft_display


data modify storage minecraft:ui mask set from storage minecraft:ui current
data modify storage minecraft:ui current append from storage minecraft:ui DecraftResult[]
function gui:barrel/decrafter/test_if_1_possible
function gui:barrel/decrafter/test_if_4_possible
function gui:barrel/decrafter/test_if_16_possible
data modify storage minecraft:ui current append from storage minecraft:ui DecraftPossible.one
data modify storage minecraft:ui current append from storage minecraft:ui DecraftPossible.four
data modify storage minecraft:ui current append from storage minecraft:ui DecraftPossible.sixteen
data modify storage minecraft:ui current append from storage minecraft:ui SelectedItem
function gui:barrel/get_mask with entity @s data.page
data modify storage minecraft:ui current append from storage minecraft:ui mask[]

function gui:barrel/load_page