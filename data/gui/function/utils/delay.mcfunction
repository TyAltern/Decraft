
$data modify storage minecraft:utils Delay.ticks set value $(ticks)
$data modify storage minecraft:utils Delay.command set value "$(command)"

$schedule function gui:utils/private/delay/delay_run_parse $(ticks)t