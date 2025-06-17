execute as @e[tag=gui] run function gui:barrel/tick


execute as @a unless score @s open_barrel matches 0 run function gui:player/open_barrel
# as @e[tag=gui] at @s if block ~ ~ ~ minecraft:barrel[open=true] if entity @s[nbt={data:{open:0}}] run say hi