$execute as $(player) if items entity @s player.cursor *[minecraft:custom_data~{ui_item:1}] run item replace entity @s player.cursor with minecraft:air
data remove block 0 -64 0 Items
scoreboard players set cursor_count utils 0
scoreboard players set cursor_add_count utils 0
$data modify block 0 -64 0 Items set value $(items)
data modify block 0 -64 0 Items[0].Slot set value 0b
data remove block 0 -64 0 Items[{components:{"minecraft:custom_data":{ui_item:1}}}]
$execute store result score cursor_count utils if items entity $(player) player.cursor *[minecraft:count={min:0}]
execute store result score cursor_add_count utils run data get block 0 -64 0 Items[0].count
execute store result block 0 -64 0 Items[0].count int 1 run scoreboard players operation cursor_count utils += cursor_add_count utils

$item replace entity $(player) player.cursor from block 0 -64 0 container.0
