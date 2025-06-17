
data remove storage operation match
$data modify storage operation compare.one set value $(one)
$data modify storage operation compare.two set value $(two)
$data modify storage operation compare.result.pass.command set value "$(if)"
$data modify storage operation compare.result.fail.command set value "$(else)"

execute store success score #match boolean run data modify storage operation compare.one set from storage operation compare.two
execute if score #match boolean matches 1 run function gui:utils/cmd with storage operation compare.result.fail
execute if score #match boolean matches 0 run function gui:utils/cmd with storage operation compare.result.pass
