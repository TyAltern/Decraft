data modify storage minecraft:ui DecraftResult[0] set value {Slot:6b,id:"minecraft:light_gray_stained_glass_pane","components":{"minecraft:tooltip_display":{hide_tooltip:1b},"minecraft:custom_data":{ui_item:1,actions:{}}}}
data modify storage minecraft:ui DecraftResult[1] set value {Slot:7b,id:"minecraft:light_gray_stained_glass_pane","components":{"minecraft:tooltip_display":{hide_tooltip:1b},"minecraft:custom_data":{ui_item:1,actions:{}}}}
data modify storage minecraft:ui DecraftResult[2] set value {Slot:8b,id:"minecraft:light_gray_stained_glass_pane","components":{"minecraft:tooltip_display":{hide_tooltip:1b},"minecraft:custom_data":{ui_item:1,actions:{}}}}
data modify storage minecraft:ui DecraftResult[3] set value {Slot:15b,id:"minecraft:light_gray_stained_glass_pane","components":{"minecraft:tooltip_display":{hide_tooltip:1b},"minecraft:custom_data":{ui_item:1,actions:{}}}}
data modify storage minecraft:ui DecraftResult[4] set value {Slot:16b,id:"minecraft:light_gray_stained_glass_pane","components":{"minecraft:tooltip_display":{hide_tooltip:1b},"minecraft:custom_data":{ui_item:1,actions:{}}}}
data modify storage minecraft:ui DecraftResult[5] set value {Slot:17b,id:"minecraft:light_gray_stained_glass_pane","components":{"minecraft:tooltip_display":{hide_tooltip:1b},"minecraft:custom_data":{ui_item:1,actions:{}}}}
data modify storage minecraft:ui DecraftResult[6] set value {Slot:24b,id:"minecraft:light_gray_stained_glass_pane","components":{"minecraft:tooltip_display":{hide_tooltip:1b},"minecraft:custom_data":{ui_item:1,actions:{}}}}
data modify storage minecraft:ui DecraftResult[7] set value {Slot:25b,id:"minecraft:light_gray_stained_glass_pane","components":{"minecraft:tooltip_display":{hide_tooltip:1b},"minecraft:custom_data":{ui_item:1,actions:{}}}}
data modify storage minecraft:ui DecraftResult[8] set value {Slot:26b,id:"minecraft:light_gray_stained_glass_pane","components":{"minecraft:tooltip_display":{hide_tooltip:1b},"minecraft:custom_data":{ui_item:1,actions:{}}}}

data modify storage minecraft:ui SelectedItemCustomData.id set string storage minecraft:ui SelectedItem.id 10
data modify storage minecraft:ui SelectedItemCustomData.count set from storage minecraft:ui SelectedItem.count
function gui:barrel/decrafter/call_try_display with storage minecraft:ui SelectedItemCustomData
