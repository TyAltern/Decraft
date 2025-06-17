# tag @s add barrel_just_open
# execute if score @s open_barrel matches 2.. run scoreboard players set @s open_barrel 1
# function gui:utils/delay_as_stop {"ticks":2,"command":"scoreboard players set @s open_barrel 0","tag":"barrel_just_open"}
scoreboard players set @s open_barrel 0
scoreboard players reset * last_player_open_barrel
scoreboard players set @s last_player_open_barrel 1
# say barrel opened
# say hi