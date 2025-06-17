scoreboard players operation required_count decraft -= #count_storage_slot_20 decraft

execute if score required_count decraft matches 0.. run data modify storage minecraft:ui current[{Slot:20b}] set value {}
execute if score required_count decraft matches ..-1 store result storage minecraft:ui current[{Slot:20b}].count int -1 run scoreboard players get required_count decraft

function gui:barrel/refresh
execute if score required_count decraft matches ..0 run return fail

scoreboard players operation required_count decraft -= #count_storage_slot_19 decraft

execute if score required_count decraft matches 0.. run data modify storage minecraft:ui current[{Slot:19b}] set value {}
execute if score required_count decraft matches ..-1 store result storage minecraft:ui current[{Slot:19b}].count int -1 run scoreboard players get required_count decraft

function gui:barrel/refresh
execute if score required_count decraft matches ..0 run return fail

scoreboard players operation required_count decraft -= #count_storage_slot_18 decraft

execute if score required_count decraft matches 0.. run data modify storage minecraft:ui current[{Slot:18b}] set value {}
execute if score required_count decraft matches ..-1 store result storage minecraft:ui current[{Slot:18b}].count int -1 run scoreboard players get required_count decraft

function gui:barrel/refresh
execute if score required_count decraft matches ..0 run return fail



# execute if score required_count decraft matches 1.. unless data storage minecraft:ui current[{Slot:20b}] if data storage minecraft:ui current[{Slot:19b}]
# execute store result storage minecraft:ui current[{Slot:$(slot)b}].count int 1 run scoreboard players operation #count_storage_slot_$(slot) decraft += required_count decraft
# execute if score #count_storage_slot_3 decraft >= required_count decraft run 