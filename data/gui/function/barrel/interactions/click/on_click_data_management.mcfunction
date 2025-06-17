data modify entity @s data.action.click.player set from storage minecraft:ui CurrentPlayerName
data modify entity @s data.action.click.ui_page set from entity @s data.page.name

data modify entity @s data.action.click.selected_item set from storage minecraft:ui temporary[0]
data modify entity @s data.action.click.selected_item_id set from entity @s data.action.click.selected_item.id
data modify entity @s data.action.click.selected_item_slot set from entity @s data.action.click.selected_item.Slot
data modify entity @s data.action.click.selected_item_count set from entity @s data.action.click.selected_item.count
data modify entity @s data.action.click.selected_item_components set value {}
data modify entity @s data.action.click.selected_item_components set from entity @s data.action.click.selected_item.components
data modify entity @s data.action.click.selected_item_is_from_ui set value 0
execute if data entity @s data.action.click.selected_item_components."minecraft:custom_data".ui_item run data modify entity @s data.action.click.selected_item_is_from_ui set value 1
data modify entity @s data.action.click.selected_item_command set value ""
data modify entity @s data.action.click.selected_item_command set from entity @s data.action.click.selected_item_components."minecraft:custom_data".actions.on_click.command
data modify entity @s data.action.click.selected_item_shift_command set value ""
data modify entity @s data.action.click.selected_item_shift_command set from entity @s data.action.click.selected_item_components."minecraft:custom_data".actions.on_shift_click.command
function gui:barrel/interactions/click/on_click_action with entity @s data.action.click