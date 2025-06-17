execute at @s unless score SelectedItemCount decraft matches 0 unless items block ~ ~ ~ container.1 *[minecraft:count=64] unless items block ~ ~ ~ container.1 *[minecraft:count=63] unless items block ~ ~ ~ container.1 *[minecraft:count=62] unless items block ~ ~ ~ container.1 *[minecraft:count=61] run scoreboard players add SelectedItemCount decraft 4
execute at @s if items block ~ ~ ~ container.1 *[minecraft:count=63] run scoreboard players set SelectedItemCount decraft 64
execute at @s if items block ~ ~ ~ container.1 *[minecraft:count=62] run scoreboard players set SelectedItemCount decraft 64
execute at @s if items block ~ ~ ~ container.1 *[minecraft:count=61] run scoreboard players set SelectedItemCount decraft 64
execute store result storage minecraft:ui SelectedItem.count int 1 run scoreboard players get SelectedItemCount decraft


function gui:barrel/refresh

function gui:barrel/decrafter/try_decraft_display