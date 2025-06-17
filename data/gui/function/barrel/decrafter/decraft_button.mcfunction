execute at @s store result score #count_storage_slot_18 decraft run data get block ~ ~ ~ Items[{Slot:18b}].count
execute at @s store result score #count_storage_slot_19 decraft run data get block ~ ~ ~ Items[{Slot:19b}].count
execute at @s store result score #count_storage_slot_20 decraft run data get block ~ ~ ~ Items[{Slot:20b}].count

scoreboard players set count_storage decraft 0
scoreboard players operation count_storage decraft += #count_storage_slot_18 decraft
scoreboard players operation count_storage decraft += #count_storage_slot_19 decraft
scoreboard players operation count_storage decraft += #count_storage_slot_20 decraft

$scoreboard players set required_count decraft $(decraft_number)
scoreboard players operation required_count decraft *= SelectedItemCount decraft

execute at @s if data block ~ ~ ~ Items[{Slot:1b,id:"minecraft:barrier"}] run return fail




execute if score count_storage decraft < required_count decraft run return fail

function gui:barrel/decrafter/remove_from_storage

