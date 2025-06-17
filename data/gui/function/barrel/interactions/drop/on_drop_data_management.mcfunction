data modify entity @s data.action.drop.player set from storage minecraft:ui CurrentPlayerName
data modify entity @s data.action.drop.ui_page set from entity @s data.page.name

execute if data storage minecraft:ui temporary[0] run data modify entity @s data.action.drop.selected_item set from storage minecraft:ui temporary[0]
execute unless data storage minecraft:ui temporary[0] run data modify entity @s data.action.drop.selected_item set from storage minecraft:ui temporary

data modify entity @s data.action.drop.selected_item_id set from entity @s data.action.drop.selected_item.id
data modify entity @s data.action.drop.selected_item_slot set from entity @s data.action.drop.selected_item.Slot
data modify entity @s data.action.drop.selected_item_count set from entity @s data.action.drop.selected_item.count

data modify entity @s data.action.drop.selected_item_components set value {}
data modify entity @s data.action.drop.selected_item_components set from entity @s data.action.drop.selected_item.components

data modify entity @s data.action.drop.selected_item_is_from_ui set value 0
execute if data entity @s data.action.drop.selected_item_components."minecraft:custom_data".ui_item run data modify entity @s data.action.drop.selected_item_is_from_ui set value 1

data modify entity @s data.action.drop.selected_item_command set value ""
data modify entity @s data.action.drop.selected_item_command set from entity @s data.action.drop.selected_item_components."minecraft:custom_data".actions.on_drop.command

function gui:barrel/interactions/drop/on_drop_action with entity @s data.action.drop