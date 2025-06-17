data modify storage minecraft:ui mask set from storage minecraft:ui current
function gui:barrel/get_mask with entity @s data.page
data modify storage minecraft:ui current append from storage minecraft:ui SelectedItem
data modify storage minecraft:ui current append from storage minecraft:ui mask[]

function gui:barrel/load_page