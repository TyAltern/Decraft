function gui:utils/give_unique_base with storage minecraft:utils give
$data modify storage minecraft:ui current[{Slot:$(clicked_item_slot)b}] set value $(clicked_item)