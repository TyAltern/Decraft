
execute at @s store result score #count_display_storage_slot_18 decraft run data get block ~ ~ ~ Items[{Slot:18b}].count
execute at @s store result score #count_display_storage_slot_19 decraft run data get block ~ ~ ~ Items[{Slot:19b}].count
execute at @s store result score #count_display_storage_slot_20 decraft run data get block ~ ~ ~ Items[{Slot:20b}].count

scoreboard players set #count_display_storage decraft 0
scoreboard players operation #count_display_storage decraft += #count_display_storage_slot_18 decraft
scoreboard players operation #count_display_storage decraft += #count_display_storage_slot_19 decraft
scoreboard players operation #count_display_storage decraft += #count_display_storage_slot_20 decraft

scoreboard players set #required_count_display decraft 1
scoreboard players operation #required_count_display decraft *= SelectedItemCount decraft
# say test 1

execute at @s if data block ~ ~ ~ Items[{Slot:1b,id:"minecraft:barrier"}] run return run data modify storage minecraft:ui DecraftPossible.one set value {Slot:4b,id:"minecraft:red_stained_glass_pane", components: {"minecraft:custom_name":{italic:0b, text:"Not enough item", bold:1b, color:"red"},"minecraft:custom_data":{ui_item:1,actions:{}}}}


execute if score #count_display_storage decraft < #required_count_display decraft run return run data modify storage minecraft:ui DecraftPossible.one set value {Slot:4b,id:"minecraft:red_stained_glass_pane", components: {"minecraft:custom_name":{italic:0b, text:"Not enough item", bold:1b, color:"red"},"minecraft:custom_data":{ui_item:1,actions:{}}}}


data modify storage minecraft:ui DecraftPossible.one set value {Slot:4b,id:"minecraft:lime_stained_glass_pane", components: {"minecraft:custom_name":{italic:0b, text:"Decraft 1", bold:1b, color:"green"},"minecraft:custom_data":{ui_item:1,actions:{on_click:{command:"function gui:barrel/decrafter/decraft_button {decraft_number:1}"}}}}}