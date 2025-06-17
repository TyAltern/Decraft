$execute if data entity @s data.action.click.selected_item.components."minecraft:custom_data".actions.on_shift_click.command unless items entity $(player) player.cursor * run return run function gui:barrel/interactions/shift_click/on_shift_click_data_management


# $say Click on $(selected_item_count)x $(selected_item_id) in $(selected_item_slot) $(selected_item_command) $(selected_item_is_from_ui)

$execute if data entity @s data.action.click.selected_item_command run function gui:utils/cmd {"command":"$(selected_item_command)"}

clear @a *[minecraft:custom_data~{ui_item:1}]


scoreboard players set sum conditions 0
execute at @s unless items block ~ ~ ~ container.18 * run scoreboard players add sum conditions 1
execute at @s unless items block ~ ~ ~ container.19 * run scoreboard players add sum conditions 1
execute at @s unless items block ~ ~ ~ container.20 * run scoreboard players add sum conditions 1

execute if score sum conditions matches 3 run data modify storage minecraft:ui SelectedItem set value {Slot:1b,id:"minecraft:barrier","components":{"minecraft:custom_data":{ui_item:1,actions:{}}}}

function gui:barrel/refresh

execute if score sum conditions matches 3 run data modify storage minecraft:ui DecraftResult[0] set value {Slot:6b,id:"minecraft:light_gray_stained_glass_pane","components":{"minecraft:tooltip_display":{hide_tooltip:1b},"minecraft:custom_data":{ui_item:1,actions:{}}}}
execute if score sum conditions matches 3 run data modify storage minecraft:ui DecraftResult[1] set value {Slot:7b,id:"minecraft:light_gray_stained_glass_pane","components":{"minecraft:tooltip_display":{hide_tooltip:1b},"minecraft:custom_data":{ui_item:1,actions:{}}}}
execute if score sum conditions matches 3 run data modify storage minecraft:ui DecraftResult[2] set value {Slot:8b,id:"minecraft:light_gray_stained_glass_pane","components":{"minecraft:tooltip_display":{hide_tooltip:1b},"minecraft:custom_data":{ui_item:1,actions:{}}}}
execute if score sum conditions matches 3 run data modify storage minecraft:ui DecraftResult[3] set value {Slot:15b,id:"minecraft:light_gray_stained_glass_pane","components":{"minecraft:tooltip_display":{hide_tooltip:1b},"minecraft:custom_data":{ui_item:1,actions:{}}}}
execute if score sum conditions matches 3 run data modify storage minecraft:ui DecraftResult[4] set value {Slot:16b,id:"minecraft:light_gray_stained_glass_pane","components":{"minecraft:tooltip_display":{hide_tooltip:1b},"minecraft:custom_data":{ui_item:1,actions:{}}}}
execute if score sum conditions matches 3 run data modify storage minecraft:ui DecraftResult[5] set value {Slot:17b,id:"minecraft:light_gray_stained_glass_pane","components":{"minecraft:tooltip_display":{hide_tooltip:1b},"minecraft:custom_data":{ui_item:1,actions:{}}}}
execute if score sum conditions matches 3 run data modify storage minecraft:ui DecraftResult[6] set value {Slot:24b,id:"minecraft:light_gray_stained_glass_pane","components":{"minecraft:tooltip_display":{hide_tooltip:1b},"minecraft:custom_data":{ui_item:1,actions:{}}}}
execute if score sum conditions matches 3 run data modify storage minecraft:ui DecraftResult[7] set value {Slot:25b,id:"minecraft:light_gray_stained_glass_pane","components":{"minecraft:tooltip_display":{hide_tooltip:1b},"minecraft:custom_data":{ui_item:1,actions:{}}}}
execute if score sum conditions matches 3 run data modify storage minecraft:ui DecraftResult[8] set value {Slot:26b,id:"minecraft:light_gray_stained_glass_pane","components":{"minecraft:tooltip_display":{hide_tooltip:1b},"minecraft:custom_data":{ui_item:1,actions:{}}}}
execute if score sum conditions matches 3 run scoreboard players set SelectedItemCount decraft 0



function gui:barrel/refresh