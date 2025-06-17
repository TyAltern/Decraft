data remove block 0 -64 0 Items
$data modify block 0 -64 0 Items set value $(items)
data remove block 0 -64 0 Items[{components:{"minecraft:custom_data":{ui_item:1}}}]
$execute if data entity $(player) Inventory[35] at $(player) run loot spawn ~ ~ ~ mine 0 -64 0 stick[minecraft:custom_data={drop_contents:1b}]
$loot give $(player) mine 0 -64 0 stick[minecraft:custom_data={drop_contents:1b}]