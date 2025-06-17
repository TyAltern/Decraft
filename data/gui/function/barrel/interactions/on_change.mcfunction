
execute store result score #curr gui run data get storage minecraft:ui current
execute store result score #prev gui run data get storage minecraft:ui previous

# Swap Hand Dectection
# NOT IMPLEMENTED YET BECAUSE OF SOME ISSUES
# $execute if items entity $(CurrentPlayerName) weapon.offhand *[minecraft:custom_data={ui_item:1}] run return run function gui:barrel/interactions/swap_hand/detection_swap_hand_slot with storage minecraft:ui 

# clear @a *[minecraft:custom_data~{ui_item:1}]

# Input detection
execute if score #prev gui < #curr gui run return run function gui:barrel/interactions/input/detection_input_slot

# Drop Detection
execute at @s if score #prev gui > #curr gui if entity @e[type=item,distance=..7,nbt={Age:0s}] run return run function gui:barrel/interactions/drop/detection_drop_slot_simple

# Click Detection
execute if score #prev gui > #curr gui run return run function gui:barrel/interactions/click/detection_click_slot

data remove storage minecraft:ui temporary
execute store success score #bool_previous gui run data modify storage minecraft:ui temporary append from storage minecraft:ui previous[{Slot:10b}]
execute store success score #bool_current gui run data modify storage minecraft:ui temporary append from storage minecraft:ui current[{Slot:10b}]

# Drop Detection Bis
execute at @s if score #bool_previous gui = #bool_current gui if entity @e[type=item,distance=..7,nbt={Age:0s}] run return run function gui:barrel/interactions/drop/detection_drop_slot_multiple

# Simult Detection
execute if score #bool_previous gui = #bool_current gui run return run function gui:barrel/interactions/simult/detection_simult_slot
