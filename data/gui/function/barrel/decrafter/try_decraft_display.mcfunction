data modify storage minecraft:ui DecraftResult[0] set value {Slot:6b,id:"minecraft:light_gray_stained_glass_pane","components":{"minecraft:tooltip_display":{hide_tooltip:1b},"minecraft:custom_data":{ui_item:1,actions:{}}}}
data modify storage minecraft:ui DecraftResult[1] set value {Slot:7b,id:"minecraft:light_gray_stained_glass_pane","components":{"minecraft:tooltip_display":{hide_tooltip:1b},"minecraft:custom_data":{ui_item:1,actions:{}}}}
data modify storage minecraft:ui DecraftResult[2] set value {Slot:8b,id:"minecraft:light_gray_stained_glass_pane","components":{"minecraft:tooltip_display":{hide_tooltip:1b},"minecraft:custom_data":{ui_item:1,actions:{}}}}
data modify storage minecraft:ui DecraftResult[3] set value {Slot:15b,id:"minecraft:light_gray_stained_glass_pane","components":{"minecraft:tooltip_display":{hide_tooltip:1b},"minecraft:custom_data":{ui_item:1,actions:{}}}}
data modify storage minecraft:ui DecraftResult[4] set value {Slot:16b,id:"minecraft:light_gray_stained_glass_pane","components":{"minecraft:tooltip_display":{hide_tooltip:1b},"minecraft:custom_data":{ui_item:1,actions:{}}}}
data modify storage minecraft:ui DecraftResult[5] set value {Slot:17b,id:"minecraft:light_gray_stained_glass_pane","components":{"minecraft:tooltip_display":{hide_tooltip:1b},"minecraft:custom_data":{ui_item:1,actions:{}}}}
data modify storage minecraft:ui DecraftResult[6] set value {Slot:24b,id:"minecraft:light_gray_stained_glass_pane","components":{"minecraft:tooltip_display":{hide_tooltip:1b},"minecraft:custom_data":{ui_item:1,actions:{}}}}
data modify storage minecraft:ui DecraftResult[7] set value {Slot:25b,id:"minecraft:light_gray_stained_glass_pane","components":{"minecraft:tooltip_display":{hide_tooltip:1b},"minecraft:custom_data":{ui_item:1,actions:{}}}}
data modify storage minecraft:ui DecraftResult[8] set value {Slot:26b,id:"minecraft:light_gray_stained_glass_pane","components":{"minecraft:tooltip_display":{hide_tooltip:1b},"minecraft:custom_data":{ui_item:1,actions:{}}}}

execute at @s if data block ~ ~ ~ Items[{Slot:1b,id:"minecraft:oak_fence",count:3}] run return run function gui:barrel/decrafter/decraft_recipes/oak_fence_display
return 0