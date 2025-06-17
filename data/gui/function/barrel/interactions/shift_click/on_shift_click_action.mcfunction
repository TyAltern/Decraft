# $say Shift Click on $(selected_item_count)x $(selected_item_id) in $(selected_item_slot) $(selected_item_command) $(selected_item_is_from_ui)

$execute if data entity @s data.action.click.selected_item_command run function gui:utils/cmd {"command":"$(selected_item_command)"}

# $function gui:utils/is_equal {"one":"$(selected_item_is_from_ui)","two":"1","if":"say from ui","else":""}

clear @a *[minecraft:custom_data~{ui_item:1}]


function gui:barrel/refresh