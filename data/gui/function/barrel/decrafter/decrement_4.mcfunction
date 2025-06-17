execute at @s unless score SelectedItemCount decraft matches 0 unless items block ~ ~ ~ container.1 *[minecraft:count=1] unless items block ~ ~ ~ container.1 *[minecraft:count=2] unless items block ~ ~ ~ container.1 *[minecraft:count=3] unless items block ~ ~ ~ container.1 *[minecraft:count=4] run scoreboard players remove SelectedItemCount decraft 4
execute at @s if items block ~ ~ ~ container.1 *[minecraft:count=2] run scoreboard players set SelectedItemCount decraft 1
execute at @s if items block ~ ~ ~ container.1 *[minecraft:count=3] run scoreboard players set SelectedItemCount decraft 1
execute at @s if items block ~ ~ ~ container.1 *[minecraft:count=4] run scoreboard players set SelectedItemCount decraft 1
execute store result storage minecraft:ui SelectedItem.count int 1 run scoreboard players get SelectedItemCount decraft


function gui:barrel/refresh