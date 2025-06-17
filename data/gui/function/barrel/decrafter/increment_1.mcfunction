execute at @s unless score SelectedItemCount decraft matches 0 unless items block ~ ~ ~ container.1 *[minecraft:count=64] run scoreboard players add SelectedItemCount decraft 1
execute store result storage minecraft:ui SelectedItem.count int 1 run scoreboard players get SelectedItemCount decraft


function gui:barrel/refresh