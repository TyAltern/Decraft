
# $say $(selected_item_count)x $(selected_item_id) in $(selected_item_slot) $(selected_item_is_from_ui)
# $say $(clicked_item_count)x $(clicked_item_id) in $(clicked_item_slot) $(clicked_item_is_from_ui)

$function gui:utils/is_equal {"one":"$(clicked_item_is_from_ui)","two":"1","if":"data modify storage minecraft:operation result set value true","else":"data remove storage minecraft:operation result"}
# $say $(selected_item)
data modify storage minecraft:utils give.player set from storage minecraft:ui CurrentPlayerName
$data modify storage minecraft:utils give.items set value [$(selected_item)]
execute if data storage minecraft:operation result run function gui:utils/give_unique with storage minecraft:utils give

$execute if data entity @s data.action.click.selected_item_command run function gui:utils/cmd {"command":"$(selected_item_command)"}
$execute if data entity @s data.action.click.clicked_item_command run function gui:utils/cmd {"command":"$(clicked_item_command)"}

scoreboard players set is_equal conditions 0
$function gui:utils/is_equal {"one":"$(selected_item_slot)","two":"18","if":"scoreboard players set is_equal conditions 1","else":""}
$function gui:utils/is_equal {"one":"$(selected_item_slot)","two":"19","if":"scoreboard players set is_equal conditions 1","else":""}
$function gui:utils/is_equal {"one":"$(selected_item_slot)","two":"20","if":"scoreboard players set is_equal conditions 1","else":""}

$execute if score is_equal conditions matches 1 run function gui:utils/is_equal {"one":"'$(selected_item_id)'","two":"'$(clicked_item_id)'","if":"","else":"function gui:barrel/decrafter/interactions/simult_in_storage with entity @s data.action.simult"}



clear @a *[minecraft:custom_data~{ui_item:1}]

