function gui:utils/get_player_name

$data modify storage minecraft:utils Delay.ticks set value $(ticks)
data modify storage minecraft:utils Delay.selector set from storage minecraft:utils get_player_name.out
$data modify storage minecraft:utils Delay.command set value "$(command)"

$schedule function gui:utils/private/delay_as/delay_as_run_parse $(ticks)t