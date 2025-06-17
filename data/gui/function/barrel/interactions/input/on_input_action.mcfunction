# $say Deposit $(selected_item_count)x $(selected_item_id) in $(selected_item_slot) $(selected_item_command) $(selected_item_is_from_ui)

$execute if data entity @s data.action.click.selected_item_command run function gui:utils/cmd {"command":"$(selected_item_command)"}

clear @a *[minecraft:custom_data~{ui_item:1}]
# Block the input of item in the result part
scoreboard players set is_deposit_on_result conditions 0
$function gui:utils/is_equal {"one":"$(selected_item_slot)","two":"6","if":"scoreboard players set is_deposit_on_result conditions 1","else":""}
$function gui:utils/is_equal {"one":"$(selected_item_slot)","two":"7","if":"scoreboard players set is_deposit_on_result conditions 1","else":""}
$function gui:utils/is_equal {"one":"$(selected_item_slot)","two":"8","if":"scoreboard players set is_deposit_on_result conditions 1","else":""}
$function gui:utils/is_equal {"one":"$(selected_item_slot)","two":"15","if":"scoreboard players set is_deposit_on_result conditions 1","else":""}
$function gui:utils/is_equal {"one":"$(selected_item_slot)","two":"16","if":"scoreboard players set is_deposit_on_result conditions 1","else":""}
$function gui:utils/is_equal {"one":"$(selected_item_slot)","two":"17","if":"scoreboard players set is_deposit_on_result conditions 1","else":""}
$function gui:utils/is_equal {"one":"$(selected_item_slot)","two":"24","if":"scoreboard players set is_deposit_on_result conditions 1","else":""}
$function gui:utils/is_equal {"one":"$(selected_item_slot)","two":"25","if":"scoreboard players set is_deposit_on_result conditions 1","else":""}
$function gui:utils/is_equal {"one":"$(selected_item_slot)","two":"26","if":"scoreboard players set is_deposit_on_result conditions 1","else":""}

$execute if score is_deposit_on_result conditions matches 1 run data modify storage minecraft:ui current[{Slot:$(selected_item_slot)b}] set value {}
execute if score is_deposit_on_result conditions matches 1 run function gui:barrel/refresh
$execute if score is_deposit_on_result conditions matches 1 run return run function gui:utils/give_unique {player:$(player),items:[$(selected_item)]}

# Item Selection management
data remove storage minecraft:operation Same
data modify storage minecraft:operation Same set from storage minecraft:ui SelectedItem.id
$execute store success score different conditions run data modify storage minecraft:operation Same set value "$(selected_item_id)"

scoreboard players set is_equal conditions 0
$function gui:utils/is_equal {"one":"$(selected_item_slot)","two":"18","if":"scoreboard players set is_equal conditions 1","else":""}
$function gui:utils/is_equal {"one":"$(selected_item_slot)","two":"19","if":"scoreboard players set is_equal conditions 1","else":""}
$function gui:utils/is_equal {"one":"$(selected_item_slot)","two":"20","if":"scoreboard players set is_equal conditions 1","else":""}

scoreboard players set is_selected_item_empty conditions 0
execute at @s if data block ~ ~ ~ Items[{Slot:1b,id:"minecraft:barrier"}] run scoreboard players set is_selected_item_empty conditions 1

$execute if score is_equal conditions matches 1 if score is_selected_item_empty conditions matches 1 run data modify storage minecraft:ui SelectedItem set value {Slot:1b,id:"$(selected_item_id)","components":{"minecraft:custom_data":{ui_item:1,actions:{}}}}
execute if score is_equal conditions matches 1 if score is_selected_item_empty conditions matches 1 run scoreboard players set SelectedItemCount decraft 1

$execute if score different conditions matches 1 unless score is_selected_item_empty conditions matches 1 run function gui:utils/give_unique {player:$(player),items:[$(selected_item)]}
$execute if score different conditions matches 1 unless score is_selected_item_empty conditions matches 1 run data modify storage minecraft:ui current[{Slot:$(selected_item_slot)b}] set value {}














function gui:barrel/refresh