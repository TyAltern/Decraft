$execute if data entity @s data.action.click.selected_item.components."minecraft:custom_data".actions.on_shift_click.command unless items entity $(player) player.cursor * run return run function gui:barrel/interactions/shift_click/on_shift_click_data_management


# $say Click on $(selected_item_count)x $(selected_item_id) in $(selected_item_slot) $(selected_item_command) $(selected_item_is_from_ui)

$execute if data entity @s data.action.click.selected_item_command run function gui:utils/cmd {"command":"$(selected_item_command)"}

clear @a *[minecraft:custom_data~{ui_item:1}]


scoreboard players set sum conditions 0
execute at @s unless items block ~ ~ ~ container.18 * run scoreboard players add sum conditions 1
execute at @s unless items block ~ ~ ~ container.19 * run scoreboard players add sum conditions 1
execute at @s unless items block ~ ~ ~ container.20 * run scoreboard players add sum conditions 1

execute if score sum conditions matches 3 run data modify storage minecraft:ui SelectedItem set value {Slot:1b,id:"minecraft:barrier","components":{"minecraft:custom_data":{ui_item:1,actions:{}}}}
execute if score sum conditions matches 3 run scoreboard players set SelectedItemCount decraft 0




function gui:barrel/refresh