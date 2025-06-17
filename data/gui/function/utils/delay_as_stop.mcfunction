function gui:utils/get_player_name
$execute if entity @s[tag=$(tag)] run return fail

$tag @s add $(tag)
$data modify storage minecraft:utils Delay.tag set value $(tag)
$data modify storage minecraft:utils Delay.ticks set value $(ticks)
data modify storage minecraft:utils Delay.selector set from storage minecraft:utils get_player_name.out
$data modify storage minecraft:utils Delay.command set value "$(command)"

$schedule function gui:utils/private/delay_as_stop_run/delay_as_stop_run_parse $(ticks)t