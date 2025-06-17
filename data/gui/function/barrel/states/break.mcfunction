say GUI broke

execute at @s run kill @e[type=item, distance=..2,nbt={Item:{"components":{"minecraft:custom_data":{ui_item:1}}}}]
execute at @s run kill @e[type=item, distance=..2,limit=1,sort=nearest,nbt={Item:{id:"minecraft:barrel"}}]
execute at @s run summon minecraft:item ~ ~ ~ {Item:{id:"minecraft:allay_spawn_egg",components:{"minecraft:custom_name":{italic:0b,text:"GUI"},"minecraft:item_model":"minecraft:barrel","minecraft:entity_data":{Tags:["gui","positionate_gui"],id:"marker"}}}}
data modify entity @e[type=minecraft:item,sort=nearest,limit=1,nbt={Item:{id:"minecraft:allay_spawn_egg"}}] Motion set value [0d,0.25d,0d]
kill @s