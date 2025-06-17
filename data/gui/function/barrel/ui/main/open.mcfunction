
function gui:barrel/ui/main/get_mask

data modify storage minecraft:ui current append from storage minecraft:ui mask[]
data modify storage minecraft:ui SelectedItem set value {Slot:1b,id:"minecraft:barrier","components":{"minecraft:custom_data":{ui_item:1,actions:{}}}}
data modify storage minecraft:ui current append from storage minecraft:ui SelectedItem
data modify entity @s data.page.mask set value "function gui:barrel/ui/main/mask"
data modify entity @s data.page.name set value "main"

function gui:barrel/load_page