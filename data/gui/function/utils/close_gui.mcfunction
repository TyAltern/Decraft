data modify storage minecraft:utils Player.name set from entity @s Pos
data modify storage minecraft:utils Player.close_gui.Motion set from entity @s Motion
data modify storage minecraft:utils Player.close_gui.Pos set from entity @s Pos
data modify storage minecraft:utils Player.close_gui.Rotation set from entity @s Rotation
execute as @s at @s run tp @s ~ ~10000 ~ 
function gui:utils/delay_as {"ticks":2,"command":"function gui:utils/private/close_gui_run_parse"}
# execute as @s schedule function gui:utils/private/close_gui_run_parse 1t