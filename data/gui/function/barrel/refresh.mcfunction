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