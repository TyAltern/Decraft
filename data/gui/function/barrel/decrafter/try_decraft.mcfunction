data modify storage minecraft:ui decraft.player set from storage minecraft:ui CurrentPlayerName

data modify storage minecraft:ui SelectedItemCustomData.id set string storage minecraft:ui SelectedItem.id 10
data modify storage minecraft:ui SelectedItemCustomData.count set from storage minecraft:ui SelectedItem.count
function gui:barrel/decrafter/call_try with storage minecraft:ui SelectedItemCustomData
