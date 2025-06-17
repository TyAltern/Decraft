summon minecraft:marker 0 0 0 {Tags:["tp_back"]}
$data modify entity @e[type=marker,limit=1,tag=tp_back] Pos set value $(Pos)
$data modify entity @e[type=marker,limit=1,tag=tp_back] Rotation set value $(Rotation)
tp @s @e[type=marker,limit=1,tag=tp_back]
kill @e[type=marker,limit=1,tag=tp_back]
