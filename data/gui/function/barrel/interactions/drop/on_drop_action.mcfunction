# $say Try to Drop $(selected_item_count)x $(selected_item_id) in $(selected_item_slot) $(selected_item_command) $(selected_item_is_from_ui)

$execute if data entity @s data.action.click.selected_item_command run function gui:utils/cmd {"command":"$(selected_item_command)"}

kill @e[type=item,distance=..7,nbt={Age:0s,Item:{components:{"minecraft:custom_data":{ui_item:1}}}}]
clear @a *[minecraft:custom_data~{ui_item:1}]


function gui:barrel/refresh