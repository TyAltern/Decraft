say SWAP

# $function gui:utils/delay {"ticks":40,"command":"execute as $(CurrentPlayerName) run say hi @s"}
# function gui:utils/delay_as_stop {"ticks":5,"command":"clear @a *[minecraft:custom_data~{ui_item:1}]","tag":"null"}
# $execute as $(CurrentPlayerName) run clear @a *[minecraft:custom_data={ui_item:1}]
$item replace entity $(CurrentPlayerName) weapon.offhand with air
function gui:barrel/refresh