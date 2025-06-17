data modify entity @s data.action.simult.player set from storage minecraft:ui CurrentPlayerName
data modify entity @s data.action.simult.ui_page set from entity @s data.page.name

$execute at @s run data modify entity @s data.action.simult.selected_item set from block ~ ~ ~ Items[{Slot:$(slot)b}]

data modify entity @s data.action.simult.selected_item_id set from entity @s data.action.simult.selected_item.id
data modify entity @s data.action.simult.selected_item_slot set from entity @s data.action.simult.selected_item.Slot
data modify entity @s data.action.simult.selected_item_count set from entity @s data.action.simult.selected_item.count

data modify entity @s data.action.simult.selected_item_components set value {}
data modify entity @s data.action.simult.selected_item_components set from entity @s data.action.simult.selected_item.components

data modify entity @s data.action.simult.selected_item_is_from_ui set value 0
execute if data entity @s data.action.simult.selected_item_components."minecraft:custom_data".ui_item run data modify entity @s data.action.simult.selected_item_is_from_ui set value 1

data modify entity @s data.action.simult.selected_item_command set value ""
data modify entity @s data.action.simult.selected_item_command set from entity @s data.action.simult.selected_item_components."minecraft:custom_data".actions.on_simult.command



data modify entity @s data.action.simult.clicked_item set from storage operation match.temp

data modify entity @s data.action.simult.clicked_item_id set from entity @s data.action.simult.clicked_item.id
data modify entity @s data.action.simult.clicked_item_slot set from entity @s data.action.simult.clicked_item.Slot
data modify entity @s data.action.simult.clicked_item_count set from entity @s data.action.simult.clicked_item.count

data modify entity @s data.action.simult.clicked_item_components set value {}
data modify entity @s data.action.simult.clicked_item_components set from entity @s data.action.simult.clicked_item.components

data modify entity @s data.action.simult.clicked_item_is_from_ui set value 0
execute if data entity @s data.action.simult.clicked_item_components."minecraft:custom_data".ui_item run data modify entity @s data.action.simult.clicked_item_is_from_ui set value 1

data modify entity @s data.action.simult.clicked_item_command set value {}
data modify entity @s data.action.simult.clicked_item_command set from entity @s data.action.simult.clicked_item_components."minecraft:custom_data".actions.on_simult.command
function gui:barrel/interactions/simult/on_simult_action with entity @s data.action.simult


function gui:barrel/refresh