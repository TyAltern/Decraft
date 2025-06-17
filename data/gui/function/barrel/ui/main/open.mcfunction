
function gui:barrel/ui/main/get_mask

data modify storage minecraft:ui current append from storage minecraft:ui mask[]
data modify storage minecraft:ui SelectedItem set value {Slot:1b,id:"minecraft:barrier","components":{"minecraft:custom_data":{ui_item:1,actions:{}}}}
data modify storage minecraft:ui DecraftPossible.one set value {Slot:4b,id:"minecraft:red_stained_glass_pane", components: {"minecraft:custom_name":{italic:0b, text:"Not enough item", bold:1b, color:"red"},"minecraft:custom_data":{ui_item:1,actions:{}}}}
data modify storage minecraft:ui DecraftPossible.four set value {Slot:13b, count:4,id:"minecraft:red_stained_glass_pane", components: {"minecraft:custom_name":{italic:0b, text:"Not enough item", bold:1b, color:"red"},"minecraft:custom_data":{ui_item:1,actions:{}}}}
data modify storage minecraft:ui DecraftPossible.sixteen set value {Slot:22b, count:16,id:"minecraft:red_stained_glass_pane", components: {"minecraft:custom_name":{italic:0b, text:"Not enough item", bold:1b, color:"red"},"minecraft:custom_data":{ui_item:1,actions:{}}}}
data modify storage minecraft:ui DecraftResult set value []
data modify storage minecraft:ui DecraftResult append value {Slot:6b,id:"minecraft:light_gray_stained_glass_pane","components":{"minecraft:tooltip_display":{hide_tooltip:1b},"minecraft:custom_data":{ui_item:1,actions:{}}}}
data modify storage minecraft:ui DecraftResult append value {Slot:7b,id:"minecraft:light_gray_stained_glass_pane","components":{"minecraft:tooltip_display":{hide_tooltip:1b},"minecraft:custom_data":{ui_item:1,actions:{}}}}
data modify storage minecraft:ui DecraftResult append value {Slot:8b,id:"minecraft:light_gray_stained_glass_pane","components":{"minecraft:tooltip_display":{hide_tooltip:1b},"minecraft:custom_data":{ui_item:1,actions:{}}}}
data modify storage minecraft:ui DecraftResult append value {Slot:15b,id:"minecraft:light_gray_stained_glass_pane","components":{"minecraft:tooltip_display":{hide_tooltip:1b},"minecraft:custom_data":{ui_item:1,actions:{}}}}
data modify storage minecraft:ui DecraftResult append value {Slot:16b,id:"minecraft:light_gray_stained_glass_pane","components":{"minecraft:tooltip_display":{hide_tooltip:1b},"minecraft:custom_data":{ui_item:1,actions:{}}}}
data modify storage minecraft:ui DecraftResult append value {Slot:17b,id:"minecraft:light_gray_stained_glass_pane","components":{"minecraft:tooltip_display":{hide_tooltip:1b},"minecraft:custom_data":{ui_item:1,actions:{}}}}
data modify storage minecraft:ui DecraftResult append value {Slot:24b,id:"minecraft:light_gray_stained_glass_pane","components":{"minecraft:tooltip_display":{hide_tooltip:1b},"minecraft:custom_data":{ui_item:1,actions:{}}}}
data modify storage minecraft:ui DecraftResult append value {Slot:25b,id:"minecraft:light_gray_stained_glass_pane","components":{"minecraft:tooltip_display":{hide_tooltip:1b},"minecraft:custom_data":{ui_item:1,actions:{}}}}
data modify storage minecraft:ui DecraftResult append value {Slot:26b,id:"minecraft:light_gray_stained_glass_pane","components":{"minecraft:tooltip_display":{hide_tooltip:1b},"minecraft:custom_data":{ui_item:1,actions:{}}}}
data modify storage minecraft:ui current append from storage minecraft:ui SelectedItem
data modify storage minecraft:ui current append from storage minecraft:ui DecraftPossible.one
data modify storage minecraft:ui current append from storage minecraft:ui DecraftPossible.four
data modify storage minecraft:ui current append from storage minecraft:ui DecraftPossible.sixteen
data modify storage minecraft:ui current append from storage minecraft:ui DecraftResult[]
data modify entity @s data.page.mask set value "function gui:barrel/ui/main/mask"
data modify entity @s data.page.name set value "main"

function gui:barrel/refresh