# Same as give_unique but you juste overwrite what was in your cursor slot with $(item)

$execute as $(player) if items entity @s player.cursor *[minecraft:custom_data~{ui_item:1}] run item replace entity @s player.cursor with minecraft:air
data remove block 0 -64 0 Items
$data modify block 0 -64 0 Items set value $(items)
data modify block 0 -64 0 Items[0].Slot set value 0b
data remove block 0 -64 0 Items[{components:{"minecraft:custom_data":{ui_item:1}}}]

$item replace entity $(player) player.cursor from block 0 -64 0 container.0
