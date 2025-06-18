import os

crafting_recipe = [
  {
    "crafting_recipe_name": "acacia_boat",
    "input": {
      "item": "minecraft:acacia_boat",
      "count": 1
    },
    "output_display": [
      "minecraft:acacia_planks",
      None,
      "minecraft:acacia_planks",
      "minecraft:acacia_planks",
      "minecraft:acacia_planks",
      "minecraft:acacia_planks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:acacia_planks",
        "count": 5
      }
    ]
  },
  {
    "crafting_recipe_name": "acacia_button",
    "input": {
      "item": "minecraft:acacia_button",
      "count": 1
    },
    "output_display": [
      "minecraft:acacia_planks",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:acacia_planks",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "acacia_chest_boat",
    "input": {
      "item": "minecraft:acacia_chest_boat",
      "count": 1
    },
    "output_display": [
      "minecraft:chest",
      "minecraft:acacia_boat",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:chest",
        "count": 1
      },
      {
        "id": "minecraft:acacia_boat",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "acacia_door",
    "input": {
      "item": "minecraft:acacia_door",
      "count": 3
    },
    "output_display": [
      "minecraft:acacia_planks",
      "minecraft:acacia_planks",
      None,
      "minecraft:acacia_planks",
      "minecraft:acacia_planks",
      None,
      "minecraft:acacia_planks",
      "minecraft:acacia_planks",
      None
    ],
    "output": [
      {
        "id": "minecraft:acacia_planks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "acacia_fence",
    "input": {
      "item": "minecraft:acacia_fence",
      "count": 3
    },
    "output_display": [
      "minecraft:acacia_planks",
      "minecraft:stick",
      "minecraft:acacia_planks",
      "minecraft:acacia_planks",
      "minecraft:stick",
      "minecraft:acacia_planks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:acacia_planks",
        "count": 4
      },
      {
        "id": "minecraft:stick",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "acacia_fence_gate",
    "input": {
      "item": "minecraft:acacia_fence_gate",
      "count": 1
    },
    "output_display": [
      "minecraft:stick",
      "minecraft:acacia_planks",
      "minecraft:stick",
      "minecraft:stick",
      "minecraft:acacia_planks",
      "minecraft:stick",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:stick",
        "count": 4
      },
      {
        "id": "minecraft:acacia_planks",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "acacia_hanging_sign",
    "input": {
      "item": "minecraft:acacia_hanging_sign",
      "count": 6
    },
    "output_display": [
      "minecraft:chain",
      None,
      "minecraft:chain",
      "minecraft:stripped_acacia_log",
      "minecraft:stripped_acacia_log",
      "minecraft:stripped_acacia_log",
      "minecraft:stripped_acacia_log",
      "minecraft:stripped_acacia_log",
      "minecraft:stripped_acacia_log"
    ],
    "output": [
      {
        "id": "minecraft:chain",
        "count": 2
      },
      {
        "id": "minecraft:stripped_acacia_log",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "acacia_planks",
    "input": {
      "item": "minecraft:acacia_planks",
      "count": 4
    },
    "output_display": [
      "minecraft:acacia_log",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:acacia_log",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "acacia_pressure_plate",
    "input": {
      "item": "minecraft:acacia_pressure_plate",
      "count": 1
    },
    "output_display": [
      "minecraft:acacia_planks",
      "minecraft:acacia_planks",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:acacia_planks",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "acacia_sign",
    "input": {
      "item": "minecraft:acacia_sign",
      "count": 3
    },
    "output_display": [
      "minecraft:acacia_planks",
      "minecraft:acacia_planks",
      "minecraft:acacia_planks",
      "minecraft:acacia_planks",
      "minecraft:acacia_planks",
      "minecraft:acacia_planks",
      None,
      "minecraft:stick",
      None
    ],
    "output": [
      {
        "id": "minecraft:acacia_planks",
        "count": 6
      },
      {
        "id": "minecraft:stick",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "acacia_slab",
    "input": {
      "item": "minecraft:acacia_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:acacia_planks",
      "minecraft:acacia_planks",
      "minecraft:acacia_planks",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:acacia_planks",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "acacia_stairs",
    "input": {
      "item": "minecraft:acacia_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:acacia_planks",
      None,
      None,
      "minecraft:acacia_planks",
      "minecraft:acacia_planks",
      None,
      "minecraft:acacia_planks",
      "minecraft:acacia_planks",
      "minecraft:acacia_planks"
    ],
    "output": [
      {
        "id": "minecraft:acacia_planks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "acacia_trapdoor",
    "input": {
      "item": "minecraft:acacia_trapdoor",
      "count": 2
    },
    "output_display": [
      "minecraft:acacia_planks",
      "minecraft:acacia_planks",
      "minecraft:acacia_planks",
      "minecraft:acacia_planks",
      "minecraft:acacia_planks",
      "minecraft:acacia_planks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:acacia_planks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "acacia_wood",
    "input": {
      "item": "minecraft:acacia_wood",
      "count": 3
    },
    "output_display": [
      "minecraft:acacia_log",
      "minecraft:acacia_log",
      None,
      "minecraft:acacia_log",
      "minecraft:acacia_log",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:acacia_log",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "activator_rail",
    "input": {
      "item": "minecraft:activator_rail",
      "count": 6
    },
    "output_display": [
      "minecraft:iron_ingot",
      "minecraft:stick",
      "minecraft:iron_ingot",
      "minecraft:iron_ingot",
      "minecraft:redstone_torch",
      "minecraft:iron_ingot",
      "minecraft:iron_ingot",
      "minecraft:stick",
      "minecraft:iron_ingot"
    ],
    "output": [
      {
        "id": "minecraft:iron_ingot",
        "count": 6
      },
      {
        "id": "minecraft:stick",
        "count": 2
      },
      {
        "id": "minecraft:redstone_torch",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "amethyst_block",
    "input": {
      "item": "minecraft:amethyst_block",
      "count": 1
    },
    "output_display": [
      "minecraft:amethyst_shard",
      "minecraft:amethyst_shard",
      None,
      "minecraft:amethyst_shard",
      "minecraft:amethyst_shard",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:amethyst_shard",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "andesite",
    "input": {
      "item": "minecraft:andesite",
      "count": 2
    },
    "output_display": [
      "minecraft:diorite",
      "minecraft:cobblestone",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:diorite",
        "count": 1
      },
      {
        "id": "minecraft:cobblestone",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "andesite_slab",
    "input": {
      "item": "minecraft:andesite_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:andesite",
      "minecraft:andesite",
      "minecraft:andesite",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:andesite",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "andesite_stairs",
    "input": {
      "item": "minecraft:andesite_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:andesite",
      None,
      None,
      "minecraft:andesite",
      "minecraft:andesite",
      None,
      "minecraft:andesite",
      "minecraft:andesite",
      "minecraft:andesite"
    ],
    "output": [
      {
        "id": "minecraft:andesite",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "andesite_wall",
    "input": {
      "item": "minecraft:andesite_wall",
      "count": 6
    },
    "output_display": [
      "minecraft:andesite",
      "minecraft:andesite",
      "minecraft:andesite",
      "minecraft:andesite",
      "minecraft:andesite",
      "minecraft:andesite",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:andesite",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "anvil",
    "input": {
      "item": "minecraft:anvil",
      "count": 1
    },
    "output_display": [
      "minecraft:iron_block",
      "minecraft:iron_block",
      "minecraft:iron_block",
      None,
      "minecraft:iron_ingot",
      None,
      "minecraft:iron_ingot",
      "minecraft:iron_ingot",
      "minecraft:iron_ingot"
    ],
    "output": [
      {
        "id": "minecraft:iron_block",
        "count": 3
      },
      {
        "id": "minecraft:iron_ingot",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "armor_stand",
    "input": {
      "item": "minecraft:armor_stand",
      "count": 1
    },
    "output_display": [
      "minecraft:stick",
      "minecraft:stick",
      "minecraft:stick",
      None,
      "minecraft:stick",
      None,
      "minecraft:stick",
      "minecraft:smooth_stone_slab",
      "minecraft:stick"
    ],
    "output": [
      {
        "id": "minecraft:stick",
        "count": 6
      },
      {
        "id": "minecraft:smooth_stone_slab",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "arrow",
    "input": {
      "item": "minecraft:arrow",
      "count": 4
    },
    "output_display": [
      "minecraft:flint",
      None,
      None,
      "minecraft:stick",
      None,
      None,
      "minecraft:feather",
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:flint",
        "count": 1
      },
      {
        "id": "minecraft:stick",
        "count": 1
      },
      {
        "id": "minecraft:feather",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "bamboo_block",
    "input": {
      "item": "minecraft:bamboo_block",
      "count": 1
    },
    "output_display": [
      "minecraft:bamboo",
      "minecraft:bamboo",
      "minecraft:bamboo",
      "minecraft:bamboo",
      "minecraft:bamboo",
      "minecraft:bamboo",
      "minecraft:bamboo",
      "minecraft:bamboo",
      "minecraft:bamboo"
    ],
    "output": [
      {
        "id": "minecraft:bamboo",
        "count": 9
      }
    ]
  },
  {
    "crafting_recipe_name": "bamboo_button",
    "input": {
      "item": "minecraft:bamboo_button",
      "count": 1
    },
    "output_display": [
      "minecraft:bamboo_planks",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:bamboo_planks",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "bamboo_chest_raft",
    "input": {
      "item": "minecraft:bamboo_chest_raft",
      "count": 1
    },
    "output_display": [
      "minecraft:chest",
      "minecraft:bamboo_raft",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:chest",
        "count": 1
      },
      {
        "id": "minecraft:bamboo_raft",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "bamboo_door",
    "input": {
      "item": "minecraft:bamboo_door",
      "count": 3
    },
    "output_display": [
      "minecraft:bamboo_planks",
      "minecraft:bamboo_planks",
      None,
      "minecraft:bamboo_planks",
      "minecraft:bamboo_planks",
      None,
      "minecraft:bamboo_planks",
      "minecraft:bamboo_planks",
      None
    ],
    "output": [
      {
        "id": "minecraft:bamboo_planks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "bamboo_fence",
    "input": {
      "item": "minecraft:bamboo_fence",
      "count": 3
    },
    "output_display": [
      "minecraft:bamboo_planks",
      "minecraft:stick",
      "minecraft:bamboo_planks",
      "minecraft:bamboo_planks",
      "minecraft:stick",
      "minecraft:bamboo_planks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:bamboo_planks",
        "count": 4
      },
      {
        "id": "minecraft:stick",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "bamboo_fence_gate",
    "input": {
      "item": "minecraft:bamboo_fence_gate",
      "count": 1
    },
    "output_display": [
      "minecraft:stick",
      "minecraft:bamboo_planks",
      "minecraft:stick",
      "minecraft:stick",
      "minecraft:bamboo_planks",
      "minecraft:stick",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:stick",
        "count": 4
      },
      {
        "id": "minecraft:bamboo_planks",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "bamboo_hanging_sign",
    "input": {
      "item": "minecraft:bamboo_hanging_sign",
      "count": 6
    },
    "output_display": [
      "minecraft:chain",
      None,
      "minecraft:chain",
      "minecraft:stripped_bamboo_block",
      "minecraft:stripped_bamboo_block",
      "minecraft:stripped_bamboo_block",
      "minecraft:stripped_bamboo_block",
      "minecraft:stripped_bamboo_block",
      "minecraft:stripped_bamboo_block"
    ],
    "output": [
      {
        "id": "minecraft:chain",
        "count": 2
      },
      {
        "id": "minecraft:stripped_bamboo_block",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "bamboo_mosaic",
    "input": {
      "item": "minecraft:bamboo_mosaic",
      "count": 1
    },
    "output_display": [
      "minecraft:bamboo_slab",
      None,
      None,
      "minecraft:bamboo_slab",
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:bamboo_slab",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "bamboo_mosaic_slab",
    "input": {
      "item": "minecraft:bamboo_mosaic_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:bamboo_mosaic",
      "minecraft:bamboo_mosaic",
      "minecraft:bamboo_mosaic",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:bamboo_mosaic",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "bamboo_mosaic_stairs",
    "input": {
      "item": "minecraft:bamboo_mosaic_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:bamboo_mosaic",
      None,
      None,
      "minecraft:bamboo_mosaic",
      "minecraft:bamboo_mosaic",
      None,
      "minecraft:bamboo_mosaic",
      "minecraft:bamboo_mosaic",
      "minecraft:bamboo_mosaic"
    ],
    "output": [
      {
        "id": "minecraft:bamboo_mosaic",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "bamboo_planks",
    "input": {
      "item": "minecraft:bamboo_planks",
      "count": 2
    },
    "output_display": [
      "minecraft:bamboo_block",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:bamboo_block",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "bamboo_pressure_plate",
    "input": {
      "item": "minecraft:bamboo_pressure_plate",
      "count": 1
    },
    "output_display": [
      "minecraft:bamboo_planks",
      "minecraft:bamboo_planks",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:bamboo_planks",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "bamboo_raft",
    "input": {
      "item": "minecraft:bamboo_raft",
      "count": 1
    },
    "output_display": [
      "minecraft:bamboo_planks",
      None,
      "minecraft:bamboo_planks",
      "minecraft:bamboo_planks",
      "minecraft:bamboo_planks",
      "minecraft:bamboo_planks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:bamboo_planks",
        "count": 5
      }
    ]
  },
  {
    "crafting_recipe_name": "bamboo_sign",
    "input": {
      "item": "minecraft:bamboo_sign",
      "count": 3
    },
    "output_display": [
      "minecraft:bamboo_planks",
      "minecraft:bamboo_planks",
      "minecraft:bamboo_planks",
      "minecraft:bamboo_planks",
      "minecraft:bamboo_planks",
      "minecraft:bamboo_planks",
      None,
      "minecraft:stick",
      None
    ],
    "output": [
      {
        "id": "minecraft:bamboo_planks",
        "count": 6
      },
      {
        "id": "minecraft:stick",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "bamboo_slab",
    "input": {
      "item": "minecraft:bamboo_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:bamboo_planks",
      "minecraft:bamboo_planks",
      "minecraft:bamboo_planks",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:bamboo_planks",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "bamboo_stairs",
    "input": {
      "item": "minecraft:bamboo_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:bamboo_planks",
      None,
      None,
      "minecraft:bamboo_planks",
      "minecraft:bamboo_planks",
      None,
      "minecraft:bamboo_planks",
      "minecraft:bamboo_planks",
      "minecraft:bamboo_planks"
    ],
    "output": [
      {
        "id": "minecraft:bamboo_planks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "bamboo_trapdoor",
    "input": {
      "item": "minecraft:bamboo_trapdoor",
      "count": 2
    },
    "output_display": [
      "minecraft:bamboo_planks",
      "minecraft:bamboo_planks",
      "minecraft:bamboo_planks",
      "minecraft:bamboo_planks",
      "minecraft:bamboo_planks",
      "minecraft:bamboo_planks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:bamboo_planks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "barrel",
    "input": {
      "item": "minecraft:barrel",
      "count": 1
    },
    "output_display": [
      "minecraft:oak_planks",
      "minecraft:oak_slab",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      None,
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:oak_slab",
      "minecraft:oak_planks"
    ],
    "output": [
      {
        "id": "minecraft:oak_planks",
        "count": 6
      },
      {
        "id": "minecraft:oak_slab",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "beacon",
    "input": {
      "item": "minecraft:beacon",
      "count": 1
    },
    "output_display": [
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:nether_star",
      "minecraft:glass",
      "minecraft:obsidian",
      "minecraft:obsidian",
      "minecraft:obsidian"
    ],
    "output": [
      {
        "id": "minecraft:glass",
        "count": 5
      },
      {
        "id": "minecraft:nether_star",
        "count": 1
      },
      {
        "id": "minecraft:obsidian",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "beehive",
    "input": {
      "item": "minecraft:beehive",
      "count": 1
    },
    "output_display": [
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:honeycomb",
      "minecraft:honeycomb",
      "minecraft:honeycomb",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:oak_planks"
    ],
    "output": [
      {
        "id": "minecraft:oak_planks",
        "count": 6
      },
      {
        "id": "minecraft:honeycomb",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "beetroot_soup",
    "input": {
      "item": "minecraft:beetroot_soup",
      "count": 1
    },
    "output_display": [
      "minecraft:bowl",
      "minecraft:beetroot",
      "minecraft:beetroot",
      "minecraft:beetroot",
      "minecraft:beetroot",
      "minecraft:beetroot",
      "minecraft:beetroot",
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:bowl",
        "count": 1
      },
      {
        "id": "minecraft:beetroot",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "birch_boat",
    "input": {
      "item": "minecraft:birch_boat",
      "count": 1
    },
    "output_display": [
      "minecraft:birch_planks",
      None,
      "minecraft:birch_planks",
      "minecraft:birch_planks",
      "minecraft:birch_planks",
      "minecraft:birch_planks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:birch_planks",
        "count": 5
      }
    ]
  },
  {
    "crafting_recipe_name": "birch_button",
    "input": {
      "item": "minecraft:birch_button",
      "count": 1
    },
    "output_display": [
      "minecraft:birch_planks",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:birch_planks",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "birch_chest_boat",
    "input": {
      "item": "minecraft:birch_chest_boat",
      "count": 1
    },
    "output_display": [
      "minecraft:chest",
      "minecraft:birch_boat",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:chest",
        "count": 1
      },
      {
        "id": "minecraft:birch_boat",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "birch_door",
    "input": {
      "item": "minecraft:birch_door",
      "count": 3
    },
    "output_display": [
      "minecraft:birch_planks",
      "minecraft:birch_planks",
      None,
      "minecraft:birch_planks",
      "minecraft:birch_planks",
      None,
      "minecraft:birch_planks",
      "minecraft:birch_planks",
      None
    ],
    "output": [
      {
        "id": "minecraft:birch_planks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "birch_fence",
    "input": {
      "item": "minecraft:birch_fence",
      "count": 3
    },
    "output_display": [
      "minecraft:birch_planks",
      "minecraft:stick",
      "minecraft:birch_planks",
      "minecraft:birch_planks",
      "minecraft:stick",
      "minecraft:birch_planks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:birch_planks",
        "count": 4
      },
      {
        "id": "minecraft:stick",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "birch_fence_gate",
    "input": {
      "item": "minecraft:birch_fence_gate",
      "count": 1
    },
    "output_display": [
      "minecraft:stick",
      "minecraft:birch_planks",
      "minecraft:stick",
      "minecraft:stick",
      "minecraft:birch_planks",
      "minecraft:stick",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:stick",
        "count": 4
      },
      {
        "id": "minecraft:birch_planks",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "birch_hanging_sign",
    "input": {
      "item": "minecraft:birch_hanging_sign",
      "count": 6
    },
    "output_display": [
      "minecraft:chain",
      None,
      "minecraft:chain",
      "minecraft:stripped_birch_log",
      "minecraft:stripped_birch_log",
      "minecraft:stripped_birch_log",
      "minecraft:stripped_birch_log",
      "minecraft:stripped_birch_log",
      "minecraft:stripped_birch_log"
    ],
    "output": [
      {
        "id": "minecraft:chain",
        "count": 2
      },
      {
        "id": "minecraft:stripped_birch_log",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "birch_planks",
    "input": {
      "item": "minecraft:birch_planks",
      "count": 4
    },
    "output_display": [
      "minecraft:birch_log",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:birch_log",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "birch_pressure_plate",
    "input": {
      "item": "minecraft:birch_pressure_plate",
      "count": 1
    },
    "output_display": [
      "minecraft:birch_planks",
      "minecraft:birch_planks",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:birch_planks",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "birch_sign",
    "input": {
      "item": "minecraft:birch_sign",
      "count": 3
    },
    "output_display": [
      "minecraft:birch_planks",
      "minecraft:birch_planks",
      "minecraft:birch_planks",
      "minecraft:birch_planks",
      "minecraft:birch_planks",
      "minecraft:birch_planks",
      None,
      "minecraft:stick",
      None
    ],
    "output": [
      {
        "id": "minecraft:birch_planks",
        "count": 6
      },
      {
        "id": "minecraft:stick",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "birch_slab",
    "input": {
      "item": "minecraft:birch_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:birch_planks",
      "minecraft:birch_planks",
      "minecraft:birch_planks",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:birch_planks",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "birch_stairs",
    "input": {
      "item": "minecraft:birch_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:birch_planks",
      None,
      None,
      "minecraft:birch_planks",
      "minecraft:birch_planks",
      None,
      "minecraft:birch_planks",
      "minecraft:birch_planks",
      "minecraft:birch_planks"
    ],
    "output": [
      {
        "id": "minecraft:birch_planks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "birch_trapdoor",
    "input": {
      "item": "minecraft:birch_trapdoor",
      "count": 2
    },
    "output_display": [
      "minecraft:birch_planks",
      "minecraft:birch_planks",
      "minecraft:birch_planks",
      "minecraft:birch_planks",
      "minecraft:birch_planks",
      "minecraft:birch_planks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:birch_planks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "birch_wood",
    "input": {
      "item": "minecraft:birch_wood",
      "count": 3
    },
    "output_display": [
      "minecraft:birch_log",
      "minecraft:birch_log",
      None,
      "minecraft:birch_log",
      "minecraft:birch_log",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:birch_log",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "blackstone_slab",
    "input": {
      "item": "minecraft:blackstone_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:blackstone",
      "minecraft:blackstone",
      "minecraft:blackstone",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:blackstone",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "blackstone_stairs",
    "input": {
      "item": "minecraft:blackstone_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:blackstone",
      None,
      None,
      "minecraft:blackstone",
      "minecraft:blackstone",
      None,
      "minecraft:blackstone",
      "minecraft:blackstone",
      "minecraft:blackstone"
    ],
    "output": [
      {
        "id": "minecraft:blackstone",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "blackstone_wall",
    "input": {
      "item": "minecraft:blackstone_wall",
      "count": 6
    },
    "output_display": [
      "minecraft:blackstone",
      "minecraft:blackstone",
      "minecraft:blackstone",
      "minecraft:blackstone",
      "minecraft:blackstone",
      "minecraft:blackstone",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:blackstone",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "black_banner",
    "input": {
      "item": "minecraft:black_banner",
      "count": 1
    },
    "output_display": [
      "minecraft:black_wool",
      "minecraft:black_wool",
      "minecraft:black_wool",
      "minecraft:black_wool",
      "minecraft:black_wool",
      "minecraft:black_wool",
      None,
      "minecraft:stick",
      None
    ],
    "output": [
      {
        "id": "minecraft:black_wool",
        "count": 6
      },
      {
        "id": "minecraft:stick",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "black_bed",
    "input": {
      "item": "minecraft:black_bed",
      "count": 1
    },
    "output_display": [
      "minecraft:black_wool",
      "minecraft:black_wool",
      "minecraft:black_wool",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:black_wool",
        "count": 3
      },
      {
        "id": "minecraft:oak_planks",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "black_candle",
    "input": {
      "item": "minecraft:black_candle",
      "count": 1
    },
    "output_display": [
      "minecraft:candle",
      "minecraft:black_dye",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:candle",
        "count": 1
      },
      {
        "id": "minecraft:black_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "black_carpet",
    "input": {
      "item": "minecraft:black_carpet",
      "count": 3
    },
    "output_display": [
      "minecraft:black_wool",
      "minecraft:black_wool",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:black_wool",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "black_concrete_powder",
    "input": {
      "item": "minecraft:black_concrete_powder",
      "count": 8
    },
    "output_display": [
      "minecraft:black_dye",
      "minecraft:sand",
      "minecraft:sand",
      "minecraft:sand",
      "minecraft:sand",
      "minecraft:gravel",
      "minecraft:gravel",
      "minecraft:gravel",
      "minecraft:gravel"
    ],
    "output": [
      {
        "id": "minecraft:black_dye",
        "count": 1
      },
      {
        "id": "minecraft:sand",
        "count": 4
      },
      {
        "id": "minecraft:gravel",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "black_dye",
    "input": {
      "item": "minecraft:black_dye",
      "count": 1
    },
    "output_display": [
      "minecraft:ink_sac",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:ink_sac",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "black_dye_from_wither_rose",
    "input": {
      "item": "minecraft:black_dye",
      "count": 1
    },
    "output_display": [
      "minecraft:wither_rose",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:wither_rose",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "black_stained_glass",
    "input": {
      "item": "minecraft:black_stained_glass",
      "count": 8
    },
    "output_display": [
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:black_dye",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass"
    ],
    "output": [
      {
        "id": "minecraft:glass",
        "count": 8
      },
      {
        "id": "minecraft:black_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "black_stained_glass_pane",
    "input": {
      "item": "minecraft:black_stained_glass_pane",
      "count": 16
    },
    "output_display": [
      "minecraft:black_stained_glass",
      "minecraft:black_stained_glass",
      "minecraft:black_stained_glass",
      "minecraft:black_stained_glass",
      "minecraft:black_stained_glass",
      "minecraft:black_stained_glass",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:black_stained_glass",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "black_stained_glass_pane_from_glass_pane",
    "input": {
      "item": "minecraft:black_stained_glass_pane",
      "count": 8
    },
    "output_display": [
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:black_dye",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane"
    ],
    "output": [
      {
        "id": "minecraft:glass_pane",
        "count": 8
      },
      {
        "id": "minecraft:black_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "black_terracotta",
    "input": {
      "item": "minecraft:black_terracotta",
      "count": 8
    },
    "output_display": [
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:black_dye",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta"
    ],
    "output": [
      {
        "id": "minecraft:terracotta",
        "count": 8
      },
      {
        "id": "minecraft:black_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "blast_furnace",
    "input": {
      "item": "minecraft:blast_furnace",
      "count": 1
    },
    "output_display": [
      "minecraft:iron_ingot",
      "minecraft:iron_ingot",
      "minecraft:iron_ingot",
      "minecraft:iron_ingot",
      "minecraft:furnace",
      "minecraft:iron_ingot",
      "minecraft:smooth_stone",
      "minecraft:smooth_stone",
      "minecraft:smooth_stone"
    ],
    "output": [
      {
        "id": "minecraft:iron_ingot",
        "count": 5
      },
      {
        "id": "minecraft:furnace",
        "count": 1
      },
      {
        "id": "minecraft:smooth_stone",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "blaze_powder",
    "input": {
      "item": "minecraft:blaze_powder",
      "count": 2
    },
    "output_display": [
      "minecraft:blaze_rod",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:blaze_rod",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "blue_banner",
    "input": {
      "item": "minecraft:blue_banner",
      "count": 1
    },
    "output_display": [
      "minecraft:blue_wool",
      "minecraft:blue_wool",
      "minecraft:blue_wool",
      "minecraft:blue_wool",
      "minecraft:blue_wool",
      "minecraft:blue_wool",
      None,
      "minecraft:stick",
      None
    ],
    "output": [
      {
        "id": "minecraft:blue_wool",
        "count": 6
      },
      {
        "id": "minecraft:stick",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "blue_bed",
    "input": {
      "item": "minecraft:blue_bed",
      "count": 1
    },
    "output_display": [
      "minecraft:blue_wool",
      "minecraft:blue_wool",
      "minecraft:blue_wool",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:blue_wool",
        "count": 3
      },
      {
        "id": "minecraft:oak_planks",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "blue_candle",
    "input": {
      "item": "minecraft:blue_candle",
      "count": 1
    },
    "output_display": [
      "minecraft:candle",
      "minecraft:blue_dye",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:candle",
        "count": 1
      },
      {
        "id": "minecraft:blue_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "blue_carpet",
    "input": {
      "item": "minecraft:blue_carpet",
      "count": 3
    },
    "output_display": [
      "minecraft:blue_wool",
      "minecraft:blue_wool",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:blue_wool",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "blue_concrete_powder",
    "input": {
      "item": "minecraft:blue_concrete_powder",
      "count": 8
    },
    "output_display": [
      "minecraft:blue_dye",
      "minecraft:sand",
      "minecraft:sand",
      "minecraft:sand",
      "minecraft:sand",
      "minecraft:gravel",
      "minecraft:gravel",
      "minecraft:gravel",
      "minecraft:gravel"
    ],
    "output": [
      {
        "id": "minecraft:blue_dye",
        "count": 1
      },
      {
        "id": "minecraft:sand",
        "count": 4
      },
      {
        "id": "minecraft:gravel",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "blue_dye",
    "input": {
      "item": "minecraft:blue_dye",
      "count": 1
    },
    "output_display": [
      "minecraft:lapis_lazuli",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:lapis_lazuli",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "blue_dye_from_cornflower",
    "input": {
      "item": "minecraft:blue_dye",
      "count": 1
    },
    "output_display": [
      "minecraft:cornflower",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:cornflower",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "blue_ice",
    "input": {
      "item": "minecraft:blue_ice",
      "count": 1
    },
    "output_display": [
      "minecraft:packed_ice",
      "minecraft:packed_ice",
      "minecraft:packed_ice",
      "minecraft:packed_ice",
      "minecraft:packed_ice",
      "minecraft:packed_ice",
      "minecraft:packed_ice",
      "minecraft:packed_ice",
      "minecraft:packed_ice"
    ],
    "output": [
      {
        "id": "minecraft:packed_ice",
        "count": 9
      }
    ]
  },
  {
    "crafting_recipe_name": "blue_stained_glass",
    "input": {
      "item": "minecraft:blue_stained_glass",
      "count": 8
    },
    "output_display": [
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:blue_dye",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass"
    ],
    "output": [
      {
        "id": "minecraft:glass",
        "count": 8
      },
      {
        "id": "minecraft:blue_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "blue_stained_glass_pane",
    "input": {
      "item": "minecraft:blue_stained_glass_pane",
      "count": 16
    },
    "output_display": [
      "minecraft:blue_stained_glass",
      "minecraft:blue_stained_glass",
      "minecraft:blue_stained_glass",
      "minecraft:blue_stained_glass",
      "minecraft:blue_stained_glass",
      "minecraft:blue_stained_glass",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:blue_stained_glass",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "blue_stained_glass_pane_from_glass_pane",
    "input": {
      "item": "minecraft:blue_stained_glass_pane",
      "count": 8
    },
    "output_display": [
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:blue_dye",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane"
    ],
    "output": [
      {
        "id": "minecraft:glass_pane",
        "count": 8
      },
      {
        "id": "minecraft:blue_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "blue_terracotta",
    "input": {
      "item": "minecraft:blue_terracotta",
      "count": 8
    },
    "output_display": [
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:blue_dye",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta"
    ],
    "output": [
      {
        "id": "minecraft:terracotta",
        "count": 8
      },
      {
        "id": "minecraft:blue_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "bolt_armor_trim_smithing_template",
    "input": {
      "item": "minecraft:bolt_armor_trim_smithing_template",
      "count": 2
    },
    "output_display": [
      "minecraft:diamond",
      "minecraft:bolt_armor_trim_smithing_template",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:copper_block",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:diamond"
    ],
    "output": [
      {
        "id": "minecraft:diamond",
        "count": 7
      },
      {
        "id": "minecraft:bolt_armor_trim_smithing_template",
        "count": 1
      },
      {
        "id": "minecraft:copper_block",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "bone_block",
    "input": {
      "item": "minecraft:bone_block",
      "count": 1
    },
    "output_display": [
      "minecraft:bone_meal",
      "minecraft:bone_meal",
      "minecraft:bone_meal",
      "minecraft:bone_meal",
      "minecraft:bone_meal",
      "minecraft:bone_meal",
      "minecraft:bone_meal",
      "minecraft:bone_meal",
      "minecraft:bone_meal"
    ],
    "output": [
      {
        "id": "minecraft:bone_meal",
        "count": 9
      }
    ]
  },
  {
    "crafting_recipe_name": "bone_meal",
    "input": {
      "item": "minecraft:bone_meal",
      "count": 3
    },
    "output_display": [
      "minecraft:bone",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:bone",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "bone_meal_from_bone_block",
    "input": {
      "item": "minecraft:bone_meal",
      "count": 9
    },
    "output_display": [
      "minecraft:bone_block",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:bone_block",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "book",
    "input": {
      "item": "minecraft:book",
      "count": 1
    },
    "output_display": [
      "minecraft:paper",
      "minecraft:paper",
      "minecraft:paper",
      "minecraft:leather",
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:paper",
        "count": 3
      },
      {
        "id": "minecraft:leather",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "bookshelf",
    "input": {
      "item": "minecraft:bookshelf",
      "count": 1
    },
    "output_display": [
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:book",
      "minecraft:book",
      "minecraft:book",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:oak_planks"
    ],
    "output": [
      {
        "id": "minecraft:oak_planks",
        "count": 6
      },
      {
        "id": "minecraft:book",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "bordure_indented_banner_pattern",
    "input": {
      "item": "minecraft:bordure_indented_banner_pattern",
      "count": 1
    },
    "output_display": [
      "minecraft:paper",
      "minecraft:vine",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:paper",
        "count": 1
      },
      {
        "id": "minecraft:vine",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "bow",
    "input": {
      "item": "minecraft:bow",
      "count": 1
    },
    "output_display": [
      None,
      "minecraft:stick",
      "minecraft:string",
      "minecraft:stick",
      None,
      "minecraft:string",
      None,
      "minecraft:stick",
      "minecraft:string"
    ],
    "output": [
      {
        "id": "minecraft:stick",
        "count": 3
      },
      {
        "id": "minecraft:string",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "bowl",
    "input": {
      "item": "minecraft:bowl",
      "count": 4
    },
    "output_display": [
      "minecraft:oak_planks",
      None,
      "minecraft:oak_planks",
      None,
      "minecraft:oak_planks",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:oak_planks",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "bread",
    "input": {
      "item": "minecraft:bread",
      "count": 1
    },
    "output_display": [
      "minecraft:wheat",
      "minecraft:wheat",
      "minecraft:wheat",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:wheat",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "brewing_stand",
    "input": {
      "item": "minecraft:brewing_stand",
      "count": 1
    },
    "output_display": [
      None,
      "minecraft:blaze_rod",
      None,
      "minecraft:cobblestone",
      "minecraft:cobblestone",
      "minecraft:cobblestone",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:blaze_rod",
        "count": 1
      },
      {
        "id": "minecraft:cobblestone",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "bricks",
    "input": {
      "item": "minecraft:bricks",
      "count": 1
    },
    "output_display": [
      "minecraft:brick",
      "minecraft:brick",
      None,
      "minecraft:brick",
      "minecraft:brick",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:brick",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "brick_slab",
    "input": {
      "item": "minecraft:brick_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:bricks",
      "minecraft:bricks",
      "minecraft:bricks",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:bricks",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "brick_stairs",
    "input": {
      "item": "minecraft:brick_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:bricks",
      None,
      None,
      "minecraft:bricks",
      "minecraft:bricks",
      None,
      "minecraft:bricks",
      "minecraft:bricks",
      "minecraft:bricks"
    ],
    "output": [
      {
        "id": "minecraft:bricks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "brick_wall",
    "input": {
      "item": "minecraft:brick_wall",
      "count": 6
    },
    "output_display": [
      "minecraft:bricks",
      "minecraft:bricks",
      "minecraft:bricks",
      "minecraft:bricks",
      "minecraft:bricks",
      "minecraft:bricks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:bricks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "brown_banner",
    "input": {
      "item": "minecraft:brown_banner",
      "count": 1
    },
    "output_display": [
      "minecraft:brown_wool",
      "minecraft:brown_wool",
      "minecraft:brown_wool",
      "minecraft:brown_wool",
      "minecraft:brown_wool",
      "minecraft:brown_wool",
      None,
      "minecraft:stick",
      None
    ],
    "output": [
      {
        "id": "minecraft:brown_wool",
        "count": 6
      },
      {
        "id": "minecraft:stick",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "brown_bed",
    "input": {
      "item": "minecraft:brown_bed",
      "count": 1
    },
    "output_display": [
      "minecraft:brown_wool",
      "minecraft:brown_wool",
      "minecraft:brown_wool",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:brown_wool",
        "count": 3
      },
      {
        "id": "minecraft:oak_planks",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "brown_candle",
    "input": {
      "item": "minecraft:brown_candle",
      "count": 1
    },
    "output_display": [
      "minecraft:candle",
      "minecraft:brown_dye",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:candle",
        "count": 1
      },
      {
        "id": "minecraft:brown_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "brown_carpet",
    "input": {
      "item": "minecraft:brown_carpet",
      "count": 3
    },
    "output_display": [
      "minecraft:brown_wool",
      "minecraft:brown_wool",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:brown_wool",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "brown_concrete_powder",
    "input": {
      "item": "minecraft:brown_concrete_powder",
      "count": 8
    },
    "output_display": [
      "minecraft:brown_dye",
      "minecraft:sand",
      "minecraft:sand",
      "minecraft:sand",
      "minecraft:sand",
      "minecraft:gravel",
      "minecraft:gravel",
      "minecraft:gravel",
      "minecraft:gravel"
    ],
    "output": [
      {
        "id": "minecraft:brown_dye",
        "count": 1
      },
      {
        "id": "minecraft:sand",
        "count": 4
      },
      {
        "id": "minecraft:gravel",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "brown_dye",
    "input": {
      "item": "minecraft:brown_dye",
      "count": 1
    },
    "output_display": [
      "minecraft:cocoa_beans",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:cocoa_beans",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "brown_stained_glass",
    "input": {
      "item": "minecraft:brown_stained_glass",
      "count": 8
    },
    "output_display": [
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:brown_dye",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass"
    ],
    "output": [
      {
        "id": "minecraft:glass",
        "count": 8
      },
      {
        "id": "minecraft:brown_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "brown_stained_glass_pane",
    "input": {
      "item": "minecraft:brown_stained_glass_pane",
      "count": 16
    },
    "output_display": [
      "minecraft:brown_stained_glass",
      "minecraft:brown_stained_glass",
      "minecraft:brown_stained_glass",
      "minecraft:brown_stained_glass",
      "minecraft:brown_stained_glass",
      "minecraft:brown_stained_glass",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:brown_stained_glass",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "brown_stained_glass_pane_from_glass_pane",
    "input": {
      "item": "minecraft:brown_stained_glass_pane",
      "count": 8
    },
    "output_display": [
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:brown_dye",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane"
    ],
    "output": [
      {
        "id": "minecraft:glass_pane",
        "count": 8
      },
      {
        "id": "minecraft:brown_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "brown_terracotta",
    "input": {
      "item": "minecraft:brown_terracotta",
      "count": 8
    },
    "output_display": [
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:brown_dye",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta"
    ],
    "output": [
      {
        "id": "minecraft:terracotta",
        "count": 8
      },
      {
        "id": "minecraft:brown_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "brush",
    "input": {
      "item": "minecraft:brush",
      "count": 1
    },
    "output_display": [
      "minecraft:feather",
      None,
      None,
      "minecraft:copper_ingot",
      None,
      None,
      "minecraft:stick",
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:feather",
        "count": 1
      },
      {
        "id": "minecraft:copper_ingot",
        "count": 1
      },
      {
        "id": "minecraft:stick",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "bucket",
    "input": {
      "item": "minecraft:bucket",
      "count": 1
    },
    "output_display": [
      "minecraft:iron_ingot",
      None,
      "minecraft:iron_ingot",
      None,
      "minecraft:iron_ingot",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:iron_ingot",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "bundle",
    "input": {
      "item": "minecraft:bundle",
      "count": 1
    },
    "output_display": [
      "minecraft:string",
      None,
      None,
      "minecraft:leather",
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:string",
        "count": 1
      },
      {
        "id": "minecraft:leather",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "cake",
    "input": {
      "item": "minecraft:cake",
      "count": 1
    },
    "output_display": [
      "minecraft:milk_bucket",
      "minecraft:milk_bucket",
      "minecraft:milk_bucket",
      "minecraft:sugar",
      "minecraft:egg",
      "minecraft:sugar",
      "minecraft:wheat",
      "minecraft:wheat",
      "minecraft:wheat"
    ],
    "output": [
      {
        "id": "minecraft:milk_bucket",
        "count": 3
      },
      {
        "id": "minecraft:sugar",
        "count": 2
      },
      {
        "id": "minecraft:egg",
        "count": 1
      },
      {
        "id": "minecraft:wheat",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "calibrated_sculk_sensor",
    "input": {
      "item": "minecraft:calibrated_sculk_sensor",
      "count": 1
    },
    "output_display": [
      None,
      "minecraft:amethyst_shard",
      None,
      "minecraft:amethyst_shard",
      "minecraft:sculk_sensor",
      "minecraft:amethyst_shard",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:amethyst_shard",
        "count": 3
      },
      {
        "id": "minecraft:sculk_sensor",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "campfire",
    "input": {
      "item": "minecraft:campfire",
      "count": 1
    },
    "output_display": [
      None,
      "minecraft:stick",
      None,
      "minecraft:stick",
      "#minecraft:coals",
      "minecraft:stick",
      "minecraft:oak_log",
      "minecraft:oak_log",
      "minecraft:oak_log"
    ],
    "output": [
      {
        "id": "minecraft:stick",
        "count": 3
      },
      {
        "id": "#minecraft:coals",
        "count": 1
      },
      {
        "id": "minecraft:oak_log",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "candle",
    "input": {
      "item": "minecraft:candle",
      "count": 1
    },
    "output_display": [
      "minecraft:string",
      None,
      None,
      "minecraft:honeycomb",
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:string",
        "count": 1
      },
      {
        "id": "minecraft:honeycomb",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "carrot_on_a_stick",
    "input": {
      "item": "minecraft:carrot_on_a_stick",
      "count": 1
    },
    "output_display": [
      "minecraft:fishing_rod",
      None,
      None,
      None,
      "minecraft:carrot",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:fishing_rod",
        "count": 1
      },
      {
        "id": "minecraft:carrot",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "cartography_table",
    "input": {
      "item": "minecraft:cartography_table",
      "count": 1
    },
    "output_display": [
      "minecraft:paper",
      "minecraft:paper",
      None,
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      None,
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      None
    ],
    "output": [
      {
        "id": "minecraft:paper",
        "count": 2
      },
      {
        "id": "minecraft:oak_planks",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "cauldron",
    "input": {
      "item": "minecraft:cauldron",
      "count": 1
    },
    "output_display": [
      "minecraft:iron_ingot",
      None,
      "minecraft:iron_ingot",
      "minecraft:iron_ingot",
      None,
      "minecraft:iron_ingot",
      "minecraft:iron_ingot",
      "minecraft:iron_ingot",
      "minecraft:iron_ingot"
    ],
    "output": [
      {
        "id": "minecraft:iron_ingot",
        "count": 7
      }
    ]
  },
  {
    "crafting_recipe_name": "chain",
    "input": {
      "item": "minecraft:chain",
      "count": 1
    },
    "output_display": [
      "minecraft:iron_nugget",
      None,
      None,
      "minecraft:iron_ingot",
      None,
      None,
      "minecraft:iron_nugget",
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:iron_nugget",
        "count": 2
      },
      {
        "id": "minecraft:iron_ingot",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "cherry_boat",
    "input": {
      "item": "minecraft:cherry_boat",
      "count": 1
    },
    "output_display": [
      "minecraft:cherry_planks",
      None,
      "minecraft:cherry_planks",
      "minecraft:cherry_planks",
      "minecraft:cherry_planks",
      "minecraft:cherry_planks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:cherry_planks",
        "count": 5
      }
    ]
  },
  {
    "crafting_recipe_name": "cherry_button",
    "input": {
      "item": "minecraft:cherry_button",
      "count": 1
    },
    "output_display": [
      "minecraft:cherry_planks",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:cherry_planks",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "cherry_chest_boat",
    "input": {
      "item": "minecraft:cherry_chest_boat",
      "count": 1
    },
    "output_display": [
      "minecraft:chest",
      "minecraft:cherry_boat",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:chest",
        "count": 1
      },
      {
        "id": "minecraft:cherry_boat",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "cherry_door",
    "input": {
      "item": "minecraft:cherry_door",
      "count": 3
    },
    "output_display": [
      "minecraft:cherry_planks",
      "minecraft:cherry_planks",
      None,
      "minecraft:cherry_planks",
      "minecraft:cherry_planks",
      None,
      "minecraft:cherry_planks",
      "minecraft:cherry_planks",
      None
    ],
    "output": [
      {
        "id": "minecraft:cherry_planks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "cherry_fence",
    "input": {
      "item": "minecraft:cherry_fence",
      "count": 3
    },
    "output_display": [
      "minecraft:cherry_planks",
      "minecraft:stick",
      "minecraft:cherry_planks",
      "minecraft:cherry_planks",
      "minecraft:stick",
      "minecraft:cherry_planks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:cherry_planks",
        "count": 4
      },
      {
        "id": "minecraft:stick",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "cherry_fence_gate",
    "input": {
      "item": "minecraft:cherry_fence_gate",
      "count": 1
    },
    "output_display": [
      "minecraft:stick",
      "minecraft:cherry_planks",
      "minecraft:stick",
      "minecraft:stick",
      "minecraft:cherry_planks",
      "minecraft:stick",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:stick",
        "count": 4
      },
      {
        "id": "minecraft:cherry_planks",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "cherry_hanging_sign",
    "input": {
      "item": "minecraft:cherry_hanging_sign",
      "count": 6
    },
    "output_display": [
      "minecraft:chain",
      None,
      "minecraft:chain",
      "minecraft:stripped_cherry_log",
      "minecraft:stripped_cherry_log",
      "minecraft:stripped_cherry_log",
      "minecraft:stripped_cherry_log",
      "minecraft:stripped_cherry_log",
      "minecraft:stripped_cherry_log"
    ],
    "output": [
      {
        "id": "minecraft:chain",
        "count": 2
      },
      {
        "id": "minecraft:stripped_cherry_log",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "cherry_planks",
    "input": {
      "item": "minecraft:cherry_planks",
      "count": 4
    },
    "output_display": [
      "minecraft:cherry_log",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:cherry_log",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "cherry_pressure_plate",
    "input": {
      "item": "minecraft:cherry_pressure_plate",
      "count": 1
    },
    "output_display": [
      "minecraft:cherry_planks",
      "minecraft:cherry_planks",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:cherry_planks",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "cherry_sign",
    "input": {
      "item": "minecraft:cherry_sign",
      "count": 3
    },
    "output_display": [
      "minecraft:cherry_planks",
      "minecraft:cherry_planks",
      "minecraft:cherry_planks",
      "minecraft:cherry_planks",
      "minecraft:cherry_planks",
      "minecraft:cherry_planks",
      None,
      "minecraft:stick",
      None
    ],
    "output": [
      {
        "id": "minecraft:cherry_planks",
        "count": 6
      },
      {
        "id": "minecraft:stick",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "cherry_slab",
    "input": {
      "item": "minecraft:cherry_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:cherry_planks",
      "minecraft:cherry_planks",
      "minecraft:cherry_planks",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:cherry_planks",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "cherry_stairs",
    "input": {
      "item": "minecraft:cherry_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:cherry_planks",
      None,
      None,
      "minecraft:cherry_planks",
      "minecraft:cherry_planks",
      None,
      "minecraft:cherry_planks",
      "minecraft:cherry_planks",
      "minecraft:cherry_planks"
    ],
    "output": [
      {
        "id": "minecraft:cherry_planks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "cherry_trapdoor",
    "input": {
      "item": "minecraft:cherry_trapdoor",
      "count": 2
    },
    "output_display": [
      "minecraft:cherry_planks",
      "minecraft:cherry_planks",
      "minecraft:cherry_planks",
      "minecraft:cherry_planks",
      "minecraft:cherry_planks",
      "minecraft:cherry_planks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:cherry_planks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "cherry_wood",
    "input": {
      "item": "minecraft:cherry_wood",
      "count": 3
    },
    "output_display": [
      "minecraft:cherry_log",
      "minecraft:cherry_log",
      None,
      "minecraft:cherry_log",
      "minecraft:cherry_log",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:cherry_log",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "chest",
    "input": {
      "item": "minecraft:chest",
      "count": 1
    },
    "output_display": [
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      None,
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:oak_planks"
    ],
    "output": [
      {
        "id": "minecraft:oak_planks",
        "count": 8
      }
    ]
  },
  {
    "crafting_recipe_name": "chest_minecart",
    "input": {
      "item": "minecraft:chest_minecart",
      "count": 1
    },
    "output_display": [
      "minecraft:chest",
      "minecraft:minecart",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:chest",
        "count": 1
      },
      {
        "id": "minecraft:minecart",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "chiseled_bookshelf",
    "input": {
      "item": "minecraft:chiseled_bookshelf",
      "count": 1
    },
    "output_display": [
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:oak_slab",
      "minecraft:oak_slab",
      "minecraft:oak_slab",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:oak_planks"
    ],
    "output": [
      {
        "id": "minecraft:oak_planks",
        "count": 6
      },
      {
        "id": "minecraft:oak_slab",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "chiseled_copper",
    "input": {
      "item": "minecraft:chiseled_copper",
      "count": 1
    },
    "output_display": [
      "minecraft:cut_copper_slab",
      None,
      None,
      "minecraft:cut_copper_slab",
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:cut_copper_slab",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "chiseled_deepslate",
    "input": {
      "item": "minecraft:chiseled_deepslate",
      "count": 1
    },
    "output_display": [
      "minecraft:cobbled_deepslate_slab",
      None,
      None,
      "minecraft:cobbled_deepslate_slab",
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:cobbled_deepslate_slab",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "chiseled_nether_bricks",
    "input": {
      "item": "minecraft:chiseled_nether_bricks",
      "count": 1
    },
    "output_display": [
      "minecraft:nether_brick_slab",
      None,
      None,
      "minecraft:nether_brick_slab",
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:nether_brick_slab",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "chiseled_polished_blackstone",
    "input": {
      "item": "minecraft:chiseled_polished_blackstone",
      "count": 1
    },
    "output_display": [
      "minecraft:polished_blackstone_slab",
      None,
      None,
      "minecraft:polished_blackstone_slab",
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:polished_blackstone_slab",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "chiseled_quartz_block",
    "input": {
      "item": "minecraft:chiseled_quartz_block",
      "count": 1
    },
    "output_display": [
      "minecraft:quartz_slab",
      None,
      None,
      "minecraft:quartz_slab",
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:quartz_slab",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "chiseled_red_sandstone",
    "input": {
      "item": "minecraft:chiseled_red_sandstone",
      "count": 1
    },
    "output_display": [
      "minecraft:red_sandstone_slab",
      None,
      None,
      "minecraft:red_sandstone_slab",
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:red_sandstone_slab",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "chiseled_resin_bricks",
    "input": {
      "item": "minecraft:chiseled_resin_bricks",
      "count": 1
    },
    "output_display": [
      "minecraft:resin_brick_slab",
      None,
      None,
      "minecraft:resin_brick_slab",
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:resin_brick_slab",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "chiseled_sandstone",
    "input": {
      "item": "minecraft:chiseled_sandstone",
      "count": 1
    },
    "output_display": [
      "minecraft:sandstone_slab",
      None,
      None,
      "minecraft:sandstone_slab",
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:sandstone_slab",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "chiseled_stone_bricks",
    "input": {
      "item": "minecraft:chiseled_stone_bricks",
      "count": 1
    },
    "output_display": [
      "minecraft:stone_brick_slab",
      None,
      None,
      "minecraft:stone_brick_slab",
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:stone_brick_slab",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "chiseled_tuff",
    "input": {
      "item": "minecraft:chiseled_tuff",
      "count": 1
    },
    "output_display": [
      "minecraft:tuff_slab",
      None,
      None,
      "minecraft:tuff_slab",
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:tuff_slab",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "chiseled_tuff_bricks",
    "input": {
      "item": "minecraft:chiseled_tuff_bricks",
      "count": 1
    },
    "output_display": [
      "minecraft:tuff_brick_slab",
      None,
      None,
      "minecraft:tuff_brick_slab",
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:tuff_brick_slab",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "clay",
    "input": {
      "item": "minecraft:clay",
      "count": 1
    },
    "output_display": [
      "minecraft:clay_ball",
      "minecraft:clay_ball",
      None,
      "minecraft:clay_ball",
      "minecraft:clay_ball",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:clay_ball",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "clock",
    "input": {
      "item": "minecraft:clock",
      "count": 1
    },
    "output_display": [
      None,
      "minecraft:gold_ingot",
      None,
      "minecraft:gold_ingot",
      "minecraft:redstone",
      "minecraft:gold_ingot",
      None,
      "minecraft:gold_ingot",
      None
    ],
    "output": [
      {
        "id": "minecraft:gold_ingot",
        "count": 4
      },
      {
        "id": "minecraft:redstone",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "coal",
    "input": {
      "item": "minecraft:coal",
      "count": 9
    },
    "output_display": [
      "minecraft:coal_block",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:coal_block",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "coal_block",
    "input": {
      "item": "minecraft:coal_block",
      "count": 1
    },
    "output_display": [
      "minecraft:coal",
      "minecraft:coal",
      "minecraft:coal",
      "minecraft:coal",
      "minecraft:coal",
      "minecraft:coal",
      "minecraft:coal",
      "minecraft:coal",
      "minecraft:coal"
    ],
    "output": [
      {
        "id": "minecraft:coal",
        "count": 9
      }
    ]
  },
  {
    "crafting_recipe_name": "coarse_dirt",
    "input": {
      "item": "minecraft:coarse_dirt",
      "count": 4
    },
    "output_display": [
      "minecraft:dirt",
      "minecraft:gravel",
      None,
      "minecraft:gravel",
      "minecraft:dirt",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:dirt",
        "count": 2
      },
      {
        "id": "minecraft:gravel",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "coast_armor_trim_smithing_template",
    "input": {
      "item": "minecraft:coast_armor_trim_smithing_template",
      "count": 2
    },
    "output_display": [
      "minecraft:diamond",
      "minecraft:coast_armor_trim_smithing_template",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:cobblestone",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:diamond"
    ],
    "output": [
      {
        "id": "minecraft:diamond",
        "count": 7
      },
      {
        "id": "minecraft:coast_armor_trim_smithing_template",
        "count": 1
      },
      {
        "id": "minecraft:cobblestone",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "cobbled_deepslate_slab",
    "input": {
      "item": "minecraft:cobbled_deepslate_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:cobbled_deepslate",
      "minecraft:cobbled_deepslate",
      "minecraft:cobbled_deepslate",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:cobbled_deepslate",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "cobbled_deepslate_stairs",
    "input": {
      "item": "minecraft:cobbled_deepslate_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:cobbled_deepslate",
      None,
      None,
      "minecraft:cobbled_deepslate",
      "minecraft:cobbled_deepslate",
      None,
      "minecraft:cobbled_deepslate",
      "minecraft:cobbled_deepslate",
      "minecraft:cobbled_deepslate"
    ],
    "output": [
      {
        "id": "minecraft:cobbled_deepslate",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "cobbled_deepslate_wall",
    "input": {
      "item": "minecraft:cobbled_deepslate_wall",
      "count": 6
    },
    "output_display": [
      "minecraft:cobbled_deepslate",
      "minecraft:cobbled_deepslate",
      "minecraft:cobbled_deepslate",
      "minecraft:cobbled_deepslate",
      "minecraft:cobbled_deepslate",
      "minecraft:cobbled_deepslate",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:cobbled_deepslate",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "cobblestone_slab",
    "input": {
      "item": "minecraft:cobblestone_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:cobblestone",
      "minecraft:cobblestone",
      "minecraft:cobblestone",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:cobblestone",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "cobblestone_stairs",
    "input": {
      "item": "minecraft:cobblestone_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:cobblestone",
      None,
      None,
      "minecraft:cobblestone",
      "minecraft:cobblestone",
      None,
      "minecraft:cobblestone",
      "minecraft:cobblestone",
      "minecraft:cobblestone"
    ],
    "output": [
      {
        "id": "minecraft:cobblestone",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "cobblestone_wall",
    "input": {
      "item": "minecraft:cobblestone_wall",
      "count": 6
    },
    "output_display": [
      "minecraft:cobblestone",
      "minecraft:cobblestone",
      "minecraft:cobblestone",
      "minecraft:cobblestone",
      "minecraft:cobblestone",
      "minecraft:cobblestone",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:cobblestone",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "comparator",
    "input": {
      "item": "minecraft:comparator",
      "count": 1
    },
    "output_display": [
      None,
      "minecraft:redstone_torch",
      None,
      "minecraft:redstone_torch",
      "minecraft:quartz",
      "minecraft:redstone_torch",
      "minecraft:stone",
      "minecraft:stone",
      "minecraft:stone"
    ],
    "output": [
      {
        "id": "minecraft:redstone_torch",
        "count": 3
      },
      {
        "id": "minecraft:quartz",
        "count": 1
      },
      {
        "id": "minecraft:stone",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "compass",
    "input": {
      "item": "minecraft:compass",
      "count": 1
    },
    "output_display": [
      None,
      "minecraft:iron_ingot",
      None,
      "minecraft:iron_ingot",
      "minecraft:redstone",
      "minecraft:iron_ingot",
      None,
      "minecraft:iron_ingot",
      None
    ],
    "output": [
      {
        "id": "minecraft:iron_ingot",
        "count": 4
      },
      {
        "id": "minecraft:redstone",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "composter",
    "input": {
      "item": "minecraft:composter",
      "count": 1
    },
    "output_display": [
      "minecraft:oak_slab",
      None,
      "minecraft:oak_slab",
      "minecraft:oak_slab",
      None,
      "minecraft:oak_slab",
      "minecraft:oak_slab",
      "minecraft:oak_slab",
      "minecraft:oak_slab"
    ],
    "output": [
      {
        "id": "minecraft:oak_slab",
        "count": 7
      }
    ]
  },
  {
    "crafting_recipe_name": "conduit",
    "input": {
      "item": "minecraft:conduit",
      "count": 1
    },
    "output_display": [
      "minecraft:nautilus_shell",
      "minecraft:nautilus_shell",
      "minecraft:nautilus_shell",
      "minecraft:nautilus_shell",
      "minecraft:heart_of_the_sea",
      "minecraft:nautilus_shell",
      "minecraft:nautilus_shell",
      "minecraft:nautilus_shell",
      "minecraft:nautilus_shell"
    ],
    "output": [
      {
        "id": "minecraft:nautilus_shell",
        "count": 8
      },
      {
        "id": "minecraft:heart_of_the_sea",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "cookie",
    "input": {
      "item": "minecraft:cookie",
      "count": 8
    },
    "output_display": [
      "minecraft:wheat",
      "minecraft:cocoa_beans",
      "minecraft:wheat",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:wheat",
        "count": 2
      },
      {
        "id": "minecraft:cocoa_beans",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "copper_block",
    "input": {
      "item": "minecraft:copper_block",
      "count": 1
    },
    "output_display": [
      "minecraft:copper_ingot",
      "minecraft:copper_ingot",
      "minecraft:copper_ingot",
      "minecraft:copper_ingot",
      "minecraft:copper_ingot",
      "minecraft:copper_ingot",
      "minecraft:copper_ingot",
      "minecraft:copper_ingot",
      "minecraft:copper_ingot"
    ],
    "output": [
      {
        "id": "minecraft:copper_ingot",
        "count": 9
      }
    ]
  },
  {
    "crafting_recipe_name": "copper_bulb",
    "input": {
      "item": "minecraft:copper_bulb",
      "count": 4
    },
    "output_display": [
      None,
      "minecraft:copper_block",
      None,
      "minecraft:copper_block",
      "minecraft:blaze_rod",
      "minecraft:copper_block",
      None,
      "minecraft:redstone",
      None
    ],
    "output": [
      {
        "id": "minecraft:copper_block",
        "count": 3
      },
      {
        "id": "minecraft:blaze_rod",
        "count": 1
      },
      {
        "id": "minecraft:redstone",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "copper_door",
    "input": {
      "item": "minecraft:copper_door",
      "count": 3
    },
    "output_display": [
      "minecraft:copper_ingot",
      "minecraft:copper_ingot",
      None,
      "minecraft:copper_ingot",
      "minecraft:copper_ingot",
      None,
      "minecraft:copper_ingot",
      "minecraft:copper_ingot",
      None
    ],
    "output": [
      {
        "id": "minecraft:copper_ingot",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "copper_grate",
    "input": {
      "item": "minecraft:copper_grate",
      "count": 4
    },
    "output_display": [
      None,
      "minecraft:copper_block",
      None,
      "minecraft:copper_block",
      None,
      "minecraft:copper_block",
      None,
      "minecraft:copper_block",
      None
    ],
    "output": [
      {
        "id": "minecraft:copper_block",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "copper_ingot",
    "input": {
      "item": "minecraft:copper_ingot",
      "count": 9
    },
    "output_display": [
      "minecraft:copper_block",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:copper_block",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "copper_ingot_from_waxed_copper_block",
    "input": {
      "item": "minecraft:copper_ingot",
      "count": 9
    },
    "output_display": [
      "minecraft:waxed_copper_block",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:waxed_copper_block",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "copper_trapdoor",
    "input": {
      "item": "minecraft:copper_trapdoor",
      "count": 2
    },
    "output_display": [
      "minecraft:copper_ingot",
      "minecraft:copper_ingot",
      "minecraft:copper_ingot",
      "minecraft:copper_ingot",
      "minecraft:copper_ingot",
      "minecraft:copper_ingot",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:copper_ingot",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "crafter",
    "input": {
      "item": "minecraft:crafter",
      "count": 1
    },
    "output_display": [
      "minecraft:iron_ingot",
      "minecraft:iron_ingot",
      "minecraft:iron_ingot",
      "minecraft:iron_ingot",
      "minecraft:crafting_table",
      "minecraft:iron_ingot",
      "minecraft:redstone",
      "minecraft:dropper",
      "minecraft:redstone"
    ],
    "output": [
      {
        "id": "minecraft:iron_ingot",
        "count": 5
      },
      {
        "id": "minecraft:crafting_table",
        "count": 1
      },
      {
        "id": "minecraft:redstone",
        "count": 2
      },
      {
        "id": "minecraft:dropper",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "crafting_table",
    "input": {
      "item": "minecraft:crafting_table",
      "count": 1
    },
    "output_display": [
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      None,
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:oak_planks",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "creaking_heart",
    "input": {
      "item": "minecraft:creaking_heart",
      "count": 1
    },
    "output_display": [
      None,
      "minecraft:pale_oak_log",
      None,
      None,
      "minecraft:resin_block",
      None,
      None,
      "minecraft:pale_oak_log",
      None
    ],
    "output": [
      {
        "id": "minecraft:pale_oak_log",
        "count": 2
      },
      {
        "id": "minecraft:resin_block",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "creeper_banner_pattern",
    "input": {
      "item": "minecraft:creeper_banner_pattern",
      "count": 1
    },
    "output_display": [
      "minecraft:paper",
      "minecraft:creeper_head",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:paper",
        "count": 1
      },
      {
        "id": "minecraft:creeper_head",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "crimson_button",
    "input": {
      "item": "minecraft:crimson_button",
      "count": 1
    },
    "output_display": [
      "minecraft:crimson_planks",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:crimson_planks",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "crimson_door",
    "input": {
      "item": "minecraft:crimson_door",
      "count": 3
    },
    "output_display": [
      "minecraft:crimson_planks",
      "minecraft:crimson_planks",
      None,
      "minecraft:crimson_planks",
      "minecraft:crimson_planks",
      None,
      "minecraft:crimson_planks",
      "minecraft:crimson_planks",
      None
    ],
    "output": [
      {
        "id": "minecraft:crimson_planks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "crimson_fence",
    "input": {
      "item": "minecraft:crimson_fence",
      "count": 3
    },
    "output_display": [
      "minecraft:crimson_planks",
      "minecraft:stick",
      "minecraft:crimson_planks",
      "minecraft:crimson_planks",
      "minecraft:stick",
      "minecraft:crimson_planks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:crimson_planks",
        "count": 4
      },
      {
        "id": "minecraft:stick",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "crimson_fence_gate",
    "input": {
      "item": "minecraft:crimson_fence_gate",
      "count": 1
    },
    "output_display": [
      "minecraft:stick",
      "minecraft:crimson_planks",
      "minecraft:stick",
      "minecraft:stick",
      "minecraft:crimson_planks",
      "minecraft:stick",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:stick",
        "count": 4
      },
      {
        "id": "minecraft:crimson_planks",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "crimson_hanging_sign",
    "input": {
      "item": "minecraft:crimson_hanging_sign",
      "count": 6
    },
    "output_display": [
      "minecraft:chain",
      None,
      "minecraft:chain",
      "minecraft:stripped_crimson_stem",
      "minecraft:stripped_crimson_stem",
      "minecraft:stripped_crimson_stem",
      "minecraft:stripped_crimson_stem",
      "minecraft:stripped_crimson_stem",
      "minecraft:stripped_crimson_stem"
    ],
    "output": [
      {
        "id": "minecraft:chain",
        "count": 2
      },
      {
        "id": "minecraft:stripped_crimson_stem",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "crimson_hyphae",
    "input": {
      "item": "minecraft:crimson_hyphae",
      "count": 3
    },
    "output_display": [
      "minecraft:crimson_stem",
      "minecraft:crimson_stem",
      None,
      "minecraft:crimson_stem",
      "minecraft:crimson_stem",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:crimson_stem",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "crimson_planks",
    "input": {
      "item": "minecraft:crimson_planks",
      "count": 4
    },
    "output_display": [
      "minecraft:crimson_stem",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:crimson_stem",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "crimson_pressure_plate",
    "input": {
      "item": "minecraft:crimson_pressure_plate",
      "count": 1
    },
    "output_display": [
      "minecraft:crimson_planks",
      "minecraft:crimson_planks",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:crimson_planks",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "crimson_sign",
    "input": {
      "item": "minecraft:crimson_sign",
      "count": 3
    },
    "output_display": [
      "minecraft:crimson_planks",
      "minecraft:crimson_planks",
      "minecraft:crimson_planks",
      "minecraft:crimson_planks",
      "minecraft:crimson_planks",
      "minecraft:crimson_planks",
      None,
      "minecraft:stick",
      None
    ],
    "output": [
      {
        "id": "minecraft:crimson_planks",
        "count": 6
      },
      {
        "id": "minecraft:stick",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "crimson_slab",
    "input": {
      "item": "minecraft:crimson_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:crimson_planks",
      "minecraft:crimson_planks",
      "minecraft:crimson_planks",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:crimson_planks",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "crimson_stairs",
    "input": {
      "item": "minecraft:crimson_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:crimson_planks",
      None,
      None,
      "minecraft:crimson_planks",
      "minecraft:crimson_planks",
      None,
      "minecraft:crimson_planks",
      "minecraft:crimson_planks",
      "minecraft:crimson_planks"
    ],
    "output": [
      {
        "id": "minecraft:crimson_planks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "crimson_trapdoor",
    "input": {
      "item": "minecraft:crimson_trapdoor",
      "count": 2
    },
    "output_display": [
      "minecraft:crimson_planks",
      "minecraft:crimson_planks",
      "minecraft:crimson_planks",
      "minecraft:crimson_planks",
      "minecraft:crimson_planks",
      "minecraft:crimson_planks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:crimson_planks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "crossbow",
    "input": {
      "item": "minecraft:crossbow",
      "count": 1
    },
    "output_display": [
      "minecraft:stick",
      "minecraft:iron_ingot",
      "minecraft:stick",
      "minecraft:string",
      "minecraft:tripwire_hook",
      "minecraft:string",
      None,
      "minecraft:stick",
      None
    ],
    "output": [
      {
        "id": "minecraft:stick",
        "count": 3
      },
      {
        "id": "minecraft:iron_ingot",
        "count": 1
      },
      {
        "id": "minecraft:string",
        "count": 2
      },
      {
        "id": "minecraft:tripwire_hook",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "cut_copper",
    "input": {
      "item": "minecraft:cut_copper",
      "count": 4
    },
    "output_display": [
      "minecraft:copper_block",
      "minecraft:copper_block",
      None,
      "minecraft:copper_block",
      "minecraft:copper_block",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:copper_block",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "cut_copper_slab",
    "input": {
      "item": "minecraft:cut_copper_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:cut_copper",
      "minecraft:cut_copper",
      "minecraft:cut_copper",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:cut_copper",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "cut_copper_stairs",
    "input": {
      "item": "minecraft:cut_copper_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:cut_copper",
      None,
      None,
      "minecraft:cut_copper",
      "minecraft:cut_copper",
      None,
      "minecraft:cut_copper",
      "minecraft:cut_copper",
      "minecraft:cut_copper"
    ],
    "output": [
      {
        "id": "minecraft:cut_copper",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "cut_red_sandstone",
    "input": {
      "item": "minecraft:cut_red_sandstone",
      "count": 4
    },
    "output_display": [
      "minecraft:red_sandstone",
      "minecraft:red_sandstone",
      None,
      "minecraft:red_sandstone",
      "minecraft:red_sandstone",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:red_sandstone",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "cut_red_sandstone_slab",
    "input": {
      "item": "minecraft:cut_red_sandstone_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:cut_red_sandstone",
      "minecraft:cut_red_sandstone",
      "minecraft:cut_red_sandstone",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:cut_red_sandstone",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "cut_sandstone",
    "input": {
      "item": "minecraft:cut_sandstone",
      "count": 4
    },
    "output_display": [
      "minecraft:sandstone",
      "minecraft:sandstone",
      None,
      "minecraft:sandstone",
      "minecraft:sandstone",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:sandstone",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "cut_sandstone_slab",
    "input": {
      "item": "minecraft:cut_sandstone_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:cut_sandstone",
      "minecraft:cut_sandstone",
      "minecraft:cut_sandstone",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:cut_sandstone",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "cyan_banner",
    "input": {
      "item": "minecraft:cyan_banner",
      "count": 1
    },
    "output_display": [
      "minecraft:cyan_wool",
      "minecraft:cyan_wool",
      "minecraft:cyan_wool",
      "minecraft:cyan_wool",
      "minecraft:cyan_wool",
      "minecraft:cyan_wool",
      None,
      "minecraft:stick",
      None
    ],
    "output": [
      {
        "id": "minecraft:cyan_wool",
        "count": 6
      },
      {
        "id": "minecraft:stick",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "cyan_bed",
    "input": {
      "item": "minecraft:cyan_bed",
      "count": 1
    },
    "output_display": [
      "minecraft:cyan_wool",
      "minecraft:cyan_wool",
      "minecraft:cyan_wool",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:cyan_wool",
        "count": 3
      },
      {
        "id": "minecraft:oak_planks",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "cyan_candle",
    "input": {
      "item": "minecraft:cyan_candle",
      "count": 1
    },
    "output_display": [
      "minecraft:candle",
      "minecraft:cyan_dye",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:candle",
        "count": 1
      },
      {
        "id": "minecraft:cyan_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "cyan_carpet",
    "input": {
      "item": "minecraft:cyan_carpet",
      "count": 3
    },
    "output_display": [
      "minecraft:cyan_wool",
      "minecraft:cyan_wool",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:cyan_wool",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "cyan_concrete_powder",
    "input": {
      "item": "minecraft:cyan_concrete_powder",
      "count": 8
    },
    "output_display": [
      "minecraft:cyan_dye",
      "minecraft:sand",
      "minecraft:sand",
      "minecraft:sand",
      "minecraft:sand",
      "minecraft:gravel",
      "minecraft:gravel",
      "minecraft:gravel",
      "minecraft:gravel"
    ],
    "output": [
      {
        "id": "minecraft:cyan_dye",
        "count": 1
      },
      {
        "id": "minecraft:sand",
        "count": 4
      },
      {
        "id": "minecraft:gravel",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "cyan_dye",
    "input": {
      "item": "minecraft:cyan_dye",
      "count": 2
    },
    "output_display": [
      "minecraft:blue_dye",
      "minecraft:green_dye",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:blue_dye",
        "count": 1
      },
      {
        "id": "minecraft:green_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "cyan_dye_from_pitcher_plant",
    "input": {
      "item": "minecraft:cyan_dye",
      "count": 2
    },
    "output_display": [
      "minecraft:pitcher_plant",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:pitcher_plant",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "cyan_stained_glass",
    "input": {
      "item": "minecraft:cyan_stained_glass",
      "count": 8
    },
    "output_display": [
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:cyan_dye",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass"
    ],
    "output": [
      {
        "id": "minecraft:glass",
        "count": 8
      },
      {
        "id": "minecraft:cyan_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "cyan_stained_glass_pane",
    "input": {
      "item": "minecraft:cyan_stained_glass_pane",
      "count": 16
    },
    "output_display": [
      "minecraft:cyan_stained_glass",
      "minecraft:cyan_stained_glass",
      "minecraft:cyan_stained_glass",
      "minecraft:cyan_stained_glass",
      "minecraft:cyan_stained_glass",
      "minecraft:cyan_stained_glass",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:cyan_stained_glass",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "cyan_stained_glass_pane_from_glass_pane",
    "input": {
      "item": "minecraft:cyan_stained_glass_pane",
      "count": 8
    },
    "output_display": [
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:cyan_dye",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane"
    ],
    "output": [
      {
        "id": "minecraft:glass_pane",
        "count": 8
      },
      {
        "id": "minecraft:cyan_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "cyan_terracotta",
    "input": {
      "item": "minecraft:cyan_terracotta",
      "count": 8
    },
    "output_display": [
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:cyan_dye",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta"
    ],
    "output": [
      {
        "id": "minecraft:terracotta",
        "count": 8
      },
      {
        "id": "minecraft:cyan_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dark_oak_boat",
    "input": {
      "item": "minecraft:dark_oak_boat",
      "count": 1
    },
    "output_display": [
      "minecraft:dark_oak_planks",
      None,
      "minecraft:dark_oak_planks",
      "minecraft:dark_oak_planks",
      "minecraft:dark_oak_planks",
      "minecraft:dark_oak_planks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:dark_oak_planks",
        "count": 5
      }
    ]
  },
  {
    "crafting_recipe_name": "dark_oak_button",
    "input": {
      "item": "minecraft:dark_oak_button",
      "count": 1
    },
    "output_display": [
      "minecraft:dark_oak_planks",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:dark_oak_planks",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dark_oak_chest_boat",
    "input": {
      "item": "minecraft:dark_oak_chest_boat",
      "count": 1
    },
    "output_display": [
      "minecraft:chest",
      "minecraft:dark_oak_boat",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:chest",
        "count": 1
      },
      {
        "id": "minecraft:dark_oak_boat",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dark_oak_door",
    "input": {
      "item": "minecraft:dark_oak_door",
      "count": 3
    },
    "output_display": [
      "minecraft:dark_oak_planks",
      "minecraft:dark_oak_planks",
      None,
      "minecraft:dark_oak_planks",
      "minecraft:dark_oak_planks",
      None,
      "minecraft:dark_oak_planks",
      "minecraft:dark_oak_planks",
      None
    ],
    "output": [
      {
        "id": "minecraft:dark_oak_planks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "dark_oak_fence",
    "input": {
      "item": "minecraft:dark_oak_fence",
      "count": 3
    },
    "output_display": [
      "minecraft:dark_oak_planks",
      "minecraft:stick",
      "minecraft:dark_oak_planks",
      "minecraft:dark_oak_planks",
      "minecraft:stick",
      "minecraft:dark_oak_planks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:dark_oak_planks",
        "count": 4
      },
      {
        "id": "minecraft:stick",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "dark_oak_fence_gate",
    "input": {
      "item": "minecraft:dark_oak_fence_gate",
      "count": 1
    },
    "output_display": [
      "minecraft:stick",
      "minecraft:dark_oak_planks",
      "minecraft:stick",
      "minecraft:stick",
      "minecraft:dark_oak_planks",
      "minecraft:stick",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:stick",
        "count": 4
      },
      {
        "id": "minecraft:dark_oak_planks",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "dark_oak_hanging_sign",
    "input": {
      "item": "minecraft:dark_oak_hanging_sign",
      "count": 6
    },
    "output_display": [
      "minecraft:chain",
      None,
      "minecraft:chain",
      "minecraft:stripped_dark_oak_log",
      "minecraft:stripped_dark_oak_log",
      "minecraft:stripped_dark_oak_log",
      "minecraft:stripped_dark_oak_log",
      "minecraft:stripped_dark_oak_log",
      "minecraft:stripped_dark_oak_log"
    ],
    "output": [
      {
        "id": "minecraft:chain",
        "count": 2
      },
      {
        "id": "minecraft:stripped_dark_oak_log",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "dark_oak_planks",
    "input": {
      "item": "minecraft:dark_oak_planks",
      "count": 4
    },
    "output_display": [
      "minecraft:dark_oak_log",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:dark_oak_log",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dark_oak_pressure_plate",
    "input": {
      "item": "minecraft:dark_oak_pressure_plate",
      "count": 1
    },
    "output_display": [
      "minecraft:dark_oak_planks",
      "minecraft:dark_oak_planks",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:dark_oak_planks",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "dark_oak_sign",
    "input": {
      "item": "minecraft:dark_oak_sign",
      "count": 3
    },
    "output_display": [
      "minecraft:dark_oak_planks",
      "minecraft:dark_oak_planks",
      "minecraft:dark_oak_planks",
      "minecraft:dark_oak_planks",
      "minecraft:dark_oak_planks",
      "minecraft:dark_oak_planks",
      None,
      "minecraft:stick",
      None
    ],
    "output": [
      {
        "id": "minecraft:dark_oak_planks",
        "count": 6
      },
      {
        "id": "minecraft:stick",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dark_oak_slab",
    "input": {
      "item": "minecraft:dark_oak_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:dark_oak_planks",
      "minecraft:dark_oak_planks",
      "minecraft:dark_oak_planks",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:dark_oak_planks",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "dark_oak_stairs",
    "input": {
      "item": "minecraft:dark_oak_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:dark_oak_planks",
      None,
      None,
      "minecraft:dark_oak_planks",
      "minecraft:dark_oak_planks",
      None,
      "minecraft:dark_oak_planks",
      "minecraft:dark_oak_planks",
      "minecraft:dark_oak_planks"
    ],
    "output": [
      {
        "id": "minecraft:dark_oak_planks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "dark_oak_trapdoor",
    "input": {
      "item": "minecraft:dark_oak_trapdoor",
      "count": 2
    },
    "output_display": [
      "minecraft:dark_oak_planks",
      "minecraft:dark_oak_planks",
      "minecraft:dark_oak_planks",
      "minecraft:dark_oak_planks",
      "minecraft:dark_oak_planks",
      "minecraft:dark_oak_planks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:dark_oak_planks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "dark_oak_wood",
    "input": {
      "item": "minecraft:dark_oak_wood",
      "count": 3
    },
    "output_display": [
      "minecraft:dark_oak_log",
      "minecraft:dark_oak_log",
      None,
      "minecraft:dark_oak_log",
      "minecraft:dark_oak_log",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:dark_oak_log",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "dark_prismarine",
    "input": {
      "item": "minecraft:dark_prismarine",
      "count": 1
    },
    "output_display": [
      "minecraft:prismarine_shard",
      "minecraft:prismarine_shard",
      "minecraft:prismarine_shard",
      "minecraft:prismarine_shard",
      "minecraft:black_dye",
      "minecraft:prismarine_shard",
      "minecraft:prismarine_shard",
      "minecraft:prismarine_shard",
      "minecraft:prismarine_shard"
    ],
    "output": [
      {
        "id": "minecraft:prismarine_shard",
        "count": 8
      },
      {
        "id": "minecraft:black_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dark_prismarine_slab",
    "input": {
      "item": "minecraft:dark_prismarine_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:dark_prismarine",
      "minecraft:dark_prismarine",
      "minecraft:dark_prismarine",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:dark_prismarine",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "dark_prismarine_stairs",
    "input": {
      "item": "minecraft:dark_prismarine_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:dark_prismarine",
      None,
      None,
      "minecraft:dark_prismarine",
      "minecraft:dark_prismarine",
      None,
      "minecraft:dark_prismarine",
      "minecraft:dark_prismarine",
      "minecraft:dark_prismarine"
    ],
    "output": [
      {
        "id": "minecraft:dark_prismarine",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "daylight_detector",
    "input": {
      "item": "minecraft:daylight_detector",
      "count": 1
    },
    "output_display": [
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:quartz",
      "minecraft:quartz",
      "minecraft:quartz",
      "minecraft:oak_slab",
      "minecraft:oak_slab",
      "minecraft:oak_slab"
    ],
    "output": [
      {
        "id": "minecraft:glass",
        "count": 3
      },
      {
        "id": "minecraft:quartz",
        "count": 3
      },
      {
        "id": "minecraft:oak_slab",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "decorated_pot_simple",
    "input": {
      "item": "minecraft:decorated_pot",
      "count": 1
    },
    "output_display": [
      None,
      "minecraft:brick",
      None,
      "minecraft:brick",
      None,
      "minecraft:brick",
      None,
      "minecraft:brick",
      None
    ],
    "output": [
      {
        "id": "minecraft:brick",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "deepslate_bricks",
    "input": {
      "item": "minecraft:deepslate_bricks",
      "count": 4
    },
    "output_display": [
      "minecraft:polished_deepslate",
      "minecraft:polished_deepslate",
      None,
      "minecraft:polished_deepslate",
      "minecraft:polished_deepslate",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:polished_deepslate",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "deepslate_brick_slab",
    "input": {
      "item": "minecraft:deepslate_brick_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:deepslate_bricks",
      "minecraft:deepslate_bricks",
      "minecraft:deepslate_bricks",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:deepslate_bricks",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "deepslate_brick_stairs",
    "input": {
      "item": "minecraft:deepslate_brick_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:deepslate_bricks",
      None,
      None,
      "minecraft:deepslate_bricks",
      "minecraft:deepslate_bricks",
      None,
      "minecraft:deepslate_bricks",
      "minecraft:deepslate_bricks",
      "minecraft:deepslate_bricks"
    ],
    "output": [
      {
        "id": "minecraft:deepslate_bricks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "deepslate_brick_wall",
    "input": {
      "item": "minecraft:deepslate_brick_wall",
      "count": 6
    },
    "output_display": [
      "minecraft:deepslate_bricks",
      "minecraft:deepslate_bricks",
      "minecraft:deepslate_bricks",
      "minecraft:deepslate_bricks",
      "minecraft:deepslate_bricks",
      "minecraft:deepslate_bricks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:deepslate_bricks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "deepslate_tiles",
    "input": {
      "item": "minecraft:deepslate_tiles",
      "count": 4
    },
    "output_display": [
      "minecraft:deepslate_bricks",
      "minecraft:deepslate_bricks",
      None,
      "minecraft:deepslate_bricks",
      "minecraft:deepslate_bricks",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:deepslate_bricks",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "deepslate_tile_slab",
    "input": {
      "item": "minecraft:deepslate_tile_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:deepslate_tiles",
      "minecraft:deepslate_tiles",
      "minecraft:deepslate_tiles",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:deepslate_tiles",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "deepslate_tile_stairs",
    "input": {
      "item": "minecraft:deepslate_tile_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:deepslate_tiles",
      None,
      None,
      "minecraft:deepslate_tiles",
      "minecraft:deepslate_tiles",
      None,
      "minecraft:deepslate_tiles",
      "minecraft:deepslate_tiles",
      "minecraft:deepslate_tiles"
    ],
    "output": [
      {
        "id": "minecraft:deepslate_tiles",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "deepslate_tile_wall",
    "input": {
      "item": "minecraft:deepslate_tile_wall",
      "count": 6
    },
    "output_display": [
      "minecraft:deepslate_tiles",
      "minecraft:deepslate_tiles",
      "minecraft:deepslate_tiles",
      "minecraft:deepslate_tiles",
      "minecraft:deepslate_tiles",
      "minecraft:deepslate_tiles",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:deepslate_tiles",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "detector_rail",
    "input": {
      "item": "minecraft:detector_rail",
      "count": 6
    },
    "output_display": [
      "minecraft:iron_ingot",
      None,
      "minecraft:iron_ingot",
      "minecraft:iron_ingot",
      "minecraft:stone_pressure_plate",
      "minecraft:iron_ingot",
      "minecraft:iron_ingot",
      "minecraft:redstone",
      "minecraft:iron_ingot"
    ],
    "output": [
      {
        "id": "minecraft:iron_ingot",
        "count": 6
      },
      {
        "id": "minecraft:stone_pressure_plate",
        "count": 1
      },
      {
        "id": "minecraft:redstone",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "diamond",
    "input": {
      "item": "minecraft:diamond",
      "count": 9
    },
    "output_display": [
      "minecraft:diamond_block",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:diamond_block",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "diamond_axe",
    "input": {
      "item": "minecraft:diamond_axe",
      "count": 1
    },
    "output_display": [
      "#minecraft:diamond_tool_materials",
      "#minecraft:diamond_tool_materials",
      None,
      "#minecraft:diamond_tool_materials",
      "minecraft:stick",
      None,
      None,
      "minecraft:stick",
      None
    ],
    "output": [
      {
        "id": "#minecraft:diamond_tool_materials",
        "count": 3
      },
      {
        "id": "minecraft:stick",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "diamond_block",
    "input": {
      "item": "minecraft:diamond_block",
      "count": 1
    },
    "output_display": [
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:diamond"
    ],
    "output": [
      {
        "id": "minecraft:diamond",
        "count": 9
      }
    ]
  },
  {
    "crafting_recipe_name": "diamond_boots",
    "input": {
      "item": "minecraft:diamond_boots",
      "count": 1
    },
    "output_display": [
      "minecraft:diamond",
      None,
      "minecraft:diamond",
      "minecraft:diamond",
      None,
      "minecraft:diamond",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:diamond",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "diamond_chestplate",
    "input": {
      "item": "minecraft:diamond_chestplate",
      "count": 1
    },
    "output_display": [
      "minecraft:diamond",
      None,
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:diamond"
    ],
    "output": [
      {
        "id": "minecraft:diamond",
        "count": 8
      }
    ]
  },
  {
    "crafting_recipe_name": "diamond_helmet",
    "input": {
      "item": "minecraft:diamond_helmet",
      "count": 1
    },
    "output_display": [
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:diamond",
      None,
      "minecraft:diamond",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:diamond",
        "count": 5
      }
    ]
  },
  {
    "crafting_recipe_name": "diamond_hoe",
    "input": {
      "item": "minecraft:diamond_hoe",
      "count": 1
    },
    "output_display": [
      "#minecraft:diamond_tool_materials",
      "#minecraft:diamond_tool_materials",
      None,
      None,
      "minecraft:stick",
      None,
      None,
      "minecraft:stick",
      None
    ],
    "output": [
      {
        "id": "#minecraft:diamond_tool_materials",
        "count": 2
      },
      {
        "id": "minecraft:stick",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "diamond_leggings",
    "input": {
      "item": "minecraft:diamond_leggings",
      "count": 1
    },
    "output_display": [
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:diamond",
      None,
      "minecraft:diamond",
      "minecraft:diamond",
      None,
      "minecraft:diamond"
    ],
    "output": [
      {
        "id": "minecraft:diamond",
        "count": 7
      }
    ]
  },
  {
    "crafting_recipe_name": "diamond_pickaxe",
    "input": {
      "item": "minecraft:diamond_pickaxe",
      "count": 1
    },
    "output_display": [
      "#minecraft:diamond_tool_materials",
      "#minecraft:diamond_tool_materials",
      "#minecraft:diamond_tool_materials",
      None,
      "minecraft:stick",
      None,
      None,
      "minecraft:stick",
      None
    ],
    "output": [
      {
        "id": "#minecraft:diamond_tool_materials",
        "count": 3
      },
      {
        "id": "minecraft:stick",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "diamond_shovel",
    "input": {
      "item": "minecraft:diamond_shovel",
      "count": 1
    },
    "output_display": [
      "#minecraft:diamond_tool_materials",
      None,
      None,
      "minecraft:stick",
      None,
      None,
      "minecraft:stick",
      None,
      None
    ],
    "output": [
      {
        "id": "#minecraft:diamond_tool_materials",
        "count": 1
      },
      {
        "id": "minecraft:stick",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "diamond_sword",
    "input": {
      "item": "minecraft:diamond_sword",
      "count": 1
    },
    "output_display": [
      "#minecraft:diamond_tool_materials",
      None,
      None,
      "#minecraft:diamond_tool_materials",
      None,
      None,
      "minecraft:stick",
      None,
      None
    ],
    "output": [
      {
        "id": "#minecraft:diamond_tool_materials",
        "count": 2
      },
      {
        "id": "minecraft:stick",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "diorite",
    "input": {
      "item": "minecraft:diorite",
      "count": 2
    },
    "output_display": [
      "minecraft:cobblestone",
      "minecraft:quartz",
      None,
      "minecraft:quartz",
      "minecraft:cobblestone",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:cobblestone",
        "count": 2
      },
      {
        "id": "minecraft:quartz",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "diorite_slab",
    "input": {
      "item": "minecraft:diorite_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:diorite",
      "minecraft:diorite",
      "minecraft:diorite",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:diorite",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "diorite_stairs",
    "input": {
      "item": "minecraft:diorite_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:diorite",
      None,
      None,
      "minecraft:diorite",
      "minecraft:diorite",
      None,
      "minecraft:diorite",
      "minecraft:diorite",
      "minecraft:diorite"
    ],
    "output": [
      {
        "id": "minecraft:diorite",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "diorite_wall",
    "input": {
      "item": "minecraft:diorite_wall",
      "count": 6
    },
    "output_display": [
      "minecraft:diorite",
      "minecraft:diorite",
      "minecraft:diorite",
      "minecraft:diorite",
      "minecraft:diorite",
      "minecraft:diorite",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:diorite",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "dispenser",
    "input": {
      "item": "minecraft:dispenser",
      "count": 1
    },
    "output_display": [
      "minecraft:cobblestone",
      "minecraft:cobblestone",
      "minecraft:cobblestone",
      "minecraft:cobblestone",
      "minecraft:bow",
      "minecraft:cobblestone",
      "minecraft:cobblestone",
      "minecraft:redstone",
      "minecraft:cobblestone"
    ],
    "output": [
      {
        "id": "minecraft:cobblestone",
        "count": 7
      },
      {
        "id": "minecraft:bow",
        "count": 1
      },
      {
        "id": "minecraft:redstone",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dried_kelp",
    "input": {
      "item": "minecraft:dried_kelp",
      "count": 9
    },
    "output_display": [
      "minecraft:dried_kelp_block",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:dried_kelp_block",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dried_kelp_block",
    "input": {
      "item": "minecraft:dried_kelp_block",
      "count": 1
    },
    "output_display": [
      "minecraft:dried_kelp",
      "minecraft:dried_kelp",
      "minecraft:dried_kelp",
      "minecraft:dried_kelp",
      "minecraft:dried_kelp",
      "minecraft:dried_kelp",
      "minecraft:dried_kelp",
      "minecraft:dried_kelp",
      "minecraft:dried_kelp"
    ],
    "output": [
      {
        "id": "minecraft:dried_kelp",
        "count": 9
      }
    ]
  },
  {
    "crafting_recipe_name": "dripstone_block",
    "input": {
      "item": "minecraft:dripstone_block",
      "count": 1
    },
    "output_display": [
      "minecraft:pointed_dripstone",
      "minecraft:pointed_dripstone",
      None,
      "minecraft:pointed_dripstone",
      "minecraft:pointed_dripstone",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:pointed_dripstone",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "dropper",
    "input": {
      "item": "minecraft:dropper",
      "count": 1
    },
    "output_display": [
      "minecraft:cobblestone",
      "minecraft:cobblestone",
      "minecraft:cobblestone",
      "minecraft:cobblestone",
      None,
      "minecraft:cobblestone",
      "minecraft:cobblestone",
      "minecraft:redstone",
      "minecraft:cobblestone"
    ],
    "output": [
      {
        "id": "minecraft:cobblestone",
        "count": 7
      },
      {
        "id": "minecraft:redstone",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dune_armor_trim_smithing_template",
    "input": {
      "item": "minecraft:dune_armor_trim_smithing_template",
      "count": 2
    },
    "output_display": [
      "minecraft:diamond",
      "minecraft:dune_armor_trim_smithing_template",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:sandstone",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:diamond"
    ],
    "output": [
      {
        "id": "minecraft:diamond",
        "count": 7
      },
      {
        "id": "minecraft:dune_armor_trim_smithing_template",
        "count": 1
      },
      {
        "id": "minecraft:sandstone",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dye_black_bed",
    "input": {
      "item": "minecraft:black_bed",
      "count": 1
    },
    "output_display": [
      "minecraft:black_dye",
      "minecraft:blue_bed",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:black_dye",
        "count": 1
      },
      {
        "id": "minecraft:blue_bed",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dye_black_carpet",
    "input": {
      "item": "minecraft:black_carpet",
      "count": 1
    },
    "output_display": [
      "minecraft:black_dye",
      "minecraft:blue_carpet",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:black_dye",
        "count": 1
      },
      {
        "id": "minecraft:blue_carpet",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dye_black_wool",
    "input": {
      "item": "minecraft:black_wool",
      "count": 1
    },
    "output_display": [
      "minecraft:black_dye",
      "minecraft:blue_wool",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:black_dye",
        "count": 1
      },
      {
        "id": "minecraft:blue_wool",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dye_blue_bed",
    "input": {
      "item": "minecraft:blue_bed",
      "count": 1
    },
    "output_display": [
      "minecraft:blue_dye",
      "minecraft:white_bed",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:blue_dye",
        "count": 1
      },
      {
        "id": "minecraft:white_bed",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dye_blue_carpet",
    "input": {
      "item": "minecraft:blue_carpet",
      "count": 1
    },
    "output_display": [
      "minecraft:blue_dye",
      "minecraft:white_carpet",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:blue_dye",
        "count": 1
      },
      {
        "id": "minecraft:white_carpet",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dye_blue_wool",
    "input": {
      "item": "minecraft:blue_wool",
      "count": 1
    },
    "output_display": [
      "minecraft:blue_dye",
      "minecraft:white_wool",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:blue_dye",
        "count": 1
      },
      {
        "id": "minecraft:white_wool",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dye_brown_bed",
    "input": {
      "item": "minecraft:brown_bed",
      "count": 1
    },
    "output_display": [
      "minecraft:brown_dye",
      "minecraft:white_bed",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:brown_dye",
        "count": 1
      },
      {
        "id": "minecraft:white_bed",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dye_brown_carpet",
    "input": {
      "item": "minecraft:brown_carpet",
      "count": 1
    },
    "output_display": [
      "minecraft:brown_dye",
      "minecraft:white_carpet",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:brown_dye",
        "count": 1
      },
      {
        "id": "minecraft:white_carpet",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dye_brown_wool",
    "input": {
      "item": "minecraft:brown_wool",
      "count": 1
    },
    "output_display": [
      "minecraft:brown_dye",
      "minecraft:white_wool",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:brown_dye",
        "count": 1
      },
      {
        "id": "minecraft:white_wool",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dye_cyan_bed",
    "input": {
      "item": "minecraft:cyan_bed",
      "count": 1
    },
    "output_display": [
      "minecraft:cyan_dye",
      "minecraft:white_bed",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:cyan_dye",
        "count": 1
      },
      {
        "id": "minecraft:white_bed",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dye_cyan_carpet",
    "input": {
      "item": "minecraft:cyan_carpet",
      "count": 1
    },
    "output_display": [
      "minecraft:cyan_dye",
      "minecraft:white_carpet",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:cyan_dye",
        "count": 1
      },
      {
        "id": "minecraft:white_carpet",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dye_cyan_wool",
    "input": {
      "item": "minecraft:cyan_wool",
      "count": 1
    },
    "output_display": [
      "minecraft:cyan_dye",
      "minecraft:white_wool",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:cyan_dye",
        "count": 1
      },
      {
        "id": "minecraft:white_wool",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dye_gray_bed",
    "input": {
      "item": "minecraft:gray_bed",
      "count": 1
    },
    "output_display": [
      "minecraft:gray_dye",
      "minecraft:white_bed",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:gray_dye",
        "count": 1
      },
      {
        "id": "minecraft:white_bed",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dye_gray_carpet",
    "input": {
      "item": "minecraft:gray_carpet",
      "count": 1
    },
    "output_display": [
      "minecraft:gray_dye",
      "minecraft:white_carpet",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:gray_dye",
        "count": 1
      },
      {
        "id": "minecraft:white_carpet",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dye_gray_wool",
    "input": {
      "item": "minecraft:gray_wool",
      "count": 1
    },
    "output_display": [
      "minecraft:gray_dye",
      "minecraft:white_wool",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:gray_dye",
        "count": 1
      },
      {
        "id": "minecraft:white_wool",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dye_green_bed",
    "input": {
      "item": "minecraft:green_bed",
      "count": 1
    },
    "output_display": [
      "minecraft:green_dye",
      "minecraft:white_bed",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:green_dye",
        "count": 1
      },
      {
        "id": "minecraft:white_bed",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dye_green_carpet",
    "input": {
      "item": "minecraft:green_carpet",
      "count": 1
    },
    "output_display": [
      "minecraft:green_dye",
      "minecraft:white_carpet",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:green_dye",
        "count": 1
      },
      {
        "id": "minecraft:white_carpet",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dye_green_wool",
    "input": {
      "item": "minecraft:green_wool",
      "count": 1
    },
    "output_display": [
      "minecraft:green_dye",
      "minecraft:white_wool",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:green_dye",
        "count": 1
      },
      {
        "id": "minecraft:white_wool",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dye_light_blue_bed",
    "input": {
      "item": "minecraft:light_blue_bed",
      "count": 1
    },
    "output_display": [
      "minecraft:light_blue_dye",
      "minecraft:white_bed",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:light_blue_dye",
        "count": 1
      },
      {
        "id": "minecraft:white_bed",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dye_light_blue_carpet",
    "input": {
      "item": "minecraft:light_blue_carpet",
      "count": 1
    },
    "output_display": [
      "minecraft:light_blue_dye",
      "minecraft:white_carpet",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:light_blue_dye",
        "count": 1
      },
      {
        "id": "minecraft:white_carpet",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dye_light_blue_wool",
    "input": {
      "item": "minecraft:light_blue_wool",
      "count": 1
    },
    "output_display": [
      "minecraft:light_blue_dye",
      "minecraft:white_wool",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:light_blue_dye",
        "count": 1
      },
      {
        "id": "minecraft:white_wool",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dye_light_gray_bed",
    "input": {
      "item": "minecraft:light_gray_bed",
      "count": 1
    },
    "output_display": [
      "minecraft:light_gray_dye",
      "minecraft:white_bed",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:light_gray_dye",
        "count": 1
      },
      {
        "id": "minecraft:white_bed",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dye_light_gray_carpet",
    "input": {
      "item": "minecraft:light_gray_carpet",
      "count": 1
    },
    "output_display": [
      "minecraft:light_gray_dye",
      "minecraft:white_carpet",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:light_gray_dye",
        "count": 1
      },
      {
        "id": "minecraft:white_carpet",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dye_light_gray_wool",
    "input": {
      "item": "minecraft:light_gray_wool",
      "count": 1
    },
    "output_display": [
      "minecraft:light_gray_dye",
      "minecraft:white_wool",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:light_gray_dye",
        "count": 1
      },
      {
        "id": "minecraft:white_wool",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dye_lime_bed",
    "input": {
      "item": "minecraft:lime_bed",
      "count": 1
    },
    "output_display": [
      "minecraft:lime_dye",
      "minecraft:white_bed",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:lime_dye",
        "count": 1
      },
      {
        "id": "minecraft:white_bed",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dye_lime_carpet",
    "input": {
      "item": "minecraft:lime_carpet",
      "count": 1
    },
    "output_display": [
      "minecraft:lime_dye",
      "minecraft:white_carpet",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:lime_dye",
        "count": 1
      },
      {
        "id": "minecraft:white_carpet",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dye_lime_wool",
    "input": {
      "item": "minecraft:lime_wool",
      "count": 1
    },
    "output_display": [
      "minecraft:lime_dye",
      "minecraft:white_wool",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:lime_dye",
        "count": 1
      },
      {
        "id": "minecraft:white_wool",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dye_magenta_bed",
    "input": {
      "item": "minecraft:magenta_bed",
      "count": 1
    },
    "output_display": [
      "minecraft:magenta_dye",
      "minecraft:white_bed",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:magenta_dye",
        "count": 1
      },
      {
        "id": "minecraft:white_bed",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dye_magenta_carpet",
    "input": {
      "item": "minecraft:magenta_carpet",
      "count": 1
    },
    "output_display": [
      "minecraft:magenta_dye",
      "minecraft:white_carpet",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:magenta_dye",
        "count": 1
      },
      {
        "id": "minecraft:white_carpet",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dye_magenta_wool",
    "input": {
      "item": "minecraft:magenta_wool",
      "count": 1
    },
    "output_display": [
      "minecraft:magenta_dye",
      "minecraft:white_wool",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:magenta_dye",
        "count": 1
      },
      {
        "id": "minecraft:white_wool",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dye_orange_bed",
    "input": {
      "item": "minecraft:orange_bed",
      "count": 1
    },
    "output_display": [
      "minecraft:orange_dye",
      "minecraft:white_bed",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:orange_dye",
        "count": 1
      },
      {
        "id": "minecraft:white_bed",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dye_orange_carpet",
    "input": {
      "item": "minecraft:orange_carpet",
      "count": 1
    },
    "output_display": [
      "minecraft:orange_dye",
      "minecraft:white_carpet",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:orange_dye",
        "count": 1
      },
      {
        "id": "minecraft:white_carpet",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dye_orange_wool",
    "input": {
      "item": "minecraft:orange_wool",
      "count": 1
    },
    "output_display": [
      "minecraft:orange_dye",
      "minecraft:white_wool",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:orange_dye",
        "count": 1
      },
      {
        "id": "minecraft:white_wool",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dye_pink_bed",
    "input": {
      "item": "minecraft:pink_bed",
      "count": 1
    },
    "output_display": [
      "minecraft:pink_dye",
      "minecraft:white_bed",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:pink_dye",
        "count": 1
      },
      {
        "id": "minecraft:white_bed",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dye_pink_carpet",
    "input": {
      "item": "minecraft:pink_carpet",
      "count": 1
    },
    "output_display": [
      "minecraft:pink_dye",
      "minecraft:white_carpet",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:pink_dye",
        "count": 1
      },
      {
        "id": "minecraft:white_carpet",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dye_pink_wool",
    "input": {
      "item": "minecraft:pink_wool",
      "count": 1
    },
    "output_display": [
      "minecraft:pink_dye",
      "minecraft:white_wool",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:pink_dye",
        "count": 1
      },
      {
        "id": "minecraft:white_wool",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dye_purple_bed",
    "input": {
      "item": "minecraft:purple_bed",
      "count": 1
    },
    "output_display": [
      "minecraft:purple_dye",
      "minecraft:white_bed",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:purple_dye",
        "count": 1
      },
      {
        "id": "minecraft:white_bed",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dye_purple_carpet",
    "input": {
      "item": "minecraft:purple_carpet",
      "count": 1
    },
    "output_display": [
      "minecraft:purple_dye",
      "minecraft:white_carpet",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:purple_dye",
        "count": 1
      },
      {
        "id": "minecraft:white_carpet",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dye_purple_wool",
    "input": {
      "item": "minecraft:purple_wool",
      "count": 1
    },
    "output_display": [
      "minecraft:purple_dye",
      "minecraft:white_wool",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:purple_dye",
        "count": 1
      },
      {
        "id": "minecraft:white_wool",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dye_red_bed",
    "input": {
      "item": "minecraft:red_bed",
      "count": 1
    },
    "output_display": [
      "minecraft:red_dye",
      "minecraft:white_bed",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:red_dye",
        "count": 1
      },
      {
        "id": "minecraft:white_bed",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dye_red_carpet",
    "input": {
      "item": "minecraft:red_carpet",
      "count": 1
    },
    "output_display": [
      "minecraft:red_dye",
      "minecraft:white_carpet",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:red_dye",
        "count": 1
      },
      {
        "id": "minecraft:white_carpet",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dye_red_wool",
    "input": {
      "item": "minecraft:red_wool",
      "count": 1
    },
    "output_display": [
      "minecraft:red_dye",
      "minecraft:white_wool",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:red_dye",
        "count": 1
      },
      {
        "id": "minecraft:white_wool",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dye_white_bed",
    "input": {
      "item": "minecraft:white_bed",
      "count": 1
    },
    "output_display": [
      "minecraft:white_dye",
      "minecraft:white_bed",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:white_dye",
        "count": 1
      },
      {
        "id": "minecraft:white_bed",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dye_white_carpet",
    "input": {
      "item": "minecraft:white_carpet",
      "count": 1
    },
    "output_display": [
      "minecraft:white_dye",
      "minecraft:white_carpet",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:white_dye",
        "count": 1
      },
      {
        "id": "minecraft:white_carpet",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dye_white_wool",
    "input": {
      "item": "minecraft:white_wool",
      "count": 1
    },
    "output_display": [
      "minecraft:white_dye",
      "minecraft:white_wool",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:white_dye",
        "count": 1
      },
      {
        "id": "minecraft:white_wool",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dye_yellow_bed",
    "input": {
      "item": "minecraft:yellow_bed",
      "count": 1
    },
    "output_display": [
      "minecraft:yellow_dye",
      "minecraft:white_bed",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:yellow_dye",
        "count": 1
      },
      {
        "id": "minecraft:white_bed",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dye_yellow_carpet",
    "input": {
      "item": "minecraft:yellow_carpet",
      "count": 1
    },
    "output_display": [
      "minecraft:yellow_dye",
      "minecraft:white_carpet",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:yellow_dye",
        "count": 1
      },
      {
        "id": "minecraft:white_carpet",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "dye_yellow_wool",
    "input": {
      "item": "minecraft:yellow_wool",
      "count": 1
    },
    "output_display": [
      "minecraft:yellow_dye",
      "minecraft:white_wool",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:yellow_dye",
        "count": 1
      },
      {
        "id": "minecraft:white_wool",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "emerald",
    "input": {
      "item": "minecraft:emerald",
      "count": 9
    },
    "output_display": [
      "minecraft:emerald_block",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:emerald_block",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "emerald_block",
    "input": {
      "item": "minecraft:emerald_block",
      "count": 1
    },
    "output_display": [
      "minecraft:emerald",
      "minecraft:emerald",
      "minecraft:emerald",
      "minecraft:emerald",
      "minecraft:emerald",
      "minecraft:emerald",
      "minecraft:emerald",
      "minecraft:emerald",
      "minecraft:emerald"
    ],
    "output": [
      {
        "id": "minecraft:emerald",
        "count": 9
      }
    ]
  },
  {
    "crafting_recipe_name": "enchanting_table",
    "input": {
      "item": "minecraft:enchanting_table",
      "count": 1
    },
    "output_display": [
      None,
      "minecraft:book",
      None,
      "minecraft:diamond",
      "minecraft:obsidian",
      "minecraft:diamond",
      "minecraft:obsidian",
      "minecraft:obsidian",
      "minecraft:obsidian"
    ],
    "output": [
      {
        "id": "minecraft:book",
        "count": 1
      },
      {
        "id": "minecraft:diamond",
        "count": 2
      },
      {
        "id": "minecraft:obsidian",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "ender_chest",
    "input": {
      "item": "minecraft:ender_chest",
      "count": 1
    },
    "output_display": [
      "minecraft:obsidian",
      "minecraft:obsidian",
      "minecraft:obsidian",
      "minecraft:obsidian",
      "minecraft:ender_eye",
      "minecraft:obsidian",
      "minecraft:obsidian",
      "minecraft:obsidian",
      "minecraft:obsidian"
    ],
    "output": [
      {
        "id": "minecraft:obsidian",
        "count": 8
      },
      {
        "id": "minecraft:ender_eye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "ender_eye",
    "input": {
      "item": "minecraft:ender_eye",
      "count": 1
    },
    "output_display": [
      "minecraft:ender_pearl",
      "minecraft:blaze_powder",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:ender_pearl",
        "count": 1
      },
      {
        "id": "minecraft:blaze_powder",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "end_crystal",
    "input": {
      "item": "minecraft:end_crystal",
      "count": 1
    },
    "output_display": [
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:ender_eye",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:ghast_tear",
      "minecraft:glass"
    ],
    "output": [
      {
        "id": "minecraft:glass",
        "count": 7
      },
      {
        "id": "minecraft:ender_eye",
        "count": 1
      },
      {
        "id": "minecraft:ghast_tear",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "end_rod",
    "input": {
      "item": "minecraft:end_rod",
      "count": 4
    },
    "output_display": [
      "minecraft:blaze_rod",
      None,
      None,
      "minecraft:popped_chorus_fruit",
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:blaze_rod",
        "count": 1
      },
      {
        "id": "minecraft:popped_chorus_fruit",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "end_stone_bricks",
    "input": {
      "item": "minecraft:end_stone_bricks",
      "count": 4
    },
    "output_display": [
      "minecraft:end_stone",
      "minecraft:end_stone",
      None,
      "minecraft:end_stone",
      "minecraft:end_stone",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:end_stone",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "end_stone_brick_slab",
    "input": {
      "item": "minecraft:end_stone_brick_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:end_stone_bricks",
      "minecraft:end_stone_bricks",
      "minecraft:end_stone_bricks",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:end_stone_bricks",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "end_stone_brick_stairs",
    "input": {
      "item": "minecraft:end_stone_brick_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:end_stone_bricks",
      None,
      None,
      "minecraft:end_stone_bricks",
      "minecraft:end_stone_bricks",
      None,
      "minecraft:end_stone_bricks",
      "minecraft:end_stone_bricks",
      "minecraft:end_stone_bricks"
    ],
    "output": [
      {
        "id": "minecraft:end_stone_bricks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "end_stone_brick_wall",
    "input": {
      "item": "minecraft:end_stone_brick_wall",
      "count": 6
    },
    "output_display": [
      "minecraft:end_stone_bricks",
      "minecraft:end_stone_bricks",
      "minecraft:end_stone_bricks",
      "minecraft:end_stone_bricks",
      "minecraft:end_stone_bricks",
      "minecraft:end_stone_bricks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:end_stone_bricks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "exposed_chiseled_copper",
    "input": {
      "item": "minecraft:exposed_chiseled_copper",
      "count": 1
    },
    "output_display": [
      "minecraft:exposed_cut_copper_slab",
      None,
      None,
      "minecraft:exposed_cut_copper_slab",
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:exposed_cut_copper_slab",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "exposed_copper_bulb",
    "input": {
      "item": "minecraft:exposed_copper_bulb",
      "count": 4
    },
    "output_display": [
      None,
      "minecraft:exposed_copper",
      None,
      "minecraft:exposed_copper",
      "minecraft:blaze_rod",
      "minecraft:exposed_copper",
      None,
      "minecraft:redstone",
      None
    ],
    "output": [
      {
        "id": "minecraft:exposed_copper",
        "count": 3
      },
      {
        "id": "minecraft:blaze_rod",
        "count": 1
      },
      {
        "id": "minecraft:redstone",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "exposed_copper_grate",
    "input": {
      "item": "minecraft:exposed_copper_grate",
      "count": 4
    },
    "output_display": [
      None,
      "minecraft:exposed_copper",
      None,
      "minecraft:exposed_copper",
      None,
      "minecraft:exposed_copper",
      None,
      "minecraft:exposed_copper",
      None
    ],
    "output": [
      {
        "id": "minecraft:exposed_copper",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "exposed_cut_copper",
    "input": {
      "item": "minecraft:exposed_cut_copper",
      "count": 4
    },
    "output_display": [
      "minecraft:exposed_copper",
      "minecraft:exposed_copper",
      None,
      "minecraft:exposed_copper",
      "minecraft:exposed_copper",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:exposed_copper",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "exposed_cut_copper_slab",
    "input": {
      "item": "minecraft:exposed_cut_copper_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:exposed_cut_copper",
      "minecraft:exposed_cut_copper",
      "minecraft:exposed_cut_copper",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:exposed_cut_copper",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "exposed_cut_copper_stairs",
    "input": {
      "item": "minecraft:exposed_cut_copper_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:exposed_cut_copper",
      None,
      None,
      "minecraft:exposed_cut_copper",
      "minecraft:exposed_cut_copper",
      None,
      "minecraft:exposed_cut_copper",
      "minecraft:exposed_cut_copper",
      "minecraft:exposed_cut_copper"
    ],
    "output": [
      {
        "id": "minecraft:exposed_cut_copper",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "eye_armor_trim_smithing_template",
    "input": {
      "item": "minecraft:eye_armor_trim_smithing_template",
      "count": 2
    },
    "output_display": [
      "minecraft:diamond",
      "minecraft:eye_armor_trim_smithing_template",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:end_stone",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:diamond"
    ],
    "output": [
      {
        "id": "minecraft:diamond",
        "count": 7
      },
      {
        "id": "minecraft:eye_armor_trim_smithing_template",
        "count": 1
      },
      {
        "id": "minecraft:end_stone",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "fermented_spider_eye",
    "input": {
      "item": "minecraft:fermented_spider_eye",
      "count": 1
    },
    "output_display": [
      "minecraft:spider_eye",
      "minecraft:brown_mushroom",
      "minecraft:sugar",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:spider_eye",
        "count": 1
      },
      {
        "id": "minecraft:brown_mushroom",
        "count": 1
      },
      {
        "id": "minecraft:sugar",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "field_masoned_banner_pattern",
    "input": {
      "item": "minecraft:field_masoned_banner_pattern",
      "count": 1
    },
    "output_display": [
      "minecraft:paper",
      "minecraft:bricks",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:paper",
        "count": 1
      },
      {
        "id": "minecraft:bricks",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "firework_rocket_simple",
    "input": {
      "item": "minecraft:firework_rocket",
      "count": 3
    },
    "output_display": [
      "minecraft:gunpowder",
      "minecraft:paper",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:gunpowder",
        "count": 1
      },
      {
        "id": "minecraft:paper",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "fire_charge",
    "input": {
      "item": "minecraft:fire_charge",
      "count": 3
    },
    "output_display": [
      "minecraft:gunpowder",
      "minecraft:blaze_powder",
      "minecraft:coal",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:gunpowder",
        "count": 1
      },
      {
        "id": "minecraft:blaze_powder",
        "count": 1
      },
      {
        "id": "minecraft:coal",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "fishing_rod",
    "input": {
      "item": "minecraft:fishing_rod",
      "count": 1
    },
    "output_display": [
      None,
      None,
      "minecraft:stick",
      None,
      "minecraft:stick",
      "minecraft:string",
      "minecraft:stick",
      None,
      "minecraft:string"
    ],
    "output": [
      {
        "id": "minecraft:stick",
        "count": 3
      },
      {
        "id": "minecraft:string",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "fletching_table",
    "input": {
      "item": "minecraft:fletching_table",
      "count": 1
    },
    "output_display": [
      "minecraft:flint",
      "minecraft:flint",
      None,
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      None,
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      None
    ],
    "output": [
      {
        "id": "minecraft:flint",
        "count": 2
      },
      {
        "id": "minecraft:oak_planks",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "flint_and_steel",
    "input": {
      "item": "minecraft:flint_and_steel",
      "count": 1
    },
    "output_display": [
      "minecraft:iron_ingot",
      "minecraft:flint",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:iron_ingot",
        "count": 1
      },
      {
        "id": "minecraft:flint",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "flower_banner_pattern",
    "input": {
      "item": "minecraft:flower_banner_pattern",
      "count": 1
    },
    "output_display": [
      "minecraft:paper",
      "minecraft:oxeye_daisy",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:paper",
        "count": 1
      },
      {
        "id": "minecraft:oxeye_daisy",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "flower_pot",
    "input": {
      "item": "minecraft:flower_pot",
      "count": 1
    },
    "output_display": [
      "minecraft:brick",
      None,
      "minecraft:brick",
      None,
      "minecraft:brick",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:brick",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "flow_armor_trim_smithing_template",
    "input": {
      "item": "minecraft:flow_armor_trim_smithing_template",
      "count": 2
    },
    "output_display": [
      "minecraft:diamond",
      "minecraft:flow_armor_trim_smithing_template",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:breeze_rod",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:diamond"
    ],
    "output": [
      {
        "id": "minecraft:diamond",
        "count": 7
      },
      {
        "id": "minecraft:flow_armor_trim_smithing_template",
        "count": 1
      },
      {
        "id": "minecraft:breeze_rod",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "furnace",
    "input": {
      "item": "minecraft:furnace",
      "count": 1
    },
    "output_display": [
      "minecraft:cobblestone",
      "minecraft:cobblestone",
      "minecraft:cobblestone",
      "minecraft:cobblestone",
      None,
      "minecraft:cobblestone",
      "minecraft:cobblestone",
      "minecraft:cobblestone",
      "minecraft:cobblestone"
    ],
    "output": [
      {
        "id": "minecraft:cobblestone",
        "count": 8
      }
    ]
  },
  {
    "crafting_recipe_name": "furnace_minecart",
    "input": {
      "item": "minecraft:furnace_minecart",
      "count": 1
    },
    "output_display": [
      "minecraft:furnace",
      "minecraft:minecart",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:furnace",
        "count": 1
      },
      {
        "id": "minecraft:minecart",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "glass_bottle",
    "input": {
      "item": "minecraft:glass_bottle",
      "count": 3
    },
    "output_display": [
      "minecraft:glass",
      None,
      "minecraft:glass",
      None,
      "minecraft:glass",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:glass",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "glass_pane",
    "input": {
      "item": "minecraft:glass_pane",
      "count": 16
    },
    "output_display": [
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:glass",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "glistering_melon_slice",
    "input": {
      "item": "minecraft:glistering_melon_slice",
      "count": 1
    },
    "output_display": [
      "minecraft:gold_nugget",
      "minecraft:gold_nugget",
      "minecraft:gold_nugget",
      "minecraft:gold_nugget",
      "minecraft:melon_slice",
      "minecraft:gold_nugget",
      "minecraft:gold_nugget",
      "minecraft:gold_nugget",
      "minecraft:gold_nugget"
    ],
    "output": [
      {
        "id": "minecraft:gold_nugget",
        "count": 8
      },
      {
        "id": "minecraft:melon_slice",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "glowstone",
    "input": {
      "item": "minecraft:glowstone",
      "count": 1
    },
    "output_display": [
      "minecraft:glowstone_dust",
      "minecraft:glowstone_dust",
      None,
      "minecraft:glowstone_dust",
      "minecraft:glowstone_dust",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:glowstone_dust",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "glow_item_frame",
    "input": {
      "item": "minecraft:glow_item_frame",
      "count": 1
    },
    "output_display": [
      "minecraft:item_frame",
      "minecraft:glow_ink_sac",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:item_frame",
        "count": 1
      },
      {
        "id": "minecraft:glow_ink_sac",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "golden_apple",
    "input": {
      "item": "minecraft:golden_apple",
      "count": 1
    },
    "output_display": [
      "minecraft:gold_ingot",
      "minecraft:gold_ingot",
      "minecraft:gold_ingot",
      "minecraft:gold_ingot",
      "minecraft:apple",
      "minecraft:gold_ingot",
      "minecraft:gold_ingot",
      "minecraft:gold_ingot",
      "minecraft:gold_ingot"
    ],
    "output": [
      {
        "id": "minecraft:gold_ingot",
        "count": 8
      },
      {
        "id": "minecraft:apple",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "golden_axe",
    "input": {
      "item": "minecraft:golden_axe",
      "count": 1
    },
    "output_display": [
      "#minecraft:gold_tool_materials",
      "#minecraft:gold_tool_materials",
      None,
      "#minecraft:gold_tool_materials",
      "minecraft:stick",
      None,
      None,
      "minecraft:stick",
      None
    ],
    "output": [
      {
        "id": "#minecraft:gold_tool_materials",
        "count": 3
      },
      {
        "id": "minecraft:stick",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "golden_boots",
    "input": {
      "item": "minecraft:golden_boots",
      "count": 1
    },
    "output_display": [
      "minecraft:gold_ingot",
      None,
      "minecraft:gold_ingot",
      "minecraft:gold_ingot",
      None,
      "minecraft:gold_ingot",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:gold_ingot",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "golden_carrot",
    "input": {
      "item": "minecraft:golden_carrot",
      "count": 1
    },
    "output_display": [
      "minecraft:gold_nugget",
      "minecraft:gold_nugget",
      "minecraft:gold_nugget",
      "minecraft:gold_nugget",
      "minecraft:carrot",
      "minecraft:gold_nugget",
      "minecraft:gold_nugget",
      "minecraft:gold_nugget",
      "minecraft:gold_nugget"
    ],
    "output": [
      {
        "id": "minecraft:gold_nugget",
        "count": 8
      },
      {
        "id": "minecraft:carrot",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "golden_chestplate",
    "input": {
      "item": "minecraft:golden_chestplate",
      "count": 1
    },
    "output_display": [
      "minecraft:gold_ingot",
      None,
      "minecraft:gold_ingot",
      "minecraft:gold_ingot",
      "minecraft:gold_ingot",
      "minecraft:gold_ingot",
      "minecraft:gold_ingot",
      "minecraft:gold_ingot",
      "minecraft:gold_ingot"
    ],
    "output": [
      {
        "id": "minecraft:gold_ingot",
        "count": 8
      }
    ]
  },
  {
    "crafting_recipe_name": "golden_helmet",
    "input": {
      "item": "minecraft:golden_helmet",
      "count": 1
    },
    "output_display": [
      "minecraft:gold_ingot",
      "minecraft:gold_ingot",
      "minecraft:gold_ingot",
      "minecraft:gold_ingot",
      None,
      "minecraft:gold_ingot",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:gold_ingot",
        "count": 5
      }
    ]
  },
  {
    "crafting_recipe_name": "golden_hoe",
    "input": {
      "item": "minecraft:golden_hoe",
      "count": 1
    },
    "output_display": [
      "#minecraft:gold_tool_materials",
      "#minecraft:gold_tool_materials",
      None,
      None,
      "minecraft:stick",
      None,
      None,
      "minecraft:stick",
      None
    ],
    "output": [
      {
        "id": "#minecraft:gold_tool_materials",
        "count": 2
      },
      {
        "id": "minecraft:stick",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "golden_leggings",
    "input": {
      "item": "minecraft:golden_leggings",
      "count": 1
    },
    "output_display": [
      "minecraft:gold_ingot",
      "minecraft:gold_ingot",
      "minecraft:gold_ingot",
      "minecraft:gold_ingot",
      None,
      "minecraft:gold_ingot",
      "minecraft:gold_ingot",
      None,
      "minecraft:gold_ingot"
    ],
    "output": [
      {
        "id": "minecraft:gold_ingot",
        "count": 7
      }
    ]
  },
  {
    "crafting_recipe_name": "golden_pickaxe",
    "input": {
      "item": "minecraft:golden_pickaxe",
      "count": 1
    },
    "output_display": [
      "#minecraft:gold_tool_materials",
      "#minecraft:gold_tool_materials",
      "#minecraft:gold_tool_materials",
      None,
      "minecraft:stick",
      None,
      None,
      "minecraft:stick",
      None
    ],
    "output": [
      {
        "id": "#minecraft:gold_tool_materials",
        "count": 3
      },
      {
        "id": "minecraft:stick",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "golden_shovel",
    "input": {
      "item": "minecraft:golden_shovel",
      "count": 1
    },
    "output_display": [
      "#minecraft:gold_tool_materials",
      None,
      None,
      "minecraft:stick",
      None,
      None,
      "minecraft:stick",
      None,
      None
    ],
    "output": [
      {
        "id": "#minecraft:gold_tool_materials",
        "count": 1
      },
      {
        "id": "minecraft:stick",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "golden_sword",
    "input": {
      "item": "minecraft:golden_sword",
      "count": 1
    },
    "output_display": [
      "#minecraft:gold_tool_materials",
      None,
      None,
      "#minecraft:gold_tool_materials",
      None,
      None,
      "minecraft:stick",
      None,
      None
    ],
    "output": [
      {
        "id": "#minecraft:gold_tool_materials",
        "count": 2
      },
      {
        "id": "minecraft:stick",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "gold_block",
    "input": {
      "item": "minecraft:gold_block",
      "count": 1
    },
    "output_display": [
      "minecraft:gold_ingot",
      "minecraft:gold_ingot",
      "minecraft:gold_ingot",
      "minecraft:gold_ingot",
      "minecraft:gold_ingot",
      "minecraft:gold_ingot",
      "minecraft:gold_ingot",
      "minecraft:gold_ingot",
      "minecraft:gold_ingot"
    ],
    "output": [
      {
        "id": "minecraft:gold_ingot",
        "count": 9
      }
    ]
  },
  {
    "crafting_recipe_name": "gold_ingot_from_gold_block",
    "input": {
      "item": "minecraft:gold_ingot",
      "count": 9
    },
    "output_display": [
      "minecraft:gold_block",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:gold_block",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "gold_ingot_from_nuggets",
    "input": {
      "item": "minecraft:gold_ingot",
      "count": 1
    },
    "output_display": [
      "minecraft:gold_nugget",
      "minecraft:gold_nugget",
      "minecraft:gold_nugget",
      "minecraft:gold_nugget",
      "minecraft:gold_nugget",
      "minecraft:gold_nugget",
      "minecraft:gold_nugget",
      "minecraft:gold_nugget",
      "minecraft:gold_nugget"
    ],
    "output": [
      {
        "id": "minecraft:gold_nugget",
        "count": 9
      }
    ]
  },
  {
    "crafting_recipe_name": "gold_nugget",
    "input": {
      "item": "minecraft:gold_nugget",
      "count": 9
    },
    "output_display": [
      "minecraft:gold_ingot",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:gold_ingot",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "granite",
    "input": {
      "item": "minecraft:granite",
      "count": 1
    },
    "output_display": [
      "minecraft:diorite",
      "minecraft:quartz",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:diorite",
        "count": 1
      },
      {
        "id": "minecraft:quartz",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "granite_slab",
    "input": {
      "item": "minecraft:granite_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:granite",
      "minecraft:granite",
      "minecraft:granite",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:granite",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "granite_stairs",
    "input": {
      "item": "minecraft:granite_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:granite",
      None,
      None,
      "minecraft:granite",
      "minecraft:granite",
      None,
      "minecraft:granite",
      "minecraft:granite",
      "minecraft:granite"
    ],
    "output": [
      {
        "id": "minecraft:granite",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "granite_wall",
    "input": {
      "item": "minecraft:granite_wall",
      "count": 6
    },
    "output_display": [
      "minecraft:granite",
      "minecraft:granite",
      "minecraft:granite",
      "minecraft:granite",
      "minecraft:granite",
      "minecraft:granite",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:granite",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "gray_banner",
    "input": {
      "item": "minecraft:gray_banner",
      "count": 1
    },
    "output_display": [
      "minecraft:gray_wool",
      "minecraft:gray_wool",
      "minecraft:gray_wool",
      "minecraft:gray_wool",
      "minecraft:gray_wool",
      "minecraft:gray_wool",
      None,
      "minecraft:stick",
      None
    ],
    "output": [
      {
        "id": "minecraft:gray_wool",
        "count": 6
      },
      {
        "id": "minecraft:stick",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "gray_bed",
    "input": {
      "item": "minecraft:gray_bed",
      "count": 1
    },
    "output_display": [
      "minecraft:gray_wool",
      "minecraft:gray_wool",
      "minecraft:gray_wool",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:gray_wool",
        "count": 3
      },
      {
        "id": "minecraft:oak_planks",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "gray_candle",
    "input": {
      "item": "minecraft:gray_candle",
      "count": 1
    },
    "output_display": [
      "minecraft:candle",
      "minecraft:gray_dye",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:candle",
        "count": 1
      },
      {
        "id": "minecraft:gray_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "gray_carpet",
    "input": {
      "item": "minecraft:gray_carpet",
      "count": 3
    },
    "output_display": [
      "minecraft:gray_wool",
      "minecraft:gray_wool",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:gray_wool",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "gray_concrete_powder",
    "input": {
      "item": "minecraft:gray_concrete_powder",
      "count": 8
    },
    "output_display": [
      "minecraft:gray_dye",
      "minecraft:sand",
      "minecraft:sand",
      "minecraft:sand",
      "minecraft:sand",
      "minecraft:gravel",
      "minecraft:gravel",
      "minecraft:gravel",
      "minecraft:gravel"
    ],
    "output": [
      {
        "id": "minecraft:gray_dye",
        "count": 1
      },
      {
        "id": "minecraft:sand",
        "count": 4
      },
      {
        "id": "minecraft:gravel",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "gray_dye",
    "input": {
      "item": "minecraft:gray_dye",
      "count": 2
    },
    "output_display": [
      "minecraft:black_dye",
      "minecraft:white_dye",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:black_dye",
        "count": 1
      },
      {
        "id": "minecraft:white_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "gray_dye_from_closed_eyeblossom",
    "input": {
      "item": "minecraft:gray_dye",
      "count": 1
    },
    "output_display": [
      "minecraft:closed_eyeblossom",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:closed_eyeblossom",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "gray_stained_glass",
    "input": {
      "item": "minecraft:gray_stained_glass",
      "count": 8
    },
    "output_display": [
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:gray_dye",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass"
    ],
    "output": [
      {
        "id": "minecraft:glass",
        "count": 8
      },
      {
        "id": "minecraft:gray_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "gray_stained_glass_pane",
    "input": {
      "item": "minecraft:gray_stained_glass_pane",
      "count": 16
    },
    "output_display": [
      "minecraft:gray_stained_glass",
      "minecraft:gray_stained_glass",
      "minecraft:gray_stained_glass",
      "minecraft:gray_stained_glass",
      "minecraft:gray_stained_glass",
      "minecraft:gray_stained_glass",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:gray_stained_glass",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "gray_stained_glass_pane_from_glass_pane",
    "input": {
      "item": "minecraft:gray_stained_glass_pane",
      "count": 8
    },
    "output_display": [
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:gray_dye",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane"
    ],
    "output": [
      {
        "id": "minecraft:glass_pane",
        "count": 8
      },
      {
        "id": "minecraft:gray_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "gray_terracotta",
    "input": {
      "item": "minecraft:gray_terracotta",
      "count": 8
    },
    "output_display": [
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:gray_dye",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta"
    ],
    "output": [
      {
        "id": "minecraft:terracotta",
        "count": 8
      },
      {
        "id": "minecraft:gray_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "green_banner",
    "input": {
      "item": "minecraft:green_banner",
      "count": 1
    },
    "output_display": [
      "minecraft:green_wool",
      "minecraft:green_wool",
      "minecraft:green_wool",
      "minecraft:green_wool",
      "minecraft:green_wool",
      "minecraft:green_wool",
      None,
      "minecraft:stick",
      None
    ],
    "output": [
      {
        "id": "minecraft:green_wool",
        "count": 6
      },
      {
        "id": "minecraft:stick",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "green_bed",
    "input": {
      "item": "minecraft:green_bed",
      "count": 1
    },
    "output_display": [
      "minecraft:green_wool",
      "minecraft:green_wool",
      "minecraft:green_wool",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:green_wool",
        "count": 3
      },
      {
        "id": "minecraft:oak_planks",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "green_candle",
    "input": {
      "item": "minecraft:green_candle",
      "count": 1
    },
    "output_display": [
      "minecraft:candle",
      "minecraft:green_dye",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:candle",
        "count": 1
      },
      {
        "id": "minecraft:green_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "green_carpet",
    "input": {
      "item": "minecraft:green_carpet",
      "count": 3
    },
    "output_display": [
      "minecraft:green_wool",
      "minecraft:green_wool",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:green_wool",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "green_concrete_powder",
    "input": {
      "item": "minecraft:green_concrete_powder",
      "count": 8
    },
    "output_display": [
      "minecraft:green_dye",
      "minecraft:sand",
      "minecraft:sand",
      "minecraft:sand",
      "minecraft:sand",
      "minecraft:gravel",
      "minecraft:gravel",
      "minecraft:gravel",
      "minecraft:gravel"
    ],
    "output": [
      {
        "id": "minecraft:green_dye",
        "count": 1
      },
      {
        "id": "minecraft:sand",
        "count": 4
      },
      {
        "id": "minecraft:gravel",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "green_stained_glass",
    "input": {
      "item": "minecraft:green_stained_glass",
      "count": 8
    },
    "output_display": [
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:green_dye",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass"
    ],
    "output": [
      {
        "id": "minecraft:glass",
        "count": 8
      },
      {
        "id": "minecraft:green_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "green_stained_glass_pane",
    "input": {
      "item": "minecraft:green_stained_glass_pane",
      "count": 16
    },
    "output_display": [
      "minecraft:green_stained_glass",
      "minecraft:green_stained_glass",
      "minecraft:green_stained_glass",
      "minecraft:green_stained_glass",
      "minecraft:green_stained_glass",
      "minecraft:green_stained_glass",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:green_stained_glass",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "green_stained_glass_pane_from_glass_pane",
    "input": {
      "item": "minecraft:green_stained_glass_pane",
      "count": 8
    },
    "output_display": [
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:green_dye",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane"
    ],
    "output": [
      {
        "id": "minecraft:glass_pane",
        "count": 8
      },
      {
        "id": "minecraft:green_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "green_terracotta",
    "input": {
      "item": "minecraft:green_terracotta",
      "count": 8
    },
    "output_display": [
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:green_dye",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta"
    ],
    "output": [
      {
        "id": "minecraft:terracotta",
        "count": 8
      },
      {
        "id": "minecraft:green_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "grindstone",
    "input": {
      "item": "minecraft:grindstone",
      "count": 1
    },
    "output_display": [
      "minecraft:stick",
      "minecraft:stone_slab",
      "minecraft:stick",
      "minecraft:oak_planks",
      None,
      "minecraft:oak_planks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:stick",
        "count": 2
      },
      {
        "id": "minecraft:stone_slab",
        "count": 1
      },
      {
        "id": "minecraft:oak_planks",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "hay_block",
    "input": {
      "item": "minecraft:hay_block",
      "count": 1
    },
    "output_display": [
      "minecraft:wheat",
      "minecraft:wheat",
      "minecraft:wheat",
      "minecraft:wheat",
      "minecraft:wheat",
      "minecraft:wheat",
      "minecraft:wheat",
      "minecraft:wheat",
      "minecraft:wheat"
    ],
    "output": [
      {
        "id": "minecraft:wheat",
        "count": 9
      }
    ]
  },
  {
    "crafting_recipe_name": "heavy_weighted_pressure_plate",
    "input": {
      "item": "minecraft:heavy_weighted_pressure_plate",
      "count": 1
    },
    "output_display": [
      "minecraft:iron_ingot",
      "minecraft:iron_ingot",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:iron_ingot",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "honeycomb_block",
    "input": {
      "item": "minecraft:honeycomb_block",
      "count": 1
    },
    "output_display": [
      "minecraft:honeycomb",
      "minecraft:honeycomb",
      None,
      "minecraft:honeycomb",
      "minecraft:honeycomb",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:honeycomb",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "honey_block",
    "input": {
      "item": "minecraft:honey_block",
      "count": 1
    },
    "output_display": [
      "minecraft:honey_bottle",
      "minecraft:honey_bottle",
      None,
      "minecraft:honey_bottle",
      "minecraft:honey_bottle",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:honey_bottle",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "honey_bottle",
    "input": {
      "item": "minecraft:honey_bottle",
      "count": 4
    },
    "output_display": [
      "minecraft:honey_block",
      "minecraft:glass_bottle",
      "minecraft:glass_bottle",
      "minecraft:glass_bottle",
      "minecraft:glass_bottle",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:honey_block",
        "count": 1
      },
      {
        "id": "minecraft:glass_bottle",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "hopper",
    "input": {
      "item": "minecraft:hopper",
      "count": 1
    },
    "output_display": [
      "minecraft:iron_ingot",
      None,
      "minecraft:iron_ingot",
      "minecraft:iron_ingot",
      "minecraft:chest",
      "minecraft:iron_ingot",
      None,
      "minecraft:iron_ingot",
      None
    ],
    "output": [
      {
        "id": "minecraft:iron_ingot",
        "count": 5
      },
      {
        "id": "minecraft:chest",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "hopper_minecart",
    "input": {
      "item": "minecraft:hopper_minecart",
      "count": 1
    },
    "output_display": [
      "minecraft:hopper",
      "minecraft:minecart",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:hopper",
        "count": 1
      },
      {
        "id": "minecraft:minecart",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "host_armor_trim_smithing_template",
    "input": {
      "item": "minecraft:host_armor_trim_smithing_template",
      "count": 2
    },
    "output_display": [
      "minecraft:diamond",
      "minecraft:host_armor_trim_smithing_template",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:terracotta",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:diamond"
    ],
    "output": [
      {
        "id": "minecraft:diamond",
        "count": 7
      },
      {
        "id": "minecraft:host_armor_trim_smithing_template",
        "count": 1
      },
      {
        "id": "minecraft:terracotta",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "iron_axe",
    "input": {
      "item": "minecraft:iron_axe",
      "count": 1
    },
    "output_display": [
      "#minecraft:iron_tool_materials",
      "#minecraft:iron_tool_materials",
      None,
      "#minecraft:iron_tool_materials",
      "minecraft:stick",
      None,
      None,
      "minecraft:stick",
      None
    ],
    "output": [
      {
        "id": "#minecraft:iron_tool_materials",
        "count": 3
      },
      {
        "id": "minecraft:stick",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "iron_bars",
    "input": {
      "item": "minecraft:iron_bars",
      "count": 16
    },
    "output_display": [
      "minecraft:iron_ingot",
      "minecraft:iron_ingot",
      "minecraft:iron_ingot",
      "minecraft:iron_ingot",
      "minecraft:iron_ingot",
      "minecraft:iron_ingot",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:iron_ingot",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "iron_block",
    "input": {
      "item": "minecraft:iron_block",
      "count": 1
    },
    "output_display": [
      "minecraft:iron_ingot",
      "minecraft:iron_ingot",
      "minecraft:iron_ingot",
      "minecraft:iron_ingot",
      "minecraft:iron_ingot",
      "minecraft:iron_ingot",
      "minecraft:iron_ingot",
      "minecraft:iron_ingot",
      "minecraft:iron_ingot"
    ],
    "output": [
      {
        "id": "minecraft:iron_ingot",
        "count": 9
      }
    ]
  },
  {
    "crafting_recipe_name": "iron_boots",
    "input": {
      "item": "minecraft:iron_boots",
      "count": 1
    },
    "output_display": [
      "minecraft:iron_ingot",
      None,
      "minecraft:iron_ingot",
      "minecraft:iron_ingot",
      None,
      "minecraft:iron_ingot",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:iron_ingot",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "iron_chestplate",
    "input": {
      "item": "minecraft:iron_chestplate",
      "count": 1
    },
    "output_display": [
      "minecraft:iron_ingot",
      None,
      "minecraft:iron_ingot",
      "minecraft:iron_ingot",
      "minecraft:iron_ingot",
      "minecraft:iron_ingot",
      "minecraft:iron_ingot",
      "minecraft:iron_ingot",
      "minecraft:iron_ingot"
    ],
    "output": [
      {
        "id": "minecraft:iron_ingot",
        "count": 8
      }
    ]
  },
  {
    "crafting_recipe_name": "iron_door",
    "input": {
      "item": "minecraft:iron_door",
      "count": 3
    },
    "output_display": [
      "minecraft:iron_ingot",
      "minecraft:iron_ingot",
      None,
      "minecraft:iron_ingot",
      "minecraft:iron_ingot",
      None,
      "minecraft:iron_ingot",
      "minecraft:iron_ingot",
      None
    ],
    "output": [
      {
        "id": "minecraft:iron_ingot",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "iron_helmet",
    "input": {
      "item": "minecraft:iron_helmet",
      "count": 1
    },
    "output_display": [
      "minecraft:iron_ingot",
      "minecraft:iron_ingot",
      "minecraft:iron_ingot",
      "minecraft:iron_ingot",
      None,
      "minecraft:iron_ingot",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:iron_ingot",
        "count": 5
      }
    ]
  },
  {
    "crafting_recipe_name": "iron_hoe",
    "input": {
      "item": "minecraft:iron_hoe",
      "count": 1
    },
    "output_display": [
      "#minecraft:iron_tool_materials",
      "#minecraft:iron_tool_materials",
      None,
      None,
      "minecraft:stick",
      None,
      None,
      "minecraft:stick",
      None
    ],
    "output": [
      {
        "id": "#minecraft:iron_tool_materials",
        "count": 2
      },
      {
        "id": "minecraft:stick",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "iron_ingot_from_iron_block",
    "input": {
      "item": "minecraft:iron_ingot",
      "count": 9
    },
    "output_display": [
      "minecraft:iron_block",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:iron_block",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "iron_ingot_from_nuggets",
    "input": {
      "item": "minecraft:iron_ingot",
      "count": 1
    },
    "output_display": [
      "minecraft:iron_nugget",
      "minecraft:iron_nugget",
      "minecraft:iron_nugget",
      "minecraft:iron_nugget",
      "minecraft:iron_nugget",
      "minecraft:iron_nugget",
      "minecraft:iron_nugget",
      "minecraft:iron_nugget",
      "minecraft:iron_nugget"
    ],
    "output": [
      {
        "id": "minecraft:iron_nugget",
        "count": 9
      }
    ]
  },
  {
    "crafting_recipe_name": "iron_leggings",
    "input": {
      "item": "minecraft:iron_leggings",
      "count": 1
    },
    "output_display": [
      "minecraft:iron_ingot",
      "minecraft:iron_ingot",
      "minecraft:iron_ingot",
      "minecraft:iron_ingot",
      None,
      "minecraft:iron_ingot",
      "minecraft:iron_ingot",
      None,
      "minecraft:iron_ingot"
    ],
    "output": [
      {
        "id": "minecraft:iron_ingot",
        "count": 7
      }
    ]
  },
  {
    "crafting_recipe_name": "iron_nugget",
    "input": {
      "item": "minecraft:iron_nugget",
      "count": 9
    },
    "output_display": [
      "minecraft:iron_ingot",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:iron_ingot",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "iron_pickaxe",
    "input": {
      "item": "minecraft:iron_pickaxe",
      "count": 1
    },
    "output_display": [
      "#minecraft:iron_tool_materials",
      "#minecraft:iron_tool_materials",
      "#minecraft:iron_tool_materials",
      None,
      "minecraft:stick",
      None,
      None,
      "minecraft:stick",
      None
    ],
    "output": [
      {
        "id": "#minecraft:iron_tool_materials",
        "count": 3
      },
      {
        "id": "minecraft:stick",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "iron_shovel",
    "input": {
      "item": "minecraft:iron_shovel",
      "count": 1
    },
    "output_display": [
      "#minecraft:iron_tool_materials",
      None,
      None,
      "minecraft:stick",
      None,
      None,
      "minecraft:stick",
      None,
      None
    ],
    "output": [
      {
        "id": "#minecraft:iron_tool_materials",
        "count": 1
      },
      {
        "id": "minecraft:stick",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "iron_sword",
    "input": {
      "item": "minecraft:iron_sword",
      "count": 1
    },
    "output_display": [
      "#minecraft:iron_tool_materials",
      None,
      None,
      "#minecraft:iron_tool_materials",
      None,
      None,
      "minecraft:stick",
      None,
      None
    ],
    "output": [
      {
        "id": "#minecraft:iron_tool_materials",
        "count": 2
      },
      {
        "id": "minecraft:stick",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "iron_trapdoor",
    "input": {
      "item": "minecraft:iron_trapdoor",
      "count": 1
    },
    "output_display": [
      "minecraft:iron_ingot",
      "minecraft:iron_ingot",
      None,
      "minecraft:iron_ingot",
      "minecraft:iron_ingot",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:iron_ingot",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "item_frame",
    "input": {
      "item": "minecraft:item_frame",
      "count": 1
    },
    "output_display": [
      "minecraft:stick",
      "minecraft:stick",
      "minecraft:stick",
      "minecraft:stick",
      "minecraft:leather",
      "minecraft:stick",
      "minecraft:stick",
      "minecraft:stick",
      "minecraft:stick"
    ],
    "output": [
      {
        "id": "minecraft:stick",
        "count": 8
      },
      {
        "id": "minecraft:leather",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "jack_o_lantern",
    "input": {
      "item": "minecraft:jack_o_lantern",
      "count": 1
    },
    "output_display": [
      "minecraft:carved_pumpkin",
      None,
      None,
      "minecraft:torch",
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:carved_pumpkin",
        "count": 1
      },
      {
        "id": "minecraft:torch",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "jukebox",
    "input": {
      "item": "minecraft:jukebox",
      "count": 1
    },
    "output_display": [
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:diamond",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:oak_planks"
    ],
    "output": [
      {
        "id": "minecraft:oak_planks",
        "count": 8
      },
      {
        "id": "minecraft:diamond",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "jungle_boat",
    "input": {
      "item": "minecraft:jungle_boat",
      "count": 1
    },
    "output_display": [
      "minecraft:jungle_planks",
      None,
      "minecraft:jungle_planks",
      "minecraft:jungle_planks",
      "minecraft:jungle_planks",
      "minecraft:jungle_planks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:jungle_planks",
        "count": 5
      }
    ]
  },
  {
    "crafting_recipe_name": "jungle_button",
    "input": {
      "item": "minecraft:jungle_button",
      "count": 1
    },
    "output_display": [
      "minecraft:jungle_planks",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:jungle_planks",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "jungle_chest_boat",
    "input": {
      "item": "minecraft:jungle_chest_boat",
      "count": 1
    },
    "output_display": [
      "minecraft:chest",
      "minecraft:jungle_boat",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:chest",
        "count": 1
      },
      {
        "id": "minecraft:jungle_boat",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "jungle_door",
    "input": {
      "item": "minecraft:jungle_door",
      "count": 3
    },
    "output_display": [
      "minecraft:jungle_planks",
      "minecraft:jungle_planks",
      None,
      "minecraft:jungle_planks",
      "minecraft:jungle_planks",
      None,
      "minecraft:jungle_planks",
      "minecraft:jungle_planks",
      None
    ],
    "output": [
      {
        "id": "minecraft:jungle_planks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "jungle_fence",
    "input": {
      "item": "minecraft:jungle_fence",
      "count": 3
    },
    "output_display": [
      "minecraft:jungle_planks",
      "minecraft:stick",
      "minecraft:jungle_planks",
      "minecraft:jungle_planks",
      "minecraft:stick",
      "minecraft:jungle_planks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:jungle_planks",
        "count": 4
      },
      {
        "id": "minecraft:stick",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "jungle_fence_gate",
    "input": {
      "item": "minecraft:jungle_fence_gate",
      "count": 1
    },
    "output_display": [
      "minecraft:stick",
      "minecraft:jungle_planks",
      "minecraft:stick",
      "minecraft:stick",
      "minecraft:jungle_planks",
      "minecraft:stick",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:stick",
        "count": 4
      },
      {
        "id": "minecraft:jungle_planks",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "jungle_hanging_sign",
    "input": {
      "item": "minecraft:jungle_hanging_sign",
      "count": 6
    },
    "output_display": [
      "minecraft:chain",
      None,
      "minecraft:chain",
      "minecraft:stripped_jungle_log",
      "minecraft:stripped_jungle_log",
      "minecraft:stripped_jungle_log",
      "minecraft:stripped_jungle_log",
      "minecraft:stripped_jungle_log",
      "minecraft:stripped_jungle_log"
    ],
    "output": [
      {
        "id": "minecraft:chain",
        "count": 2
      },
      {
        "id": "minecraft:stripped_jungle_log",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "jungle_planks",
    "input": {
      "item": "minecraft:jungle_planks",
      "count": 4
    },
    "output_display": [
      "minecraft:jungle_log",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:jungle_log",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "jungle_pressure_plate",
    "input": {
      "item": "minecraft:jungle_pressure_plate",
      "count": 1
    },
    "output_display": [
      "minecraft:jungle_planks",
      "minecraft:jungle_planks",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:jungle_planks",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "jungle_sign",
    "input": {
      "item": "minecraft:jungle_sign",
      "count": 3
    },
    "output_display": [
      "minecraft:jungle_planks",
      "minecraft:jungle_planks",
      "minecraft:jungle_planks",
      "minecraft:jungle_planks",
      "minecraft:jungle_planks",
      "minecraft:jungle_planks",
      None,
      "minecraft:stick",
      None
    ],
    "output": [
      {
        "id": "minecraft:jungle_planks",
        "count": 6
      },
      {
        "id": "minecraft:stick",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "jungle_slab",
    "input": {
      "item": "minecraft:jungle_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:jungle_planks",
      "minecraft:jungle_planks",
      "minecraft:jungle_planks",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:jungle_planks",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "jungle_stairs",
    "input": {
      "item": "minecraft:jungle_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:jungle_planks",
      None,
      None,
      "minecraft:jungle_planks",
      "minecraft:jungle_planks",
      None,
      "minecraft:jungle_planks",
      "minecraft:jungle_planks",
      "minecraft:jungle_planks"
    ],
    "output": [
      {
        "id": "minecraft:jungle_planks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "jungle_trapdoor",
    "input": {
      "item": "minecraft:jungle_trapdoor",
      "count": 2
    },
    "output_display": [
      "minecraft:jungle_planks",
      "minecraft:jungle_planks",
      "minecraft:jungle_planks",
      "minecraft:jungle_planks",
      "minecraft:jungle_planks",
      "minecraft:jungle_planks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:jungle_planks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "jungle_wood",
    "input": {
      "item": "minecraft:jungle_wood",
      "count": 3
    },
    "output_display": [
      "minecraft:jungle_log",
      "minecraft:jungle_log",
      None,
      "minecraft:jungle_log",
      "minecraft:jungle_log",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:jungle_log",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "ladder",
    "input": {
      "item": "minecraft:ladder",
      "count": 3
    },
    "output_display": [
      "minecraft:stick",
      None,
      "minecraft:stick",
      "minecraft:stick",
      "minecraft:stick",
      "minecraft:stick",
      "minecraft:stick",
      None,
      "minecraft:stick"
    ],
    "output": [
      {
        "id": "minecraft:stick",
        "count": 7
      }
    ]
  },
  {
    "crafting_recipe_name": "lantern",
    "input": {
      "item": "minecraft:lantern",
      "count": 1
    },
    "output_display": [
      "minecraft:iron_nugget",
      "minecraft:iron_nugget",
      "minecraft:iron_nugget",
      "minecraft:iron_nugget",
      "minecraft:torch",
      "minecraft:iron_nugget",
      "minecraft:iron_nugget",
      "minecraft:iron_nugget",
      "minecraft:iron_nugget"
    ],
    "output": [
      {
        "id": "minecraft:iron_nugget",
        "count": 8
      },
      {
        "id": "minecraft:torch",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "lapis_block",
    "input": {
      "item": "minecraft:lapis_block",
      "count": 1
    },
    "output_display": [
      "minecraft:lapis_lazuli",
      "minecraft:lapis_lazuli",
      "minecraft:lapis_lazuli",
      "minecraft:lapis_lazuli",
      "minecraft:lapis_lazuli",
      "minecraft:lapis_lazuli",
      "minecraft:lapis_lazuli",
      "minecraft:lapis_lazuli",
      "minecraft:lapis_lazuli"
    ],
    "output": [
      {
        "id": "minecraft:lapis_lazuli",
        "count": 9
      }
    ]
  },
  {
    "crafting_recipe_name": "lapis_lazuli",
    "input": {
      "item": "minecraft:lapis_lazuli",
      "count": 9
    },
    "output_display": [
      "minecraft:lapis_block",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:lapis_block",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "lead",
    "input": {
      "item": "minecraft:lead",
      "count": 2
    },
    "output_display": [
      "minecraft:string",
      "minecraft:string",
      None,
      "minecraft:string",
      "minecraft:slime_ball",
      None,
      None,
      None,
      "minecraft:string"
    ],
    "output": [
      {
        "id": "minecraft:string",
        "count": 4
      },
      {
        "id": "minecraft:slime_ball",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "leather",
    "input": {
      "item": "minecraft:leather",
      "count": 1
    },
    "output_display": [
      "minecraft:rabbit_hide",
      "minecraft:rabbit_hide",
      None,
      "minecraft:rabbit_hide",
      "minecraft:rabbit_hide",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:rabbit_hide",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "leather_boots",
    "input": {
      "item": "minecraft:leather_boots",
      "count": 1
    },
    "output_display": [
      "minecraft:leather",
      None,
      "minecraft:leather",
      "minecraft:leather",
      None,
      "minecraft:leather",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:leather",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "leather_chestplate",
    "input": {
      "item": "minecraft:leather_chestplate",
      "count": 1
    },
    "output_display": [
      "minecraft:leather",
      None,
      "minecraft:leather",
      "minecraft:leather",
      "minecraft:leather",
      "minecraft:leather",
      "minecraft:leather",
      "minecraft:leather",
      "minecraft:leather"
    ],
    "output": [
      {
        "id": "minecraft:leather",
        "count": 8
      }
    ]
  },
  {
    "crafting_recipe_name": "leather_helmet",
    "input": {
      "item": "minecraft:leather_helmet",
      "count": 1
    },
    "output_display": [
      "minecraft:leather",
      "minecraft:leather",
      "minecraft:leather",
      "minecraft:leather",
      None,
      "minecraft:leather",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:leather",
        "count": 5
      }
    ]
  },
  {
    "crafting_recipe_name": "leather_horse_armor",
    "input": {
      "item": "minecraft:leather_horse_armor",
      "count": 1
    },
    "output_display": [
      "minecraft:leather",
      None,
      "minecraft:leather",
      "minecraft:leather",
      "minecraft:leather",
      "minecraft:leather",
      "minecraft:leather",
      None,
      "minecraft:leather"
    ],
    "output": [
      {
        "id": "minecraft:leather",
        "count": 7
      }
    ]
  },
  {
    "crafting_recipe_name": "leather_leggings",
    "input": {
      "item": "minecraft:leather_leggings",
      "count": 1
    },
    "output_display": [
      "minecraft:leather",
      "minecraft:leather",
      "minecraft:leather",
      "minecraft:leather",
      None,
      "minecraft:leather",
      "minecraft:leather",
      None,
      "minecraft:leather"
    ],
    "output": [
      {
        "id": "minecraft:leather",
        "count": 7
      }
    ]
  },
  {
    "crafting_recipe_name": "lectern",
    "input": {
      "item": "minecraft:lectern",
      "count": 1
    },
    "output_display": [
      "minecraft:oak_slab",
      "minecraft:oak_slab",
      "minecraft:oak_slab",
      None,
      "minecraft:bookshelf",
      None,
      None,
      "minecraft:oak_slab",
      None
    ],
    "output": [
      {
        "id": "minecraft:oak_slab",
        "count": 4
      },
      {
        "id": "minecraft:bookshelf",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "lever",
    "input": {
      "item": "minecraft:lever",
      "count": 1
    },
    "output_display": [
      "minecraft:stick",
      None,
      None,
      "minecraft:cobblestone",
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:stick",
        "count": 1
      },
      {
        "id": "minecraft:cobblestone",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "lightning_rod",
    "input": {
      "item": "minecraft:lightning_rod",
      "count": 1
    },
    "output_display": [
      "minecraft:copper_ingot",
      None,
      None,
      "minecraft:copper_ingot",
      None,
      None,
      "minecraft:copper_ingot",
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:copper_ingot",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "light_blue_banner",
    "input": {
      "item": "minecraft:light_blue_banner",
      "count": 1
    },
    "output_display": [
      "minecraft:light_blue_wool",
      "minecraft:light_blue_wool",
      "minecraft:light_blue_wool",
      "minecraft:light_blue_wool",
      "minecraft:light_blue_wool",
      "minecraft:light_blue_wool",
      None,
      "minecraft:stick",
      None
    ],
    "output": [
      {
        "id": "minecraft:light_blue_wool",
        "count": 6
      },
      {
        "id": "minecraft:stick",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "light_blue_bed",
    "input": {
      "item": "minecraft:light_blue_bed",
      "count": 1
    },
    "output_display": [
      "minecraft:light_blue_wool",
      "minecraft:light_blue_wool",
      "minecraft:light_blue_wool",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:light_blue_wool",
        "count": 3
      },
      {
        "id": "minecraft:oak_planks",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "light_blue_candle",
    "input": {
      "item": "minecraft:light_blue_candle",
      "count": 1
    },
    "output_display": [
      "minecraft:candle",
      "minecraft:light_blue_dye",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:candle",
        "count": 1
      },
      {
        "id": "minecraft:light_blue_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "light_blue_carpet",
    "input": {
      "item": "minecraft:light_blue_carpet",
      "count": 3
    },
    "output_display": [
      "minecraft:light_blue_wool",
      "minecraft:light_blue_wool",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:light_blue_wool",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "light_blue_concrete_powder",
    "input": {
      "item": "minecraft:light_blue_concrete_powder",
      "count": 8
    },
    "output_display": [
      "minecraft:light_blue_dye",
      "minecraft:sand",
      "minecraft:sand",
      "minecraft:sand",
      "minecraft:sand",
      "minecraft:gravel",
      "minecraft:gravel",
      "minecraft:gravel",
      "minecraft:gravel"
    ],
    "output": [
      {
        "id": "minecraft:light_blue_dye",
        "count": 1
      },
      {
        "id": "minecraft:sand",
        "count": 4
      },
      {
        "id": "minecraft:gravel",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "light_blue_dye_from_blue_orchid",
    "input": {
      "item": "minecraft:light_blue_dye",
      "count": 1
    },
    "output_display": [
      "minecraft:blue_orchid",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:blue_orchid",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "light_blue_dye_from_blue_white_dye",
    "input": {
      "item": "minecraft:light_blue_dye",
      "count": 2
    },
    "output_display": [
      "minecraft:blue_dye",
      "minecraft:white_dye",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:blue_dye",
        "count": 1
      },
      {
        "id": "minecraft:white_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "light_blue_stained_glass",
    "input": {
      "item": "minecraft:light_blue_stained_glass",
      "count": 8
    },
    "output_display": [
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:light_blue_dye",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass"
    ],
    "output": [
      {
        "id": "minecraft:glass",
        "count": 8
      },
      {
        "id": "minecraft:light_blue_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "light_blue_stained_glass_pane",
    "input": {
      "item": "minecraft:light_blue_stained_glass_pane",
      "count": 16
    },
    "output_display": [
      "minecraft:light_blue_stained_glass",
      "minecraft:light_blue_stained_glass",
      "minecraft:light_blue_stained_glass",
      "minecraft:light_blue_stained_glass",
      "minecraft:light_blue_stained_glass",
      "minecraft:light_blue_stained_glass",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:light_blue_stained_glass",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "light_blue_stained_glass_pane_from_glass_pane",
    "input": {
      "item": "minecraft:light_blue_stained_glass_pane",
      "count": 8
    },
    "output_display": [
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:light_blue_dye",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane"
    ],
    "output": [
      {
        "id": "minecraft:glass_pane",
        "count": 8
      },
      {
        "id": "minecraft:light_blue_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "light_blue_terracotta",
    "input": {
      "item": "minecraft:light_blue_terracotta",
      "count": 8
    },
    "output_display": [
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:light_blue_dye",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta"
    ],
    "output": [
      {
        "id": "minecraft:terracotta",
        "count": 8
      },
      {
        "id": "minecraft:light_blue_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "light_gray_banner",
    "input": {
      "item": "minecraft:light_gray_banner",
      "count": 1
    },
    "output_display": [
      "minecraft:light_gray_wool",
      "minecraft:light_gray_wool",
      "minecraft:light_gray_wool",
      "minecraft:light_gray_wool",
      "minecraft:light_gray_wool",
      "minecraft:light_gray_wool",
      None,
      "minecraft:stick",
      None
    ],
    "output": [
      {
        "id": "minecraft:light_gray_wool",
        "count": 6
      },
      {
        "id": "minecraft:stick",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "light_gray_bed",
    "input": {
      "item": "minecraft:light_gray_bed",
      "count": 1
    },
    "output_display": [
      "minecraft:light_gray_wool",
      "minecraft:light_gray_wool",
      "minecraft:light_gray_wool",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:light_gray_wool",
        "count": 3
      },
      {
        "id": "minecraft:oak_planks",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "light_gray_candle",
    "input": {
      "item": "minecraft:light_gray_candle",
      "count": 1
    },
    "output_display": [
      "minecraft:candle",
      "minecraft:light_gray_dye",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:candle",
        "count": 1
      },
      {
        "id": "minecraft:light_gray_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "light_gray_carpet",
    "input": {
      "item": "minecraft:light_gray_carpet",
      "count": 3
    },
    "output_display": [
      "minecraft:light_gray_wool",
      "minecraft:light_gray_wool",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:light_gray_wool",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "light_gray_concrete_powder",
    "input": {
      "item": "minecraft:light_gray_concrete_powder",
      "count": 8
    },
    "output_display": [
      "minecraft:light_gray_dye",
      "minecraft:sand",
      "minecraft:sand",
      "minecraft:sand",
      "minecraft:sand",
      "minecraft:gravel",
      "minecraft:gravel",
      "minecraft:gravel",
      "minecraft:gravel"
    ],
    "output": [
      {
        "id": "minecraft:light_gray_dye",
        "count": 1
      },
      {
        "id": "minecraft:sand",
        "count": 4
      },
      {
        "id": "minecraft:gravel",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "light_gray_dye_from_azure_bluet",
    "input": {
      "item": "minecraft:light_gray_dye",
      "count": 1
    },
    "output_display": [
      "minecraft:azure_bluet",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:azure_bluet",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "light_gray_dye_from_black_white_dye",
    "input": {
      "item": "minecraft:light_gray_dye",
      "count": 3
    },
    "output_display": [
      "minecraft:black_dye",
      "minecraft:white_dye",
      "minecraft:white_dye",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:black_dye",
        "count": 1
      },
      {
        "id": "minecraft:white_dye",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "light_gray_dye_from_gray_white_dye",
    "input": {
      "item": "minecraft:light_gray_dye",
      "count": 2
    },
    "output_display": [
      "minecraft:gray_dye",
      "minecraft:white_dye",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:gray_dye",
        "count": 1
      },
      {
        "id": "minecraft:white_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "light_gray_dye_from_oxeye_daisy",
    "input": {
      "item": "minecraft:light_gray_dye",
      "count": 1
    },
    "output_display": [
      "minecraft:oxeye_daisy",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:oxeye_daisy",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "light_gray_dye_from_white_tulip",
    "input": {
      "item": "minecraft:light_gray_dye",
      "count": 1
    },
    "output_display": [
      "minecraft:white_tulip",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:white_tulip",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "light_gray_stained_glass",
    "input": {
      "item": "minecraft:light_gray_stained_glass",
      "count": 8
    },
    "output_display": [
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:light_gray_dye",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass"
    ],
    "output": [
      {
        "id": "minecraft:glass",
        "count": 8
      },
      {
        "id": "minecraft:light_gray_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "light_gray_stained_glass_pane",
    "input": {
      "item": "minecraft:light_gray_stained_glass_pane",
      "count": 16
    },
    "output_display": [
      "minecraft:light_gray_stained_glass",
      "minecraft:light_gray_stained_glass",
      "minecraft:light_gray_stained_glass",
      "minecraft:light_gray_stained_glass",
      "minecraft:light_gray_stained_glass",
      "minecraft:light_gray_stained_glass",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:light_gray_stained_glass",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "light_gray_stained_glass_pane_from_glass_pane",
    "input": {
      "item": "minecraft:light_gray_stained_glass_pane",
      "count": 8
    },
    "output_display": [
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:light_gray_dye",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane"
    ],
    "output": [
      {
        "id": "minecraft:glass_pane",
        "count": 8
      },
      {
        "id": "minecraft:light_gray_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "light_gray_terracotta",
    "input": {
      "item": "minecraft:light_gray_terracotta",
      "count": 8
    },
    "output_display": [
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:light_gray_dye",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta"
    ],
    "output": [
      {
        "id": "minecraft:terracotta",
        "count": 8
      },
      {
        "id": "minecraft:light_gray_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "light_weighted_pressure_plate",
    "input": {
      "item": "minecraft:light_weighted_pressure_plate",
      "count": 1
    },
    "output_display": [
      "minecraft:gold_ingot",
      "minecraft:gold_ingot",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:gold_ingot",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "lime_banner",
    "input": {
      "item": "minecraft:lime_banner",
      "count": 1
    },
    "output_display": [
      "minecraft:lime_wool",
      "minecraft:lime_wool",
      "minecraft:lime_wool",
      "minecraft:lime_wool",
      "minecraft:lime_wool",
      "minecraft:lime_wool",
      None,
      "minecraft:stick",
      None
    ],
    "output": [
      {
        "id": "minecraft:lime_wool",
        "count": 6
      },
      {
        "id": "minecraft:stick",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "lime_bed",
    "input": {
      "item": "minecraft:lime_bed",
      "count": 1
    },
    "output_display": [
      "minecraft:lime_wool",
      "minecraft:lime_wool",
      "minecraft:lime_wool",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:lime_wool",
        "count": 3
      },
      {
        "id": "minecraft:oak_planks",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "lime_candle",
    "input": {
      "item": "minecraft:lime_candle",
      "count": 1
    },
    "output_display": [
      "minecraft:candle",
      "minecraft:lime_dye",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:candle",
        "count": 1
      },
      {
        "id": "minecraft:lime_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "lime_carpet",
    "input": {
      "item": "minecraft:lime_carpet",
      "count": 3
    },
    "output_display": [
      "minecraft:lime_wool",
      "minecraft:lime_wool",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:lime_wool",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "lime_concrete_powder",
    "input": {
      "item": "minecraft:lime_concrete_powder",
      "count": 8
    },
    "output_display": [
      "minecraft:lime_dye",
      "minecraft:sand",
      "minecraft:sand",
      "minecraft:sand",
      "minecraft:sand",
      "minecraft:gravel",
      "minecraft:gravel",
      "minecraft:gravel",
      "minecraft:gravel"
    ],
    "output": [
      {
        "id": "minecraft:lime_dye",
        "count": 1
      },
      {
        "id": "minecraft:sand",
        "count": 4
      },
      {
        "id": "minecraft:gravel",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "lime_dye",
    "input": {
      "item": "minecraft:lime_dye",
      "count": 2
    },
    "output_display": [
      "minecraft:green_dye",
      "minecraft:white_dye",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:green_dye",
        "count": 1
      },
      {
        "id": "minecraft:white_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "lime_stained_glass",
    "input": {
      "item": "minecraft:lime_stained_glass",
      "count": 8
    },
    "output_display": [
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:lime_dye",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass"
    ],
    "output": [
      {
        "id": "minecraft:glass",
        "count": 8
      },
      {
        "id": "minecraft:lime_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "lime_stained_glass_pane",
    "input": {
      "item": "minecraft:lime_stained_glass_pane",
      "count": 16
    },
    "output_display": [
      "minecraft:lime_stained_glass",
      "minecraft:lime_stained_glass",
      "minecraft:lime_stained_glass",
      "minecraft:lime_stained_glass",
      "minecraft:lime_stained_glass",
      "minecraft:lime_stained_glass",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:lime_stained_glass",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "lime_stained_glass_pane_from_glass_pane",
    "input": {
      "item": "minecraft:lime_stained_glass_pane",
      "count": 8
    },
    "output_display": [
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:lime_dye",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane"
    ],
    "output": [
      {
        "id": "minecraft:glass_pane",
        "count": 8
      },
      {
        "id": "minecraft:lime_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "lime_terracotta",
    "input": {
      "item": "minecraft:lime_terracotta",
      "count": 8
    },
    "output_display": [
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:lime_dye",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta"
    ],
    "output": [
      {
        "id": "minecraft:terracotta",
        "count": 8
      },
      {
        "id": "minecraft:lime_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "lodestone",
    "input": {
      "item": "minecraft:lodestone",
      "count": 1
    },
    "output_display": [
      "minecraft:chiseled_stone_bricks",
      "minecraft:chiseled_stone_bricks",
      "minecraft:chiseled_stone_bricks",
      "minecraft:chiseled_stone_bricks",
      "minecraft:iron_ingot",
      "minecraft:chiseled_stone_bricks",
      "minecraft:chiseled_stone_bricks",
      "minecraft:chiseled_stone_bricks",
      "minecraft:chiseled_stone_bricks"
    ],
    "output": [
      {
        "id": "minecraft:chiseled_stone_bricks",
        "count": 8
      },
      {
        "id": "minecraft:iron_ingot",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "loom",
    "input": {
      "item": "minecraft:loom",
      "count": 1
    },
    "output_display": [
      "minecraft:string",
      "minecraft:string",
      None,
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:string",
        "count": 2
      },
      {
        "id": "minecraft:oak_planks",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "mace",
    "input": {
      "item": "minecraft:mace",
      "count": 1
    },
    "output_display": [
      None,
      "minecraft:heavy_core",
      None,
      None,
      "minecraft:breeze_rod",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:heavy_core",
        "count": 1
      },
      {
        "id": "minecraft:breeze_rod",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "magenta_banner",
    "input": {
      "item": "minecraft:magenta_banner",
      "count": 1
    },
    "output_display": [
      "minecraft:magenta_wool",
      "minecraft:magenta_wool",
      "minecraft:magenta_wool",
      "minecraft:magenta_wool",
      "minecraft:magenta_wool",
      "minecraft:magenta_wool",
      None,
      "minecraft:stick",
      None
    ],
    "output": [
      {
        "id": "minecraft:magenta_wool",
        "count": 6
      },
      {
        "id": "minecraft:stick",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "magenta_bed",
    "input": {
      "item": "minecraft:magenta_bed",
      "count": 1
    },
    "output_display": [
      "minecraft:magenta_wool",
      "minecraft:magenta_wool",
      "minecraft:magenta_wool",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:magenta_wool",
        "count": 3
      },
      {
        "id": "minecraft:oak_planks",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "magenta_candle",
    "input": {
      "item": "minecraft:magenta_candle",
      "count": 1
    },
    "output_display": [
      "minecraft:candle",
      "minecraft:magenta_dye",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:candle",
        "count": 1
      },
      {
        "id": "minecraft:magenta_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "magenta_carpet",
    "input": {
      "item": "minecraft:magenta_carpet",
      "count": 3
    },
    "output_display": [
      "minecraft:magenta_wool",
      "minecraft:magenta_wool",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:magenta_wool",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "magenta_concrete_powder",
    "input": {
      "item": "minecraft:magenta_concrete_powder",
      "count": 8
    },
    "output_display": [
      "minecraft:magenta_dye",
      "minecraft:sand",
      "minecraft:sand",
      "minecraft:sand",
      "minecraft:sand",
      "minecraft:gravel",
      "minecraft:gravel",
      "minecraft:gravel",
      "minecraft:gravel"
    ],
    "output": [
      {
        "id": "minecraft:magenta_dye",
        "count": 1
      },
      {
        "id": "minecraft:sand",
        "count": 4
      },
      {
        "id": "minecraft:gravel",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "magenta_dye_from_allium",
    "input": {
      "item": "minecraft:magenta_dye",
      "count": 1
    },
    "output_display": [
      "minecraft:allium",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:allium",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "magenta_dye_from_blue_red_pink",
    "input": {
      "item": "minecraft:magenta_dye",
      "count": 3
    },
    "output_display": [
      "minecraft:blue_dye",
      "minecraft:red_dye",
      "minecraft:pink_dye",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:blue_dye",
        "count": 1
      },
      {
        "id": "minecraft:red_dye",
        "count": 1
      },
      {
        "id": "minecraft:pink_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "magenta_dye_from_blue_red_white_dye",
    "input": {
      "item": "minecraft:magenta_dye",
      "count": 4
    },
    "output_display": [
      "minecraft:blue_dye",
      "minecraft:red_dye",
      "minecraft:red_dye",
      "minecraft:white_dye",
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:blue_dye",
        "count": 1
      },
      {
        "id": "minecraft:red_dye",
        "count": 2
      },
      {
        "id": "minecraft:white_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "magenta_dye_from_lilac",
    "input": {
      "item": "minecraft:magenta_dye",
      "count": 2
    },
    "output_display": [
      "minecraft:lilac",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:lilac",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "magenta_dye_from_purple_and_pink",
    "input": {
      "item": "minecraft:magenta_dye",
      "count": 2
    },
    "output_display": [
      "minecraft:purple_dye",
      "minecraft:pink_dye",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:purple_dye",
        "count": 1
      },
      {
        "id": "minecraft:pink_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "magenta_stained_glass",
    "input": {
      "item": "minecraft:magenta_stained_glass",
      "count": 8
    },
    "output_display": [
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:magenta_dye",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass"
    ],
    "output": [
      {
        "id": "minecraft:glass",
        "count": 8
      },
      {
        "id": "minecraft:magenta_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "magenta_stained_glass_pane",
    "input": {
      "item": "minecraft:magenta_stained_glass_pane",
      "count": 16
    },
    "output_display": [
      "minecraft:magenta_stained_glass",
      "minecraft:magenta_stained_glass",
      "minecraft:magenta_stained_glass",
      "minecraft:magenta_stained_glass",
      "minecraft:magenta_stained_glass",
      "minecraft:magenta_stained_glass",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:magenta_stained_glass",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "magenta_stained_glass_pane_from_glass_pane",
    "input": {
      "item": "minecraft:magenta_stained_glass_pane",
      "count": 8
    },
    "output_display": [
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:magenta_dye",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane"
    ],
    "output": [
      {
        "id": "minecraft:glass_pane",
        "count": 8
      },
      {
        "id": "minecraft:magenta_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "magenta_terracotta",
    "input": {
      "item": "minecraft:magenta_terracotta",
      "count": 8
    },
    "output_display": [
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:magenta_dye",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta"
    ],
    "output": [
      {
        "id": "minecraft:terracotta",
        "count": 8
      },
      {
        "id": "minecraft:magenta_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "magma_block",
    "input": {
      "item": "minecraft:magma_block",
      "count": 1
    },
    "output_display": [
      "minecraft:magma_cream",
      "minecraft:magma_cream",
      None,
      "minecraft:magma_cream",
      "minecraft:magma_cream",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:magma_cream",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "magma_cream",
    "input": {
      "item": "minecraft:magma_cream",
      "count": 1
    },
    "output_display": [
      "minecraft:blaze_powder",
      "minecraft:slime_ball",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:blaze_powder",
        "count": 1
      },
      {
        "id": "minecraft:slime_ball",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "mangrove_boat",
    "input": {
      "item": "minecraft:mangrove_boat",
      "count": 1
    },
    "output_display": [
      "minecraft:mangrove_planks",
      None,
      "minecraft:mangrove_planks",
      "minecraft:mangrove_planks",
      "minecraft:mangrove_planks",
      "minecraft:mangrove_planks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:mangrove_planks",
        "count": 5
      }
    ]
  },
  {
    "crafting_recipe_name": "mangrove_button",
    "input": {
      "item": "minecraft:mangrove_button",
      "count": 1
    },
    "output_display": [
      "minecraft:mangrove_planks",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:mangrove_planks",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "mangrove_chest_boat",
    "input": {
      "item": "minecraft:mangrove_chest_boat",
      "count": 1
    },
    "output_display": [
      "minecraft:chest",
      "minecraft:mangrove_boat",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:chest",
        "count": 1
      },
      {
        "id": "minecraft:mangrove_boat",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "mangrove_door",
    "input": {
      "item": "minecraft:mangrove_door",
      "count": 3
    },
    "output_display": [
      "minecraft:mangrove_planks",
      "minecraft:mangrove_planks",
      None,
      "minecraft:mangrove_planks",
      "minecraft:mangrove_planks",
      None,
      "minecraft:mangrove_planks",
      "minecraft:mangrove_planks",
      None
    ],
    "output": [
      {
        "id": "minecraft:mangrove_planks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "mangrove_fence",
    "input": {
      "item": "minecraft:mangrove_fence",
      "count": 3
    },
    "output_display": [
      "minecraft:mangrove_planks",
      "minecraft:stick",
      "minecraft:mangrove_planks",
      "minecraft:mangrove_planks",
      "minecraft:stick",
      "minecraft:mangrove_planks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:mangrove_planks",
        "count": 4
      },
      {
        "id": "minecraft:stick",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "mangrove_fence_gate",
    "input": {
      "item": "minecraft:mangrove_fence_gate",
      "count": 1
    },
    "output_display": [
      "minecraft:stick",
      "minecraft:mangrove_planks",
      "minecraft:stick",
      "minecraft:stick",
      "minecraft:mangrove_planks",
      "minecraft:stick",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:stick",
        "count": 4
      },
      {
        "id": "minecraft:mangrove_planks",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "mangrove_hanging_sign",
    "input": {
      "item": "minecraft:mangrove_hanging_sign",
      "count": 6
    },
    "output_display": [
      "minecraft:chain",
      None,
      "minecraft:chain",
      "minecraft:stripped_mangrove_log",
      "minecraft:stripped_mangrove_log",
      "minecraft:stripped_mangrove_log",
      "minecraft:stripped_mangrove_log",
      "minecraft:stripped_mangrove_log",
      "minecraft:stripped_mangrove_log"
    ],
    "output": [
      {
        "id": "minecraft:chain",
        "count": 2
      },
      {
        "id": "minecraft:stripped_mangrove_log",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "mangrove_planks",
    "input": {
      "item": "minecraft:mangrove_planks",
      "count": 4
    },
    "output_display": [
      "minecraft:mangrove_log",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:mangrove_log",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "mangrove_pressure_plate",
    "input": {
      "item": "minecraft:mangrove_pressure_plate",
      "count": 1
    },
    "output_display": [
      "minecraft:mangrove_planks",
      "minecraft:mangrove_planks",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:mangrove_planks",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "mangrove_sign",
    "input": {
      "item": "minecraft:mangrove_sign",
      "count": 3
    },
    "output_display": [
      "minecraft:mangrove_planks",
      "minecraft:mangrove_planks",
      "minecraft:mangrove_planks",
      "minecraft:mangrove_planks",
      "minecraft:mangrove_planks",
      "minecraft:mangrove_planks",
      None,
      "minecraft:stick",
      None
    ],
    "output": [
      {
        "id": "minecraft:mangrove_planks",
        "count": 6
      },
      {
        "id": "minecraft:stick",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "mangrove_slab",
    "input": {
      "item": "minecraft:mangrove_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:mangrove_planks",
      "minecraft:mangrove_planks",
      "minecraft:mangrove_planks",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:mangrove_planks",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "mangrove_stairs",
    "input": {
      "item": "minecraft:mangrove_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:mangrove_planks",
      None,
      None,
      "minecraft:mangrove_planks",
      "minecraft:mangrove_planks",
      None,
      "minecraft:mangrove_planks",
      "minecraft:mangrove_planks",
      "minecraft:mangrove_planks"
    ],
    "output": [
      {
        "id": "minecraft:mangrove_planks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "mangrove_trapdoor",
    "input": {
      "item": "minecraft:mangrove_trapdoor",
      "count": 2
    },
    "output_display": [
      "minecraft:mangrove_planks",
      "minecraft:mangrove_planks",
      "minecraft:mangrove_planks",
      "minecraft:mangrove_planks",
      "minecraft:mangrove_planks",
      "minecraft:mangrove_planks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:mangrove_planks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "mangrove_wood",
    "input": {
      "item": "minecraft:mangrove_wood",
      "count": 3
    },
    "output_display": [
      "minecraft:mangrove_log",
      "minecraft:mangrove_log",
      None,
      "minecraft:mangrove_log",
      "minecraft:mangrove_log",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:mangrove_log",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "map",
    "input": {
      "item": "minecraft:map",
      "count": 1
    },
    "output_display": [
      "minecraft:paper",
      "minecraft:paper",
      "minecraft:paper",
      "minecraft:paper",
      "minecraft:compass",
      "minecraft:paper",
      "minecraft:paper",
      "minecraft:paper",
      "minecraft:paper"
    ],
    "output": [
      {
        "id": "minecraft:paper",
        "count": 8
      },
      {
        "id": "minecraft:compass",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "melon",
    "input": {
      "item": "minecraft:melon",
      "count": 1
    },
    "output_display": [
      "minecraft:melon_slice",
      "minecraft:melon_slice",
      "minecraft:melon_slice",
      "minecraft:melon_slice",
      "minecraft:melon_slice",
      "minecraft:melon_slice",
      "minecraft:melon_slice",
      "minecraft:melon_slice",
      "minecraft:melon_slice"
    ],
    "output": [
      {
        "id": "minecraft:melon_slice",
        "count": 9
      }
    ]
  },
  {
    "crafting_recipe_name": "melon_seeds",
    "input": {
      "item": "minecraft:melon_seeds",
      "count": 1
    },
    "output_display": [
      "minecraft:melon_slice",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:melon_slice",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "minecart",
    "input": {
      "item": "minecraft:minecart",
      "count": 1
    },
    "output_display": [
      "minecraft:iron_ingot",
      None,
      "minecraft:iron_ingot",
      "minecraft:iron_ingot",
      "minecraft:iron_ingot",
      "minecraft:iron_ingot",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:iron_ingot",
        "count": 5
      }
    ]
  },
  {
    "crafting_recipe_name": "mojang_banner_pattern",
    "input": {
      "item": "minecraft:mojang_banner_pattern",
      "count": 1
    },
    "output_display": [
      "minecraft:paper",
      "minecraft:enchanted_golden_apple",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:paper",
        "count": 1
      },
      {
        "id": "minecraft:enchanted_golden_apple",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "mossy_cobblestone_from_moss_block",
    "input": {
      "item": "minecraft:mossy_cobblestone",
      "count": 1
    },
    "output_display": [
      "minecraft:cobblestone",
      "minecraft:moss_block",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:cobblestone",
        "count": 1
      },
      {
        "id": "minecraft:moss_block",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "mossy_cobblestone_from_vine",
    "input": {
      "item": "minecraft:mossy_cobblestone",
      "count": 1
    },
    "output_display": [
      "minecraft:cobblestone",
      "minecraft:vine",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:cobblestone",
        "count": 1
      },
      {
        "id": "minecraft:vine",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "mossy_cobblestone_slab",
    "input": {
      "item": "minecraft:mossy_cobblestone_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:mossy_cobblestone",
      "minecraft:mossy_cobblestone",
      "minecraft:mossy_cobblestone",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:mossy_cobblestone",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "mossy_cobblestone_stairs",
    "input": {
      "item": "minecraft:mossy_cobblestone_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:mossy_cobblestone",
      None,
      None,
      "minecraft:mossy_cobblestone",
      "minecraft:mossy_cobblestone",
      None,
      "minecraft:mossy_cobblestone",
      "minecraft:mossy_cobblestone",
      "minecraft:mossy_cobblestone"
    ],
    "output": [
      {
        "id": "minecraft:mossy_cobblestone",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "mossy_cobblestone_wall",
    "input": {
      "item": "minecraft:mossy_cobblestone_wall",
      "count": 6
    },
    "output_display": [
      "minecraft:mossy_cobblestone",
      "minecraft:mossy_cobblestone",
      "minecraft:mossy_cobblestone",
      "minecraft:mossy_cobblestone",
      "minecraft:mossy_cobblestone",
      "minecraft:mossy_cobblestone",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:mossy_cobblestone",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "mossy_stone_bricks_from_moss_block",
    "input": {
      "item": "minecraft:mossy_stone_bricks",
      "count": 1
    },
    "output_display": [
      "minecraft:stone_bricks",
      "minecraft:moss_block",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:stone_bricks",
        "count": 1
      },
      {
        "id": "minecraft:moss_block",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "mossy_stone_bricks_from_vine",
    "input": {
      "item": "minecraft:mossy_stone_bricks",
      "count": 1
    },
    "output_display": [
      "minecraft:stone_bricks",
      "minecraft:vine",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:stone_bricks",
        "count": 1
      },
      {
        "id": "minecraft:vine",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "mossy_stone_brick_slab",
    "input": {
      "item": "minecraft:mossy_stone_brick_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:mossy_stone_bricks",
      "minecraft:mossy_stone_bricks",
      "minecraft:mossy_stone_bricks",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:mossy_stone_bricks",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "mossy_stone_brick_stairs",
    "input": {
      "item": "minecraft:mossy_stone_brick_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:mossy_stone_bricks",
      None,
      None,
      "minecraft:mossy_stone_bricks",
      "minecraft:mossy_stone_bricks",
      None,
      "minecraft:mossy_stone_bricks",
      "minecraft:mossy_stone_bricks",
      "minecraft:mossy_stone_bricks"
    ],
    "output": [
      {
        "id": "minecraft:mossy_stone_bricks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "mossy_stone_brick_wall",
    "input": {
      "item": "minecraft:mossy_stone_brick_wall",
      "count": 6
    },
    "output_display": [
      "minecraft:mossy_stone_bricks",
      "minecraft:mossy_stone_bricks",
      "minecraft:mossy_stone_bricks",
      "minecraft:mossy_stone_bricks",
      "minecraft:mossy_stone_bricks",
      "minecraft:mossy_stone_bricks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:mossy_stone_bricks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "moss_carpet",
    "input": {
      "item": "minecraft:moss_carpet",
      "count": 3
    },
    "output_display": [
      "minecraft:moss_block",
      "minecraft:moss_block",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:moss_block",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "muddy_mangrove_roots",
    "input": {
      "item": "minecraft:muddy_mangrove_roots",
      "count": 1
    },
    "output_display": [
      "minecraft:mud",
      "minecraft:mangrove_roots",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:mud",
        "count": 1
      },
      {
        "id": "minecraft:mangrove_roots",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "mud_bricks",
    "input": {
      "item": "minecraft:mud_bricks",
      "count": 4
    },
    "output_display": [
      "minecraft:packed_mud",
      "minecraft:packed_mud",
      None,
      "minecraft:packed_mud",
      "minecraft:packed_mud",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:packed_mud",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "mud_brick_slab",
    "input": {
      "item": "minecraft:mud_brick_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:mud_bricks",
      "minecraft:mud_bricks",
      "minecraft:mud_bricks",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:mud_bricks",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "mud_brick_stairs",
    "input": {
      "item": "minecraft:mud_brick_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:mud_bricks",
      None,
      None,
      "minecraft:mud_bricks",
      "minecraft:mud_bricks",
      None,
      "minecraft:mud_bricks",
      "minecraft:mud_bricks",
      "minecraft:mud_bricks"
    ],
    "output": [
      {
        "id": "minecraft:mud_bricks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "mud_brick_wall",
    "input": {
      "item": "minecraft:mud_brick_wall",
      "count": 6
    },
    "output_display": [
      "minecraft:mud_bricks",
      "minecraft:mud_bricks",
      "minecraft:mud_bricks",
      "minecraft:mud_bricks",
      "minecraft:mud_bricks",
      "minecraft:mud_bricks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:mud_bricks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "mushroom_stew",
    "input": {
      "item": "minecraft:mushroom_stew",
      "count": 1
    },
    "output_display": [
      "minecraft:brown_mushroom",
      "minecraft:red_mushroom",
      "minecraft:bowl",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:brown_mushroom",
        "count": 1
      },
      {
        "id": "minecraft:red_mushroom",
        "count": 1
      },
      {
        "id": "minecraft:bowl",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "music_disc_5",
    "input": {
      "item": "minecraft:music_disc_5",
      "count": 1
    },
    "output_display": [
      "minecraft:disc_fragment_5",
      "minecraft:disc_fragment_5",
      "minecraft:disc_fragment_5",
      "minecraft:disc_fragment_5",
      "minecraft:disc_fragment_5",
      "minecraft:disc_fragment_5",
      "minecraft:disc_fragment_5",
      "minecraft:disc_fragment_5",
      "minecraft:disc_fragment_5"
    ],
    "output": [
      {
        "id": "minecraft:disc_fragment_5",
        "count": 9
      }
    ]
  },
  {
    "crafting_recipe_name": "netherite_block",
    "input": {
      "item": "minecraft:netherite_block",
      "count": 1
    },
    "output_display": [
      "minecraft:netherite_ingot",
      "minecraft:netherite_ingot",
      "minecraft:netherite_ingot",
      "minecraft:netherite_ingot",
      "minecraft:netherite_ingot",
      "minecraft:netherite_ingot",
      "minecraft:netherite_ingot",
      "minecraft:netherite_ingot",
      "minecraft:netherite_ingot"
    ],
    "output": [
      {
        "id": "minecraft:netherite_ingot",
        "count": 9
      }
    ]
  },
  {
    "crafting_recipe_name": "netherite_ingot",
    "input": {
      "item": "minecraft:netherite_ingot",
      "count": 1
    },
    "output_display": [
      "minecraft:netherite_scrap",
      "minecraft:netherite_scrap",
      "minecraft:netherite_scrap",
      "minecraft:netherite_scrap",
      "minecraft:gold_ingot",
      "minecraft:gold_ingot",
      "minecraft:gold_ingot",
      "minecraft:gold_ingot",
      None
    ],
    "output": [
      {
        "id": "minecraft:netherite_scrap",
        "count": 4
      },
      {
        "id": "minecraft:gold_ingot",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "netherite_ingot_from_netherite_block",
    "input": {
      "item": "minecraft:netherite_ingot",
      "count": 9
    },
    "output_display": [
      "minecraft:netherite_block",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:netherite_block",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "netherite_upgrade_smithing_template",
    "input": {
      "item": "minecraft:netherite_upgrade_smithing_template",
      "count": 2
    },
    "output_display": [
      "minecraft:diamond",
      "minecraft:netherite_upgrade_smithing_template",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:netherrack",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:diamond"
    ],
    "output": [
      {
        "id": "minecraft:diamond",
        "count": 7
      },
      {
        "id": "minecraft:netherite_upgrade_smithing_template",
        "count": 1
      },
      {
        "id": "minecraft:netherrack",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "nether_bricks",
    "input": {
      "item": "minecraft:nether_bricks",
      "count": 1
    },
    "output_display": [
      "minecraft:nether_brick",
      "minecraft:nether_brick",
      None,
      "minecraft:nether_brick",
      "minecraft:nether_brick",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:nether_brick",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "nether_brick_fence",
    "input": {
      "item": "minecraft:nether_brick_fence",
      "count": 6
    },
    "output_display": [
      "minecraft:nether_bricks",
      "minecraft:nether_brick",
      "minecraft:nether_bricks",
      "minecraft:nether_bricks",
      "minecraft:nether_brick",
      "minecraft:nether_bricks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:nether_bricks",
        "count": 4
      },
      {
        "id": "minecraft:nether_brick",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "nether_brick_slab",
    "input": {
      "item": "minecraft:nether_brick_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:nether_bricks",
      "minecraft:nether_bricks",
      "minecraft:nether_bricks",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:nether_bricks",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "nether_brick_stairs",
    "input": {
      "item": "minecraft:nether_brick_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:nether_bricks",
      None,
      None,
      "minecraft:nether_bricks",
      "minecraft:nether_bricks",
      None,
      "minecraft:nether_bricks",
      "minecraft:nether_bricks",
      "minecraft:nether_bricks"
    ],
    "output": [
      {
        "id": "minecraft:nether_bricks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "nether_brick_wall",
    "input": {
      "item": "minecraft:nether_brick_wall",
      "count": 6
    },
    "output_display": [
      "minecraft:nether_bricks",
      "minecraft:nether_bricks",
      "minecraft:nether_bricks",
      "minecraft:nether_bricks",
      "minecraft:nether_bricks",
      "minecraft:nether_bricks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:nether_bricks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "nether_wart_block",
    "input": {
      "item": "minecraft:nether_wart_block",
      "count": 1
    },
    "output_display": [
      "minecraft:nether_wart",
      "minecraft:nether_wart",
      "minecraft:nether_wart",
      "minecraft:nether_wart",
      "minecraft:nether_wart",
      "minecraft:nether_wart",
      "minecraft:nether_wart",
      "minecraft:nether_wart",
      "minecraft:nether_wart"
    ],
    "output": [
      {
        "id": "minecraft:nether_wart",
        "count": 9
      }
    ]
  },
  {
    "crafting_recipe_name": "note_block",
    "input": {
      "item": "minecraft:note_block",
      "count": 1
    },
    "output_display": [
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:redstone",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:oak_planks"
    ],
    "output": [
      {
        "id": "minecraft:oak_planks",
        "count": 8
      },
      {
        "id": "minecraft:redstone",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "oak_boat",
    "input": {
      "item": "minecraft:oak_boat",
      "count": 1
    },
    "output_display": [
      "minecraft:oak_planks",
      None,
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:oak_planks",
        "count": 5
      }
    ]
  },
  {
    "crafting_recipe_name": "oak_button",
    "input": {
      "item": "minecraft:oak_button",
      "count": 1
    },
    "output_display": [
      "minecraft:oak_planks",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:oak_planks",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "oak_chest_boat",
    "input": {
      "item": "minecraft:oak_chest_boat",
      "count": 1
    },
    "output_display": [
      "minecraft:chest",
      "minecraft:oak_boat",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:chest",
        "count": 1
      },
      {
        "id": "minecraft:oak_boat",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "oak_door",
    "input": {
      "item": "minecraft:oak_door",
      "count": 3
    },
    "output_display": [
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      None,
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      None,
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      None
    ],
    "output": [
      {
        "id": "minecraft:oak_planks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "oak_fence",
    "input": {
      "item": "minecraft:oak_fence",
      "count": 3
    },
    "output_display": [
      "minecraft:oak_planks",
      "minecraft:stick",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:stick",
      "minecraft:oak_planks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:oak_planks",
        "count": 4
      },
      {
        "id": "minecraft:stick",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "oak_fence_gate",
    "input": {
      "item": "minecraft:oak_fence_gate",
      "count": 1
    },
    "output_display": [
      "minecraft:stick",
      "minecraft:oak_planks",
      "minecraft:stick",
      "minecraft:stick",
      "minecraft:oak_planks",
      "minecraft:stick",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:stick",
        "count": 4
      },
      {
        "id": "minecraft:oak_planks",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "oak_hanging_sign",
    "input": {
      "item": "minecraft:oak_hanging_sign",
      "count": 6
    },
    "output_display": [
      "minecraft:chain",
      None,
      "minecraft:chain",
      "minecraft:stripped_oak_log",
      "minecraft:stripped_oak_log",
      "minecraft:stripped_oak_log",
      "minecraft:stripped_oak_log",
      "minecraft:stripped_oak_log",
      "minecraft:stripped_oak_log"
    ],
    "output": [
      {
        "id": "minecraft:chain",
        "count": 2
      },
      {
        "id": "minecraft:stripped_oak_log",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "oak_planks",
    "input": {
      "item": "minecraft:oak_planks",
      "count": 4
    },
    "output_display": [
      "minecraft:oak_log",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:oak_log",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "oak_pressure_plate",
    "input": {
      "item": "minecraft:oak_pressure_plate",
      "count": 1
    },
    "output_display": [
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:oak_planks",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "oak_sign",
    "input": {
      "item": "minecraft:oak_sign",
      "count": 3
    },
    "output_display": [
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      None,
      "minecraft:stick",
      None
    ],
    "output": [
      {
        "id": "minecraft:oak_planks",
        "count": 6
      },
      {
        "id": "minecraft:stick",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "oak_slab",
    "input": {
      "item": "minecraft:oak_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:oak_planks",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "oak_stairs",
    "input": {
      "item": "minecraft:oak_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:oak_planks",
      None,
      None,
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      None,
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:oak_planks"
    ],
    "output": [
      {
        "id": "minecraft:oak_planks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "oak_trapdoor",
    "input": {
      "item": "minecraft:oak_trapdoor",
      "count": 2
    },
    "output_display": [
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:oak_planks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "oak_wood",
    "input": {
      "item": "minecraft:oak_wood",
      "count": 3
    },
    "output_display": [
      "minecraft:oak_log",
      "minecraft:oak_log",
      None,
      "minecraft:oak_log",
      "minecraft:oak_log",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:oak_log",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "observer",
    "input": {
      "item": "minecraft:observer",
      "count": 1
    },
    "output_display": [
      "minecraft:cobblestone",
      "minecraft:cobblestone",
      "minecraft:cobblestone",
      "minecraft:redstone",
      "minecraft:redstone",
      "minecraft:quartz",
      "minecraft:cobblestone",
      "minecraft:cobblestone",
      "minecraft:cobblestone"
    ],
    "output": [
      {
        "id": "minecraft:cobblestone",
        "count": 6
      },
      {
        "id": "minecraft:redstone",
        "count": 2
      },
      {
        "id": "minecraft:quartz",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "orange_banner",
    "input": {
      "item": "minecraft:orange_banner",
      "count": 1
    },
    "output_display": [
      "minecraft:orange_wool",
      "minecraft:orange_wool",
      "minecraft:orange_wool",
      "minecraft:orange_wool",
      "minecraft:orange_wool",
      "minecraft:orange_wool",
      None,
      "minecraft:stick",
      None
    ],
    "output": [
      {
        "id": "minecraft:orange_wool",
        "count": 6
      },
      {
        "id": "minecraft:stick",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "orange_bed",
    "input": {
      "item": "minecraft:orange_bed",
      "count": 1
    },
    "output_display": [
      "minecraft:orange_wool",
      "minecraft:orange_wool",
      "minecraft:orange_wool",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:orange_wool",
        "count": 3
      },
      {
        "id": "minecraft:oak_planks",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "orange_candle",
    "input": {
      "item": "minecraft:orange_candle",
      "count": 1
    },
    "output_display": [
      "minecraft:candle",
      "minecraft:orange_dye",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:candle",
        "count": 1
      },
      {
        "id": "minecraft:orange_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "orange_carpet",
    "input": {
      "item": "minecraft:orange_carpet",
      "count": 3
    },
    "output_display": [
      "minecraft:orange_wool",
      "minecraft:orange_wool",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:orange_wool",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "orange_concrete_powder",
    "input": {
      "item": "minecraft:orange_concrete_powder",
      "count": 8
    },
    "output_display": [
      "minecraft:orange_dye",
      "minecraft:sand",
      "minecraft:sand",
      "minecraft:sand",
      "minecraft:sand",
      "minecraft:gravel",
      "minecraft:gravel",
      "minecraft:gravel",
      "minecraft:gravel"
    ],
    "output": [
      {
        "id": "minecraft:orange_dye",
        "count": 1
      },
      {
        "id": "minecraft:sand",
        "count": 4
      },
      {
        "id": "minecraft:gravel",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "orange_dye_from_open_eyeblossom",
    "input": {
      "item": "minecraft:orange_dye",
      "count": 1
    },
    "output_display": [
      "minecraft:open_eyeblossom",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:open_eyeblossom",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "orange_dye_from_orange_tulip",
    "input": {
      "item": "minecraft:orange_dye",
      "count": 1
    },
    "output_display": [
      "minecraft:orange_tulip",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:orange_tulip",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "orange_dye_from_red_yellow",
    "input": {
      "item": "minecraft:orange_dye",
      "count": 2
    },
    "output_display": [
      "minecraft:red_dye",
      "minecraft:yellow_dye",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:red_dye",
        "count": 1
      },
      {
        "id": "minecraft:yellow_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "orange_dye_from_torchflower",
    "input": {
      "item": "minecraft:orange_dye",
      "count": 1
    },
    "output_display": [
      "minecraft:torchflower",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:torchflower",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "orange_stained_glass",
    "input": {
      "item": "minecraft:orange_stained_glass",
      "count": 8
    },
    "output_display": [
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:orange_dye",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass"
    ],
    "output": [
      {
        "id": "minecraft:glass",
        "count": 8
      },
      {
        "id": "minecraft:orange_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "orange_stained_glass_pane",
    "input": {
      "item": "minecraft:orange_stained_glass_pane",
      "count": 16
    },
    "output_display": [
      "minecraft:orange_stained_glass",
      "minecraft:orange_stained_glass",
      "minecraft:orange_stained_glass",
      "minecraft:orange_stained_glass",
      "minecraft:orange_stained_glass",
      "minecraft:orange_stained_glass",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:orange_stained_glass",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "orange_stained_glass_pane_from_glass_pane",
    "input": {
      "item": "minecraft:orange_stained_glass_pane",
      "count": 8
    },
    "output_display": [
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:orange_dye",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane"
    ],
    "output": [
      {
        "id": "minecraft:glass_pane",
        "count": 8
      },
      {
        "id": "minecraft:orange_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "orange_terracotta",
    "input": {
      "item": "minecraft:orange_terracotta",
      "count": 8
    },
    "output_display": [
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:orange_dye",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta"
    ],
    "output": [
      {
        "id": "minecraft:terracotta",
        "count": 8
      },
      {
        "id": "minecraft:orange_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "oxidized_chiseled_copper",
    "input": {
      "item": "minecraft:oxidized_chiseled_copper",
      "count": 1
    },
    "output_display": [
      "minecraft:oxidized_cut_copper_slab",
      None,
      None,
      "minecraft:oxidized_cut_copper_slab",
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:oxidized_cut_copper_slab",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "oxidized_copper_bulb",
    "input": {
      "item": "minecraft:oxidized_copper_bulb",
      "count": 4
    },
    "output_display": [
      None,
      "minecraft:oxidized_copper",
      None,
      "minecraft:oxidized_copper",
      "minecraft:blaze_rod",
      "minecraft:oxidized_copper",
      None,
      "minecraft:redstone",
      None
    ],
    "output": [
      {
        "id": "minecraft:oxidized_copper",
        "count": 3
      },
      {
        "id": "minecraft:blaze_rod",
        "count": 1
      },
      {
        "id": "minecraft:redstone",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "oxidized_copper_grate",
    "input": {
      "item": "minecraft:oxidized_copper_grate",
      "count": 4
    },
    "output_display": [
      None,
      "minecraft:oxidized_copper",
      None,
      "minecraft:oxidized_copper",
      None,
      "minecraft:oxidized_copper",
      None,
      "minecraft:oxidized_copper",
      None
    ],
    "output": [
      {
        "id": "minecraft:oxidized_copper",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "oxidized_cut_copper",
    "input": {
      "item": "minecraft:oxidized_cut_copper",
      "count": 4
    },
    "output_display": [
      "minecraft:oxidized_copper",
      "minecraft:oxidized_copper",
      None,
      "minecraft:oxidized_copper",
      "minecraft:oxidized_copper",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:oxidized_copper",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "oxidized_cut_copper_slab",
    "input": {
      "item": "minecraft:oxidized_cut_copper_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:oxidized_cut_copper",
      "minecraft:oxidized_cut_copper",
      "minecraft:oxidized_cut_copper",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:oxidized_cut_copper",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "oxidized_cut_copper_stairs",
    "input": {
      "item": "minecraft:oxidized_cut_copper_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:oxidized_cut_copper",
      None,
      None,
      "minecraft:oxidized_cut_copper",
      "minecraft:oxidized_cut_copper",
      None,
      "minecraft:oxidized_cut_copper",
      "minecraft:oxidized_cut_copper",
      "minecraft:oxidized_cut_copper"
    ],
    "output": [
      {
        "id": "minecraft:oxidized_cut_copper",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "packed_ice",
    "input": {
      "item": "minecraft:packed_ice",
      "count": 1
    },
    "output_display": [
      "minecraft:ice",
      "minecraft:ice",
      "minecraft:ice",
      "minecraft:ice",
      "minecraft:ice",
      "minecraft:ice",
      "minecraft:ice",
      "minecraft:ice",
      "minecraft:ice"
    ],
    "output": [
      {
        "id": "minecraft:ice",
        "count": 9
      }
    ]
  },
  {
    "crafting_recipe_name": "packed_mud",
    "input": {
      "item": "minecraft:packed_mud",
      "count": 1
    },
    "output_display": [
      "minecraft:mud",
      "minecraft:wheat",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:mud",
        "count": 1
      },
      {
        "id": "minecraft:wheat",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "painting",
    "input": {
      "item": "minecraft:painting",
      "count": 1
    },
    "output_display": [
      "minecraft:stick",
      "minecraft:stick",
      "minecraft:stick",
      "minecraft:stick",
      "minecraft:white_wool",
      "minecraft:stick",
      "minecraft:stick",
      "minecraft:stick",
      "minecraft:stick"
    ],
    "output": [
      {
        "id": "minecraft:stick",
        "count": 8
      },
      {
        "id": "minecraft:white_wool",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "pale_moss_carpet",
    "input": {
      "item": "minecraft:pale_moss_carpet",
      "count": 3
    },
    "output_display": [
      "minecraft:pale_moss_block",
      "minecraft:pale_moss_block",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:pale_moss_block",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "pale_oak_boat",
    "input": {
      "item": "minecraft:pale_oak_boat",
      "count": 1
    },
    "output_display": [
      "minecraft:pale_oak_planks",
      None,
      "minecraft:pale_oak_planks",
      "minecraft:pale_oak_planks",
      "minecraft:pale_oak_planks",
      "minecraft:pale_oak_planks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:pale_oak_planks",
        "count": 5
      }
    ]
  },
  {
    "crafting_recipe_name": "pale_oak_button",
    "input": {
      "item": "minecraft:pale_oak_button",
      "count": 1
    },
    "output_display": [
      "minecraft:pale_oak_planks",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:pale_oak_planks",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "pale_oak_chest_boat",
    "input": {
      "item": "minecraft:pale_oak_chest_boat",
      "count": 1
    },
    "output_display": [
      "minecraft:chest",
      "minecraft:pale_oak_boat",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:chest",
        "count": 1
      },
      {
        "id": "minecraft:pale_oak_boat",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "pale_oak_door",
    "input": {
      "item": "minecraft:pale_oak_door",
      "count": 3
    },
    "output_display": [
      "minecraft:pale_oak_planks",
      "minecraft:pale_oak_planks",
      None,
      "minecraft:pale_oak_planks",
      "minecraft:pale_oak_planks",
      None,
      "minecraft:pale_oak_planks",
      "minecraft:pale_oak_planks",
      None
    ],
    "output": [
      {
        "id": "minecraft:pale_oak_planks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "pale_oak_fence",
    "input": {
      "item": "minecraft:pale_oak_fence",
      "count": 3
    },
    "output_display": [
      "minecraft:pale_oak_planks",
      "minecraft:stick",
      "minecraft:pale_oak_planks",
      "minecraft:pale_oak_planks",
      "minecraft:stick",
      "minecraft:pale_oak_planks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:pale_oak_planks",
        "count": 4
      },
      {
        "id": "minecraft:stick",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "pale_oak_fence_gate",
    "input": {
      "item": "minecraft:pale_oak_fence_gate",
      "count": 1
    },
    "output_display": [
      "minecraft:stick",
      "minecraft:pale_oak_planks",
      "minecraft:stick",
      "minecraft:stick",
      "minecraft:pale_oak_planks",
      "minecraft:stick",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:stick",
        "count": 4
      },
      {
        "id": "minecraft:pale_oak_planks",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "pale_oak_hanging_sign",
    "input": {
      "item": "minecraft:pale_oak_hanging_sign",
      "count": 6
    },
    "output_display": [
      "minecraft:chain",
      None,
      "minecraft:chain",
      "minecraft:stripped_pale_oak_log",
      "minecraft:stripped_pale_oak_log",
      "minecraft:stripped_pale_oak_log",
      "minecraft:stripped_pale_oak_log",
      "minecraft:stripped_pale_oak_log",
      "minecraft:stripped_pale_oak_log"
    ],
    "output": [
      {
        "id": "minecraft:chain",
        "count": 2
      },
      {
        "id": "minecraft:stripped_pale_oak_log",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "pale_oak_planks",
    "input": {
      "item": "minecraft:pale_oak_planks",
      "count": 4
    },
    "output_display": [
      "#minecraft:pale_oak_logs",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "#minecraft:pale_oak_logs",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "pale_oak_pressure_plate",
    "input": {
      "item": "minecraft:pale_oak_pressure_plate",
      "count": 1
    },
    "output_display": [
      "minecraft:pale_oak_planks",
      "minecraft:pale_oak_planks",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:pale_oak_planks",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "pale_oak_sign",
    "input": {
      "item": "minecraft:pale_oak_sign",
      "count": 3
    },
    "output_display": [
      "minecraft:pale_oak_planks",
      "minecraft:pale_oak_planks",
      "minecraft:pale_oak_planks",
      "minecraft:pale_oak_planks",
      "minecraft:pale_oak_planks",
      "minecraft:pale_oak_planks",
      None,
      "minecraft:stick",
      None
    ],
    "output": [
      {
        "id": "minecraft:pale_oak_planks",
        "count": 6
      },
      {
        "id": "minecraft:stick",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "pale_oak_slab",
    "input": {
      "item": "minecraft:pale_oak_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:pale_oak_planks",
      "minecraft:pale_oak_planks",
      "minecraft:pale_oak_planks",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:pale_oak_planks",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "pale_oak_stairs",
    "input": {
      "item": "minecraft:pale_oak_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:pale_oak_planks",
      None,
      None,
      "minecraft:pale_oak_planks",
      "minecraft:pale_oak_planks",
      None,
      "minecraft:pale_oak_planks",
      "minecraft:pale_oak_planks",
      "minecraft:pale_oak_planks"
    ],
    "output": [
      {
        "id": "minecraft:pale_oak_planks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "pale_oak_trapdoor",
    "input": {
      "item": "minecraft:pale_oak_trapdoor",
      "count": 2
    },
    "output_display": [
      "minecraft:pale_oak_planks",
      "minecraft:pale_oak_planks",
      "minecraft:pale_oak_planks",
      "minecraft:pale_oak_planks",
      "minecraft:pale_oak_planks",
      "minecraft:pale_oak_planks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:pale_oak_planks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "pale_oak_wood",
    "input": {
      "item": "minecraft:pale_oak_wood",
      "count": 3
    },
    "output_display": [
      "minecraft:pale_oak_log",
      "minecraft:pale_oak_log",
      None,
      "minecraft:pale_oak_log",
      "minecraft:pale_oak_log",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:pale_oak_log",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "paper",
    "input": {
      "item": "minecraft:paper",
      "count": 3
    },
    "output_display": [
      "minecraft:sugar_cane",
      "minecraft:sugar_cane",
      "minecraft:sugar_cane",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:sugar_cane",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "pink_banner",
    "input": {
      "item": "minecraft:pink_banner",
      "count": 1
    },
    "output_display": [
      "minecraft:pink_wool",
      "minecraft:pink_wool",
      "minecraft:pink_wool",
      "minecraft:pink_wool",
      "minecraft:pink_wool",
      "minecraft:pink_wool",
      None,
      "minecraft:stick",
      None
    ],
    "output": [
      {
        "id": "minecraft:pink_wool",
        "count": 6
      },
      {
        "id": "minecraft:stick",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "pink_bed",
    "input": {
      "item": "minecraft:pink_bed",
      "count": 1
    },
    "output_display": [
      "minecraft:pink_wool",
      "minecraft:pink_wool",
      "minecraft:pink_wool",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:pink_wool",
        "count": 3
      },
      {
        "id": "minecraft:oak_planks",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "pink_candle",
    "input": {
      "item": "minecraft:pink_candle",
      "count": 1
    },
    "output_display": [
      "minecraft:candle",
      "minecraft:pink_dye",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:candle",
        "count": 1
      },
      {
        "id": "minecraft:pink_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "pink_carpet",
    "input": {
      "item": "minecraft:pink_carpet",
      "count": 3
    },
    "output_display": [
      "minecraft:pink_wool",
      "minecraft:pink_wool",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:pink_wool",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "pink_concrete_powder",
    "input": {
      "item": "minecraft:pink_concrete_powder",
      "count": 8
    },
    "output_display": [
      "minecraft:pink_dye",
      "minecraft:sand",
      "minecraft:sand",
      "minecraft:sand",
      "minecraft:sand",
      "minecraft:gravel",
      "minecraft:gravel",
      "minecraft:gravel",
      "minecraft:gravel"
    ],
    "output": [
      {
        "id": "minecraft:pink_dye",
        "count": 1
      },
      {
        "id": "minecraft:sand",
        "count": 4
      },
      {
        "id": "minecraft:gravel",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "pink_dye_from_peony",
    "input": {
      "item": "minecraft:pink_dye",
      "count": 2
    },
    "output_display": [
      "minecraft:peony",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:peony",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "pink_dye_from_pink_petals",
    "input": {
      "item": "minecraft:pink_dye",
      "count": 1
    },
    "output_display": [
      "minecraft:pink_petals",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:pink_petals",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "pink_dye_from_pink_tulip",
    "input": {
      "item": "minecraft:pink_dye",
      "count": 1
    },
    "output_display": [
      "minecraft:pink_tulip",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:pink_tulip",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "pink_dye_from_red_white_dye",
    "input": {
      "item": "minecraft:pink_dye",
      "count": 2
    },
    "output_display": [
      "minecraft:red_dye",
      "minecraft:white_dye",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:red_dye",
        "count": 1
      },
      {
        "id": "minecraft:white_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "pink_stained_glass",
    "input": {
      "item": "minecraft:pink_stained_glass",
      "count": 8
    },
    "output_display": [
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:pink_dye",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass"
    ],
    "output": [
      {
        "id": "minecraft:glass",
        "count": 8
      },
      {
        "id": "minecraft:pink_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "pink_stained_glass_pane",
    "input": {
      "item": "minecraft:pink_stained_glass_pane",
      "count": 16
    },
    "output_display": [
      "minecraft:pink_stained_glass",
      "minecraft:pink_stained_glass",
      "minecraft:pink_stained_glass",
      "minecraft:pink_stained_glass",
      "minecraft:pink_stained_glass",
      "minecraft:pink_stained_glass",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:pink_stained_glass",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "pink_stained_glass_pane_from_glass_pane",
    "input": {
      "item": "minecraft:pink_stained_glass_pane",
      "count": 8
    },
    "output_display": [
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:pink_dye",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane"
    ],
    "output": [
      {
        "id": "minecraft:glass_pane",
        "count": 8
      },
      {
        "id": "minecraft:pink_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "pink_terracotta",
    "input": {
      "item": "minecraft:pink_terracotta",
      "count": 8
    },
    "output_display": [
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:pink_dye",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta"
    ],
    "output": [
      {
        "id": "minecraft:terracotta",
        "count": 8
      },
      {
        "id": "minecraft:pink_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "piston",
    "input": {
      "item": "minecraft:piston",
      "count": 1
    },
    "output_display": [
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:cobblestone",
      "minecraft:iron_ingot",
      "minecraft:cobblestone",
      "minecraft:cobblestone",
      "minecraft:redstone",
      "minecraft:cobblestone"
    ],
    "output": [
      {
        "id": "minecraft:oak_planks",
        "count": 3
      },
      {
        "id": "minecraft:cobblestone",
        "count": 4
      },
      {
        "id": "minecraft:iron_ingot",
        "count": 1
      },
      {
        "id": "minecraft:redstone",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "polished_andesite",
    "input": {
      "item": "minecraft:polished_andesite",
      "count": 4
    },
    "output_display": [
      "minecraft:andesite",
      "minecraft:andesite",
      None,
      "minecraft:andesite",
      "minecraft:andesite",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:andesite",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "polished_andesite_slab",
    "input": {
      "item": "minecraft:polished_andesite_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:polished_andesite",
      "minecraft:polished_andesite",
      "minecraft:polished_andesite",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:polished_andesite",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "polished_andesite_stairs",
    "input": {
      "item": "minecraft:polished_andesite_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:polished_andesite",
      None,
      None,
      "minecraft:polished_andesite",
      "minecraft:polished_andesite",
      None,
      "minecraft:polished_andesite",
      "minecraft:polished_andesite",
      "minecraft:polished_andesite"
    ],
    "output": [
      {
        "id": "minecraft:polished_andesite",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "polished_basalt",
    "input": {
      "item": "minecraft:polished_basalt",
      "count": 4
    },
    "output_display": [
      "minecraft:basalt",
      "minecraft:basalt",
      None,
      "minecraft:basalt",
      "minecraft:basalt",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:basalt",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "polished_blackstone",
    "input": {
      "item": "minecraft:polished_blackstone",
      "count": 4
    },
    "output_display": [
      "minecraft:blackstone",
      "minecraft:blackstone",
      None,
      "minecraft:blackstone",
      "minecraft:blackstone",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:blackstone",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "polished_blackstone_bricks",
    "input": {
      "item": "minecraft:polished_blackstone_bricks",
      "count": 4
    },
    "output_display": [
      "minecraft:polished_blackstone",
      "minecraft:polished_blackstone",
      None,
      "minecraft:polished_blackstone",
      "minecraft:polished_blackstone",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:polished_blackstone",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "polished_blackstone_brick_slab",
    "input": {
      "item": "minecraft:polished_blackstone_brick_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:polished_blackstone_bricks",
      "minecraft:polished_blackstone_bricks",
      "minecraft:polished_blackstone_bricks",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:polished_blackstone_bricks",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "polished_blackstone_brick_stairs",
    "input": {
      "item": "minecraft:polished_blackstone_brick_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:polished_blackstone_bricks",
      None,
      None,
      "minecraft:polished_blackstone_bricks",
      "minecraft:polished_blackstone_bricks",
      None,
      "minecraft:polished_blackstone_bricks",
      "minecraft:polished_blackstone_bricks",
      "minecraft:polished_blackstone_bricks"
    ],
    "output": [
      {
        "id": "minecraft:polished_blackstone_bricks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "polished_blackstone_brick_wall",
    "input": {
      "item": "minecraft:polished_blackstone_brick_wall",
      "count": 6
    },
    "output_display": [
      "minecraft:polished_blackstone_bricks",
      "minecraft:polished_blackstone_bricks",
      "minecraft:polished_blackstone_bricks",
      "minecraft:polished_blackstone_bricks",
      "minecraft:polished_blackstone_bricks",
      "minecraft:polished_blackstone_bricks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:polished_blackstone_bricks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "polished_blackstone_button",
    "input": {
      "item": "minecraft:polished_blackstone_button",
      "count": 1
    },
    "output_display": [
      "minecraft:polished_blackstone",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:polished_blackstone",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "polished_blackstone_pressure_plate",
    "input": {
      "item": "minecraft:polished_blackstone_pressure_plate",
      "count": 1
    },
    "output_display": [
      "minecraft:polished_blackstone",
      "minecraft:polished_blackstone",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:polished_blackstone",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "polished_blackstone_slab",
    "input": {
      "item": "minecraft:polished_blackstone_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:polished_blackstone",
      "minecraft:polished_blackstone",
      "minecraft:polished_blackstone",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:polished_blackstone",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "polished_blackstone_stairs",
    "input": {
      "item": "minecraft:polished_blackstone_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:polished_blackstone",
      None,
      None,
      "minecraft:polished_blackstone",
      "minecraft:polished_blackstone",
      None,
      "minecraft:polished_blackstone",
      "minecraft:polished_blackstone",
      "minecraft:polished_blackstone"
    ],
    "output": [
      {
        "id": "minecraft:polished_blackstone",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "polished_blackstone_wall",
    "input": {
      "item": "minecraft:polished_blackstone_wall",
      "count": 6
    },
    "output_display": [
      "minecraft:polished_blackstone",
      "minecraft:polished_blackstone",
      "minecraft:polished_blackstone",
      "minecraft:polished_blackstone",
      "minecraft:polished_blackstone",
      "minecraft:polished_blackstone",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:polished_blackstone",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "polished_deepslate",
    "input": {
      "item": "minecraft:polished_deepslate",
      "count": 4
    },
    "output_display": [
      "minecraft:cobbled_deepslate",
      "minecraft:cobbled_deepslate",
      None,
      "minecraft:cobbled_deepslate",
      "minecraft:cobbled_deepslate",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:cobbled_deepslate",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "polished_deepslate_slab",
    "input": {
      "item": "minecraft:polished_deepslate_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:polished_deepslate",
      "minecraft:polished_deepslate",
      "minecraft:polished_deepslate",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:polished_deepslate",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "polished_deepslate_stairs",
    "input": {
      "item": "minecraft:polished_deepslate_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:polished_deepslate",
      None,
      None,
      "minecraft:polished_deepslate",
      "minecraft:polished_deepslate",
      None,
      "minecraft:polished_deepslate",
      "minecraft:polished_deepslate",
      "minecraft:polished_deepslate"
    ],
    "output": [
      {
        "id": "minecraft:polished_deepslate",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "polished_deepslate_wall",
    "input": {
      "item": "minecraft:polished_deepslate_wall",
      "count": 6
    },
    "output_display": [
      "minecraft:polished_deepslate",
      "minecraft:polished_deepslate",
      "minecraft:polished_deepslate",
      "minecraft:polished_deepslate",
      "minecraft:polished_deepslate",
      "minecraft:polished_deepslate",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:polished_deepslate",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "polished_diorite",
    "input": {
      "item": "minecraft:polished_diorite",
      "count": 4
    },
    "output_display": [
      "minecraft:diorite",
      "minecraft:diorite",
      None,
      "minecraft:diorite",
      "minecraft:diorite",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:diorite",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "polished_diorite_slab",
    "input": {
      "item": "minecraft:polished_diorite_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:polished_diorite",
      "minecraft:polished_diorite",
      "minecraft:polished_diorite",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:polished_diorite",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "polished_diorite_stairs",
    "input": {
      "item": "minecraft:polished_diorite_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:polished_diorite",
      None,
      None,
      "minecraft:polished_diorite",
      "minecraft:polished_diorite",
      None,
      "minecraft:polished_diorite",
      "minecraft:polished_diorite",
      "minecraft:polished_diorite"
    ],
    "output": [
      {
        "id": "minecraft:polished_diorite",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "polished_granite",
    "input": {
      "item": "minecraft:polished_granite",
      "count": 4
    },
    "output_display": [
      "minecraft:granite",
      "minecraft:granite",
      None,
      "minecraft:granite",
      "minecraft:granite",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:granite",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "polished_granite_slab",
    "input": {
      "item": "minecraft:polished_granite_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:polished_granite",
      "minecraft:polished_granite",
      "minecraft:polished_granite",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:polished_granite",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "polished_granite_stairs",
    "input": {
      "item": "minecraft:polished_granite_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:polished_granite",
      None,
      None,
      "minecraft:polished_granite",
      "minecraft:polished_granite",
      None,
      "minecraft:polished_granite",
      "minecraft:polished_granite",
      "minecraft:polished_granite"
    ],
    "output": [
      {
        "id": "minecraft:polished_granite",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "polished_tuff",
    "input": {
      "item": "minecraft:polished_tuff",
      "count": 4
    },
    "output_display": [
      "minecraft:tuff",
      "minecraft:tuff",
      None,
      "minecraft:tuff",
      "minecraft:tuff",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:tuff",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "polished_tuff_slab",
    "input": {
      "item": "minecraft:polished_tuff_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:polished_tuff",
      "minecraft:polished_tuff",
      "minecraft:polished_tuff",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:polished_tuff",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "polished_tuff_stairs",
    "input": {
      "item": "minecraft:polished_tuff_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:polished_tuff",
      None,
      None,
      "minecraft:polished_tuff",
      "minecraft:polished_tuff",
      None,
      "minecraft:polished_tuff",
      "minecraft:polished_tuff",
      "minecraft:polished_tuff"
    ],
    "output": [
      {
        "id": "minecraft:polished_tuff",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "polished_tuff_wall",
    "input": {
      "item": "minecraft:polished_tuff_wall",
      "count": 6
    },
    "output_display": [
      "minecraft:polished_tuff",
      "minecraft:polished_tuff",
      "minecraft:polished_tuff",
      "minecraft:polished_tuff",
      "minecraft:polished_tuff",
      "minecraft:polished_tuff",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:polished_tuff",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "powered_rail",
    "input": {
      "item": "minecraft:powered_rail",
      "count": 6
    },
    "output_display": [
      "minecraft:gold_ingot",
      None,
      "minecraft:gold_ingot",
      "minecraft:gold_ingot",
      "minecraft:stick",
      "minecraft:gold_ingot",
      "minecraft:gold_ingot",
      "minecraft:redstone",
      "minecraft:gold_ingot"
    ],
    "output": [
      {
        "id": "minecraft:gold_ingot",
        "count": 6
      },
      {
        "id": "minecraft:stick",
        "count": 1
      },
      {
        "id": "minecraft:redstone",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "prismarine",
    "input": {
      "item": "minecraft:prismarine",
      "count": 1
    },
    "output_display": [
      "minecraft:prismarine_shard",
      "minecraft:prismarine_shard",
      None,
      "minecraft:prismarine_shard",
      "minecraft:prismarine_shard",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:prismarine_shard",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "prismarine_bricks",
    "input": {
      "item": "minecraft:prismarine_bricks",
      "count": 1
    },
    "output_display": [
      "minecraft:prismarine_shard",
      "minecraft:prismarine_shard",
      "minecraft:prismarine_shard",
      "minecraft:prismarine_shard",
      "minecraft:prismarine_shard",
      "minecraft:prismarine_shard",
      "minecraft:prismarine_shard",
      "minecraft:prismarine_shard",
      "minecraft:prismarine_shard"
    ],
    "output": [
      {
        "id": "minecraft:prismarine_shard",
        "count": 9
      }
    ]
  },
  {
    "crafting_recipe_name": "prismarine_brick_slab",
    "input": {
      "item": "minecraft:prismarine_brick_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:prismarine_bricks",
      "minecraft:prismarine_bricks",
      "minecraft:prismarine_bricks",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:prismarine_bricks",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "prismarine_brick_stairs",
    "input": {
      "item": "minecraft:prismarine_brick_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:prismarine_bricks",
      None,
      None,
      "minecraft:prismarine_bricks",
      "minecraft:prismarine_bricks",
      None,
      "minecraft:prismarine_bricks",
      "minecraft:prismarine_bricks",
      "minecraft:prismarine_bricks"
    ],
    "output": [
      {
        "id": "minecraft:prismarine_bricks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "prismarine_slab",
    "input": {
      "item": "minecraft:prismarine_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:prismarine",
      "minecraft:prismarine",
      "minecraft:prismarine",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:prismarine",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "prismarine_stairs",
    "input": {
      "item": "minecraft:prismarine_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:prismarine",
      None,
      None,
      "minecraft:prismarine",
      "minecraft:prismarine",
      None,
      "minecraft:prismarine",
      "minecraft:prismarine",
      "minecraft:prismarine"
    ],
    "output": [
      {
        "id": "minecraft:prismarine",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "prismarine_wall",
    "input": {
      "item": "minecraft:prismarine_wall",
      "count": 6
    },
    "output_display": [
      "minecraft:prismarine",
      "minecraft:prismarine",
      "minecraft:prismarine",
      "minecraft:prismarine",
      "minecraft:prismarine",
      "minecraft:prismarine",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:prismarine",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "pumpkin_pie",
    "input": {
      "item": "minecraft:pumpkin_pie",
      "count": 1
    },
    "output_display": [
      "minecraft:pumpkin",
      "minecraft:sugar",
      "minecraft:egg",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:pumpkin",
        "count": 1
      },
      {
        "id": "minecraft:sugar",
        "count": 1
      },
      {
        "id": "minecraft:egg",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "pumpkin_seeds",
    "input": {
      "item": "minecraft:pumpkin_seeds",
      "count": 4
    },
    "output_display": [
      "minecraft:pumpkin",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:pumpkin",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "purple_banner",
    "input": {
      "item": "minecraft:purple_banner",
      "count": 1
    },
    "output_display": [
      "minecraft:purple_wool",
      "minecraft:purple_wool",
      "minecraft:purple_wool",
      "minecraft:purple_wool",
      "minecraft:purple_wool",
      "minecraft:purple_wool",
      None,
      "minecraft:stick",
      None
    ],
    "output": [
      {
        "id": "minecraft:purple_wool",
        "count": 6
      },
      {
        "id": "minecraft:stick",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "purple_bed",
    "input": {
      "item": "minecraft:purple_bed",
      "count": 1
    },
    "output_display": [
      "minecraft:purple_wool",
      "minecraft:purple_wool",
      "minecraft:purple_wool",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:purple_wool",
        "count": 3
      },
      {
        "id": "minecraft:oak_planks",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "purple_candle",
    "input": {
      "item": "minecraft:purple_candle",
      "count": 1
    },
    "output_display": [
      "minecraft:candle",
      "minecraft:purple_dye",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:candle",
        "count": 1
      },
      {
        "id": "minecraft:purple_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "purple_carpet",
    "input": {
      "item": "minecraft:purple_carpet",
      "count": 3
    },
    "output_display": [
      "minecraft:purple_wool",
      "minecraft:purple_wool",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:purple_wool",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "purple_concrete_powder",
    "input": {
      "item": "minecraft:purple_concrete_powder",
      "count": 8
    },
    "output_display": [
      "minecraft:purple_dye",
      "minecraft:sand",
      "minecraft:sand",
      "minecraft:sand",
      "minecraft:sand",
      "minecraft:gravel",
      "minecraft:gravel",
      "minecraft:gravel",
      "minecraft:gravel"
    ],
    "output": [
      {
        "id": "minecraft:purple_dye",
        "count": 1
      },
      {
        "id": "minecraft:sand",
        "count": 4
      },
      {
        "id": "minecraft:gravel",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "purple_dye",
    "input": {
      "item": "minecraft:purple_dye",
      "count": 2
    },
    "output_display": [
      "minecraft:blue_dye",
      "minecraft:red_dye",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:blue_dye",
        "count": 1
      },
      {
        "id": "minecraft:red_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "purple_stained_glass",
    "input": {
      "item": "minecraft:purple_stained_glass",
      "count": 8
    },
    "output_display": [
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:purple_dye",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass"
    ],
    "output": [
      {
        "id": "minecraft:glass",
        "count": 8
      },
      {
        "id": "minecraft:purple_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "purple_stained_glass_pane",
    "input": {
      "item": "minecraft:purple_stained_glass_pane",
      "count": 16
    },
    "output_display": [
      "minecraft:purple_stained_glass",
      "minecraft:purple_stained_glass",
      "minecraft:purple_stained_glass",
      "minecraft:purple_stained_glass",
      "minecraft:purple_stained_glass",
      "minecraft:purple_stained_glass",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:purple_stained_glass",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "purple_stained_glass_pane_from_glass_pane",
    "input": {
      "item": "minecraft:purple_stained_glass_pane",
      "count": 8
    },
    "output_display": [
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:purple_dye",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane"
    ],
    "output": [
      {
        "id": "minecraft:glass_pane",
        "count": 8
      },
      {
        "id": "minecraft:purple_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "purple_terracotta",
    "input": {
      "item": "minecraft:purple_terracotta",
      "count": 8
    },
    "output_display": [
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:purple_dye",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta"
    ],
    "output": [
      {
        "id": "minecraft:terracotta",
        "count": 8
      },
      {
        "id": "minecraft:purple_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "purpur_block",
    "input": {
      "item": "minecraft:purpur_block",
      "count": 4
    },
    "output_display": [
      "minecraft:popped_chorus_fruit",
      "minecraft:popped_chorus_fruit",
      None,
      "minecraft:popped_chorus_fruit",
      "minecraft:popped_chorus_fruit",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:popped_chorus_fruit",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "purpur_pillar",
    "input": {
      "item": "minecraft:purpur_pillar",
      "count": 1
    },
    "output_display": [
      "minecraft:purpur_slab",
      None,
      None,
      "minecraft:purpur_slab",
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:purpur_slab",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "purpur_slab",
    "input": {
      "item": "minecraft:purpur_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:purpur_block",
      "minecraft:purpur_block",
      "minecraft:purpur_block",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:purpur_block",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "purpur_stairs",
    "input": {
      "item": "minecraft:purpur_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:purpur_block",
      None,
      None,
      "minecraft:purpur_block",
      "minecraft:purpur_block",
      None,
      "minecraft:purpur_block",
      "minecraft:purpur_block",
      "minecraft:purpur_block"
    ],
    "output": [
      {
        "id": "minecraft:purpur_block",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "quartz_block",
    "input": {
      "item": "minecraft:quartz_block",
      "count": 1
    },
    "output_display": [
      "minecraft:quartz",
      "minecraft:quartz",
      None,
      "minecraft:quartz",
      "minecraft:quartz",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:quartz",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "quartz_bricks",
    "input": {
      "item": "minecraft:quartz_bricks",
      "count": 4
    },
    "output_display": [
      "minecraft:quartz_block",
      "minecraft:quartz_block",
      None,
      "minecraft:quartz_block",
      "minecraft:quartz_block",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:quartz_block",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "quartz_pillar",
    "input": {
      "item": "minecraft:quartz_pillar",
      "count": 2
    },
    "output_display": [
      "minecraft:quartz_block",
      None,
      None,
      "minecraft:quartz_block",
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:quartz_block",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "quartz_slab",
    "input": {
      "item": "minecraft:quartz_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:chiseled_quartz_block",
      "minecraft:chiseled_quartz_block",
      "minecraft:chiseled_quartz_block",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:chiseled_quartz_block",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "quartz_stairs",
    "input": {
      "item": "minecraft:quartz_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:chiseled_quartz_block",
      None,
      None,
      "minecraft:chiseled_quartz_block",
      "minecraft:chiseled_quartz_block",
      None,
      "minecraft:chiseled_quartz_block",
      "minecraft:chiseled_quartz_block",
      "minecraft:chiseled_quartz_block"
    ],
    "output": [
      {
        "id": "minecraft:chiseled_quartz_block",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "rabbit_stew_from_brown_mushroom",
    "input": {
      "item": "minecraft:rabbit_stew",
      "count": 1
    },
    "output_display": [
      "minecraft:baked_potato",
      "minecraft:cooked_rabbit",
      "minecraft:bowl",
      "minecraft:carrot",
      "minecraft:brown_mushroom",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:baked_potato",
        "count": 1
      },
      {
        "id": "minecraft:cooked_rabbit",
        "count": 1
      },
      {
        "id": "minecraft:bowl",
        "count": 1
      },
      {
        "id": "minecraft:carrot",
        "count": 1
      },
      {
        "id": "minecraft:brown_mushroom",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "rabbit_stew_from_red_mushroom",
    "input": {
      "item": "minecraft:rabbit_stew",
      "count": 1
    },
    "output_display": [
      "minecraft:baked_potato",
      "minecraft:cooked_rabbit",
      "minecraft:bowl",
      "minecraft:carrot",
      "minecraft:red_mushroom",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:baked_potato",
        "count": 1
      },
      {
        "id": "minecraft:cooked_rabbit",
        "count": 1
      },
      {
        "id": "minecraft:bowl",
        "count": 1
      },
      {
        "id": "minecraft:carrot",
        "count": 1
      },
      {
        "id": "minecraft:red_mushroom",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "rail",
    "input": {
      "item": "minecraft:rail",
      "count": 16
    },
    "output_display": [
      "minecraft:iron_ingot",
      None,
      "minecraft:iron_ingot",
      "minecraft:iron_ingot",
      "minecraft:stick",
      "minecraft:iron_ingot",
      "minecraft:iron_ingot",
      None,
      "minecraft:iron_ingot"
    ],
    "output": [
      {
        "id": "minecraft:iron_ingot",
        "count": 6
      },
      {
        "id": "minecraft:stick",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "raiser_armor_trim_smithing_template",
    "input": {
      "item": "minecraft:raiser_armor_trim_smithing_template",
      "count": 2
    },
    "output_display": [
      "minecraft:diamond",
      "minecraft:raiser_armor_trim_smithing_template",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:terracotta",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:diamond"
    ],
    "output": [
      {
        "id": "minecraft:diamond",
        "count": 7
      },
      {
        "id": "minecraft:raiser_armor_trim_smithing_template",
        "count": 1
      },
      {
        "id": "minecraft:terracotta",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "raw_copper",
    "input": {
      "item": "minecraft:raw_copper",
      "count": 9
    },
    "output_display": [
      "minecraft:raw_copper_block",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:raw_copper_block",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "raw_copper_block",
    "input": {
      "item": "minecraft:raw_copper_block",
      "count": 1
    },
    "output_display": [
      "minecraft:raw_copper",
      "minecraft:raw_copper",
      "minecraft:raw_copper",
      "minecraft:raw_copper",
      "minecraft:raw_copper",
      "minecraft:raw_copper",
      "minecraft:raw_copper",
      "minecraft:raw_copper",
      "minecraft:raw_copper"
    ],
    "output": [
      {
        "id": "minecraft:raw_copper",
        "count": 9
      }
    ]
  },
  {
    "crafting_recipe_name": "raw_gold",
    "input": {
      "item": "minecraft:raw_gold",
      "count": 9
    },
    "output_display": [
      "minecraft:raw_gold_block",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:raw_gold_block",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "raw_gold_block",
    "input": {
      "item": "minecraft:raw_gold_block",
      "count": 1
    },
    "output_display": [
      "minecraft:raw_gold",
      "minecraft:raw_gold",
      "minecraft:raw_gold",
      "minecraft:raw_gold",
      "minecraft:raw_gold",
      "minecraft:raw_gold",
      "minecraft:raw_gold",
      "minecraft:raw_gold",
      "minecraft:raw_gold"
    ],
    "output": [
      {
        "id": "minecraft:raw_gold",
        "count": 9
      }
    ]
  },
  {
    "crafting_recipe_name": "raw_iron",
    "input": {
      "item": "minecraft:raw_iron",
      "count": 9
    },
    "output_display": [
      "minecraft:raw_iron_block",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:raw_iron_block",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "raw_iron_block",
    "input": {
      "item": "minecraft:raw_iron_block",
      "count": 1
    },
    "output_display": [
      "minecraft:raw_iron",
      "minecraft:raw_iron",
      "minecraft:raw_iron",
      "minecraft:raw_iron",
      "minecraft:raw_iron",
      "minecraft:raw_iron",
      "minecraft:raw_iron",
      "minecraft:raw_iron",
      "minecraft:raw_iron"
    ],
    "output": [
      {
        "id": "minecraft:raw_iron",
        "count": 9
      }
    ]
  },
  {
    "crafting_recipe_name": "recovery_compass",
    "input": {
      "item": "minecraft:recovery_compass",
      "count": 1
    },
    "output_display": [
      "minecraft:echo_shard",
      "minecraft:echo_shard",
      "minecraft:echo_shard",
      "minecraft:echo_shard",
      "minecraft:compass",
      "minecraft:echo_shard",
      "minecraft:echo_shard",
      "minecraft:echo_shard",
      "minecraft:echo_shard"
    ],
    "output": [
      {
        "id": "minecraft:echo_shard",
        "count": 8
      },
      {
        "id": "minecraft:compass",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "redstone",
    "input": {
      "item": "minecraft:redstone",
      "count": 9
    },
    "output_display": [
      "minecraft:redstone_block",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:redstone_block",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "redstone_block",
    "input": {
      "item": "minecraft:redstone_block",
      "count": 1
    },
    "output_display": [
      "minecraft:redstone",
      "minecraft:redstone",
      "minecraft:redstone",
      "minecraft:redstone",
      "minecraft:redstone",
      "minecraft:redstone",
      "minecraft:redstone",
      "minecraft:redstone",
      "minecraft:redstone"
    ],
    "output": [
      {
        "id": "minecraft:redstone",
        "count": 9
      }
    ]
  },
  {
    "crafting_recipe_name": "redstone_lamp",
    "input": {
      "item": "minecraft:redstone_lamp",
      "count": 1
    },
    "output_display": [
      None,
      "minecraft:redstone",
      None,
      "minecraft:redstone",
      "minecraft:glowstone",
      "minecraft:redstone",
      None,
      "minecraft:redstone",
      None
    ],
    "output": [
      {
        "id": "minecraft:redstone",
        "count": 4
      },
      {
        "id": "minecraft:glowstone",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "redstone_torch",
    "input": {
      "item": "minecraft:redstone_torch",
      "count": 1
    },
    "output_display": [
      "minecraft:redstone",
      None,
      None,
      "minecraft:stick",
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:redstone",
        "count": 1
      },
      {
        "id": "minecraft:stick",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "red_banner",
    "input": {
      "item": "minecraft:red_banner",
      "count": 1
    },
    "output_display": [
      "minecraft:red_wool",
      "minecraft:red_wool",
      "minecraft:red_wool",
      "minecraft:red_wool",
      "minecraft:red_wool",
      "minecraft:red_wool",
      None,
      "minecraft:stick",
      None
    ],
    "output": [
      {
        "id": "minecraft:red_wool",
        "count": 6
      },
      {
        "id": "minecraft:stick",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "red_bed",
    "input": {
      "item": "minecraft:red_bed",
      "count": 1
    },
    "output_display": [
      "minecraft:red_wool",
      "minecraft:red_wool",
      "minecraft:red_wool",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:red_wool",
        "count": 3
      },
      {
        "id": "minecraft:oak_planks",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "red_candle",
    "input": {
      "item": "minecraft:red_candle",
      "count": 1
    },
    "output_display": [
      "minecraft:candle",
      "minecraft:red_dye",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:candle",
        "count": 1
      },
      {
        "id": "minecraft:red_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "red_carpet",
    "input": {
      "item": "minecraft:red_carpet",
      "count": 3
    },
    "output_display": [
      "minecraft:red_wool",
      "minecraft:red_wool",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:red_wool",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "red_concrete_powder",
    "input": {
      "item": "minecraft:red_concrete_powder",
      "count": 8
    },
    "output_display": [
      "minecraft:red_dye",
      "minecraft:sand",
      "minecraft:sand",
      "minecraft:sand",
      "minecraft:sand",
      "minecraft:gravel",
      "minecraft:gravel",
      "minecraft:gravel",
      "minecraft:gravel"
    ],
    "output": [
      {
        "id": "minecraft:red_dye",
        "count": 1
      },
      {
        "id": "minecraft:sand",
        "count": 4
      },
      {
        "id": "minecraft:gravel",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "red_dye_from_beetroot",
    "input": {
      "item": "minecraft:red_dye",
      "count": 1
    },
    "output_display": [
      "minecraft:beetroot",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:beetroot",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "red_dye_from_poppy",
    "input": {
      "item": "minecraft:red_dye",
      "count": 1
    },
    "output_display": [
      "minecraft:poppy",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:poppy",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "red_dye_from_rose_bush",
    "input": {
      "item": "minecraft:red_dye",
      "count": 2
    },
    "output_display": [
      "minecraft:rose_bush",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:rose_bush",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "red_dye_from_tulip",
    "input": {
      "item": "minecraft:red_dye",
      "count": 1
    },
    "output_display": [
      "minecraft:red_tulip",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:red_tulip",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "red_nether_bricks",
    "input": {
      "item": "minecraft:red_nether_bricks",
      "count": 1
    },
    "output_display": [
      "minecraft:nether_brick",
      "minecraft:nether_wart",
      None,
      "minecraft:nether_wart",
      "minecraft:nether_brick",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:nether_brick",
        "count": 2
      },
      {
        "id": "minecraft:nether_wart",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "red_nether_brick_slab",
    "input": {
      "item": "minecraft:red_nether_brick_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:red_nether_bricks",
      "minecraft:red_nether_bricks",
      "minecraft:red_nether_bricks",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:red_nether_bricks",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "red_nether_brick_stairs",
    "input": {
      "item": "minecraft:red_nether_brick_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:red_nether_bricks",
      None,
      None,
      "minecraft:red_nether_bricks",
      "minecraft:red_nether_bricks",
      None,
      "minecraft:red_nether_bricks",
      "minecraft:red_nether_bricks",
      "minecraft:red_nether_bricks"
    ],
    "output": [
      {
        "id": "minecraft:red_nether_bricks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "red_nether_brick_wall",
    "input": {
      "item": "minecraft:red_nether_brick_wall",
      "count": 6
    },
    "output_display": [
      "minecraft:red_nether_bricks",
      "minecraft:red_nether_bricks",
      "minecraft:red_nether_bricks",
      "minecraft:red_nether_bricks",
      "minecraft:red_nether_bricks",
      "minecraft:red_nether_bricks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:red_nether_bricks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "red_sandstone",
    "input": {
      "item": "minecraft:red_sandstone",
      "count": 1
    },
    "output_display": [
      "minecraft:red_sand",
      "minecraft:red_sand",
      None,
      "minecraft:red_sand",
      "minecraft:red_sand",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:red_sand",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "red_sandstone_slab",
    "input": {
      "item": "minecraft:red_sandstone_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:red_sandstone",
      "minecraft:red_sandstone",
      "minecraft:red_sandstone",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:red_sandstone",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "red_sandstone_stairs",
    "input": {
      "item": "minecraft:red_sandstone_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:red_sandstone",
      None,
      None,
      "minecraft:red_sandstone",
      "minecraft:red_sandstone",
      None,
      "minecraft:red_sandstone",
      "minecraft:red_sandstone",
      "minecraft:red_sandstone"
    ],
    "output": [
      {
        "id": "minecraft:red_sandstone",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "red_sandstone_wall",
    "input": {
      "item": "minecraft:red_sandstone_wall",
      "count": 6
    },
    "output_display": [
      "minecraft:red_sandstone",
      "minecraft:red_sandstone",
      "minecraft:red_sandstone",
      "minecraft:red_sandstone",
      "minecraft:red_sandstone",
      "minecraft:red_sandstone",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:red_sandstone",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "red_stained_glass",
    "input": {
      "item": "minecraft:red_stained_glass",
      "count": 8
    },
    "output_display": [
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:red_dye",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass"
    ],
    "output": [
      {
        "id": "minecraft:glass",
        "count": 8
      },
      {
        "id": "minecraft:red_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "red_stained_glass_pane",
    "input": {
      "item": "minecraft:red_stained_glass_pane",
      "count": 16
    },
    "output_display": [
      "minecraft:red_stained_glass",
      "minecraft:red_stained_glass",
      "minecraft:red_stained_glass",
      "minecraft:red_stained_glass",
      "minecraft:red_stained_glass",
      "minecraft:red_stained_glass",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:red_stained_glass",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "red_stained_glass_pane_from_glass_pane",
    "input": {
      "item": "minecraft:red_stained_glass_pane",
      "count": 8
    },
    "output_display": [
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:red_dye",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane"
    ],
    "output": [
      {
        "id": "minecraft:glass_pane",
        "count": 8
      },
      {
        "id": "minecraft:red_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "red_terracotta",
    "input": {
      "item": "minecraft:red_terracotta",
      "count": 8
    },
    "output_display": [
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:red_dye",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta"
    ],
    "output": [
      {
        "id": "minecraft:terracotta",
        "count": 8
      },
      {
        "id": "minecraft:red_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "repeater",
    "input": {
      "item": "minecraft:repeater",
      "count": 1
    },
    "output_display": [
      "minecraft:redstone_torch",
      "minecraft:redstone",
      "minecraft:redstone_torch",
      "minecraft:stone",
      "minecraft:stone",
      "minecraft:stone",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:redstone_torch",
        "count": 2
      },
      {
        "id": "minecraft:redstone",
        "count": 1
      },
      {
        "id": "minecraft:stone",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "resin_block",
    "input": {
      "item": "minecraft:resin_block",
      "count": 1
    },
    "output_display": [
      "minecraft:resin_clump",
      "minecraft:resin_clump",
      "minecraft:resin_clump",
      "minecraft:resin_clump",
      "minecraft:resin_clump",
      "minecraft:resin_clump",
      "minecraft:resin_clump",
      "minecraft:resin_clump",
      "minecraft:resin_clump"
    ],
    "output": [
      {
        "id": "minecraft:resin_clump",
        "count": 9
      }
    ]
  },
  {
    "crafting_recipe_name": "resin_bricks",
    "input": {
      "item": "minecraft:resin_bricks",
      "count": 1
    },
    "output_display": [
      "minecraft:resin_brick",
      "minecraft:resin_brick",
      None,
      "minecraft:resin_brick",
      "minecraft:resin_brick",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:resin_brick",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "resin_brick_slab",
    "input": {
      "item": "minecraft:resin_brick_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:resin_bricks",
      "minecraft:resin_bricks",
      "minecraft:resin_bricks",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:resin_bricks",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "resin_brick_stairs",
    "input": {
      "item": "minecraft:resin_brick_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:resin_bricks",
      None,
      None,
      "minecraft:resin_bricks",
      "minecraft:resin_bricks",
      None,
      "minecraft:resin_bricks",
      "minecraft:resin_bricks",
      "minecraft:resin_bricks"
    ],
    "output": [
      {
        "id": "minecraft:resin_bricks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "resin_brick_wall",
    "input": {
      "item": "minecraft:resin_brick_wall",
      "count": 6
    },
    "output_display": [
      "minecraft:resin_bricks",
      "minecraft:resin_bricks",
      "minecraft:resin_bricks",
      "minecraft:resin_bricks",
      "minecraft:resin_bricks",
      "minecraft:resin_bricks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:resin_bricks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "resin_clump",
    "input": {
      "item": "minecraft:resin_clump",
      "count": 9
    },
    "output_display": [
      "minecraft:resin_block",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:resin_block",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "respawn_anchor",
    "input": {
      "item": "minecraft:respawn_anchor",
      "count": 1
    },
    "output_display": [
      "minecraft:crying_obsidian",
      "minecraft:crying_obsidian",
      "minecraft:crying_obsidian",
      "minecraft:glowstone",
      "minecraft:glowstone",
      "minecraft:glowstone",
      "minecraft:crying_obsidian",
      "minecraft:crying_obsidian",
      "minecraft:crying_obsidian"
    ],
    "output": [
      {
        "id": "minecraft:crying_obsidian",
        "count": 6
      },
      {
        "id": "minecraft:glowstone",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "rib_armor_trim_smithing_template",
    "input": {
      "item": "minecraft:rib_armor_trim_smithing_template",
      "count": 2
    },
    "output_display": [
      "minecraft:diamond",
      "minecraft:rib_armor_trim_smithing_template",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:netherrack",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:diamond"
    ],
    "output": [
      {
        "id": "minecraft:diamond",
        "count": 7
      },
      {
        "id": "minecraft:rib_armor_trim_smithing_template",
        "count": 1
      },
      {
        "id": "minecraft:netherrack",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "sandstone",
    "input": {
      "item": "minecraft:sandstone",
      "count": 1
    },
    "output_display": [
      "minecraft:sand",
      "minecraft:sand",
      None,
      "minecraft:sand",
      "minecraft:sand",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:sand",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "sandstone_slab",
    "input": {
      "item": "minecraft:sandstone_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:sandstone",
      "minecraft:sandstone",
      "minecraft:sandstone",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:sandstone",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "sandstone_stairs",
    "input": {
      "item": "minecraft:sandstone_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:sandstone",
      None,
      None,
      "minecraft:sandstone",
      "minecraft:sandstone",
      None,
      "minecraft:sandstone",
      "minecraft:sandstone",
      "minecraft:sandstone"
    ],
    "output": [
      {
        "id": "minecraft:sandstone",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "sandstone_wall",
    "input": {
      "item": "minecraft:sandstone_wall",
      "count": 6
    },
    "output_display": [
      "minecraft:sandstone",
      "minecraft:sandstone",
      "minecraft:sandstone",
      "minecraft:sandstone",
      "minecraft:sandstone",
      "minecraft:sandstone",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:sandstone",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "scaffolding",
    "input": {
      "item": "minecraft:scaffolding",
      "count": 6
    },
    "output_display": [
      "minecraft:bamboo",
      "minecraft:string",
      "minecraft:bamboo",
      "minecraft:bamboo",
      None,
      "minecraft:bamboo",
      "minecraft:bamboo",
      None,
      "minecraft:bamboo"
    ],
    "output": [
      {
        "id": "minecraft:bamboo",
        "count": 6
      },
      {
        "id": "minecraft:string",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "sea_lantern",
    "input": {
      "item": "minecraft:sea_lantern",
      "count": 1
    },
    "output_display": [
      "minecraft:prismarine_shard",
      "minecraft:prismarine_crystals",
      "minecraft:prismarine_shard",
      "minecraft:prismarine_crystals",
      "minecraft:prismarine_crystals",
      "minecraft:prismarine_crystals",
      "minecraft:prismarine_shard",
      "minecraft:prismarine_crystals",
      "minecraft:prismarine_shard"
    ],
    "output": [
      {
        "id": "minecraft:prismarine_shard",
        "count": 4
      },
      {
        "id": "minecraft:prismarine_crystals",
        "count": 5
      }
    ]
  },
  {
    "crafting_recipe_name": "sentry_armor_trim_smithing_template",
    "input": {
      "item": "minecraft:sentry_armor_trim_smithing_template",
      "count": 2
    },
    "output_display": [
      "minecraft:diamond",
      "minecraft:sentry_armor_trim_smithing_template",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:cobblestone",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:diamond"
    ],
    "output": [
      {
        "id": "minecraft:diamond",
        "count": 7
      },
      {
        "id": "minecraft:sentry_armor_trim_smithing_template",
        "count": 1
      },
      {
        "id": "minecraft:cobblestone",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "shaper_armor_trim_smithing_template",
    "input": {
      "item": "minecraft:shaper_armor_trim_smithing_template",
      "count": 2
    },
    "output_display": [
      "minecraft:diamond",
      "minecraft:shaper_armor_trim_smithing_template",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:terracotta",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:diamond"
    ],
    "output": [
      {
        "id": "minecraft:diamond",
        "count": 7
      },
      {
        "id": "minecraft:shaper_armor_trim_smithing_template",
        "count": 1
      },
      {
        "id": "minecraft:terracotta",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "shears",
    "input": {
      "item": "minecraft:shears",
      "count": 1
    },
    "output_display": [
      None,
      "minecraft:iron_ingot",
      None,
      "minecraft:iron_ingot",
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:iron_ingot",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "shield",
    "input": {
      "item": "minecraft:shield",
      "count": 1
    },
    "output_display": [
      "minecraft:oak_planks",
      "minecraft:iron_ingot",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      None,
      "minecraft:oak_planks",
      None
    ],
    "output": [
      {
        "id": "minecraft:oak_planks",
        "count": 6
      },
      {
        "id": "minecraft:iron_ingot",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "shulker_box",
    "input": {
      "item": "minecraft:shulker_box",
      "count": 1
    },
    "output_display": [
      "minecraft:shulker_shell",
      None,
      None,
      "minecraft:chest",
      None,
      None,
      "minecraft:shulker_shell",
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:shulker_shell",
        "count": 2
      },
      {
        "id": "minecraft:chest",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "silence_armor_trim_smithing_template",
    "input": {
      "item": "minecraft:silence_armor_trim_smithing_template",
      "count": 2
    },
    "output_display": [
      "minecraft:diamond",
      "minecraft:silence_armor_trim_smithing_template",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:cobbled_deepslate",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:diamond"
    ],
    "output": [
      {
        "id": "minecraft:diamond",
        "count": 7
      },
      {
        "id": "minecraft:silence_armor_trim_smithing_template",
        "count": 1
      },
      {
        "id": "minecraft:cobbled_deepslate",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "skull_banner_pattern",
    "input": {
      "item": "minecraft:skull_banner_pattern",
      "count": 1
    },
    "output_display": [
      "minecraft:paper",
      "minecraft:wither_skeleton_skull",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:paper",
        "count": 1
      },
      {
        "id": "minecraft:wither_skeleton_skull",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "slime_ball",
    "input": {
      "item": "minecraft:slime_ball",
      "count": 9
    },
    "output_display": [
      "minecraft:slime_block",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:slime_block",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "slime_block",
    "input": {
      "item": "minecraft:slime_block",
      "count": 1
    },
    "output_display": [
      "minecraft:slime_ball",
      "minecraft:slime_ball",
      "minecraft:slime_ball",
      "minecraft:slime_ball",
      "minecraft:slime_ball",
      "minecraft:slime_ball",
      "minecraft:slime_ball",
      "minecraft:slime_ball",
      "minecraft:slime_ball"
    ],
    "output": [
      {
        "id": "minecraft:slime_ball",
        "count": 9
      }
    ]
  },
  {
    "crafting_recipe_name": "smithing_table",
    "input": {
      "item": "minecraft:smithing_table",
      "count": 1
    },
    "output_display": [
      "minecraft:iron_ingot",
      "minecraft:iron_ingot",
      None,
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      None,
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      None
    ],
    "output": [
      {
        "id": "minecraft:iron_ingot",
        "count": 2
      },
      {
        "id": "minecraft:oak_planks",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "smoker",
    "input": {
      "item": "minecraft:smoker",
      "count": 1
    },
    "output_display": [
      None,
      "minecraft:oak_log",
      None,
      "minecraft:oak_log",
      "minecraft:furnace",
      "minecraft:oak_log",
      None,
      "minecraft:oak_log",
      None
    ],
    "output": [
      {
        "id": "minecraft:oak_log",
        "count": 4
      },
      {
        "id": "minecraft:furnace",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "smooth_quartz_slab",
    "input": {
      "item": "minecraft:smooth_quartz_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:smooth_quartz",
      "minecraft:smooth_quartz",
      "minecraft:smooth_quartz",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:smooth_quartz",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "smooth_quartz_stairs",
    "input": {
      "item": "minecraft:smooth_quartz_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:smooth_quartz",
      None,
      None,
      "minecraft:smooth_quartz",
      "minecraft:smooth_quartz",
      None,
      "minecraft:smooth_quartz",
      "minecraft:smooth_quartz",
      "minecraft:smooth_quartz"
    ],
    "output": [
      {
        "id": "minecraft:smooth_quartz",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "smooth_red_sandstone_slab",
    "input": {
      "item": "minecraft:smooth_red_sandstone_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:smooth_red_sandstone",
      "minecraft:smooth_red_sandstone",
      "minecraft:smooth_red_sandstone",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:smooth_red_sandstone",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "smooth_red_sandstone_stairs",
    "input": {
      "item": "minecraft:smooth_red_sandstone_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:smooth_red_sandstone",
      None,
      None,
      "minecraft:smooth_red_sandstone",
      "minecraft:smooth_red_sandstone",
      None,
      "minecraft:smooth_red_sandstone",
      "minecraft:smooth_red_sandstone",
      "minecraft:smooth_red_sandstone"
    ],
    "output": [
      {
        "id": "minecraft:smooth_red_sandstone",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "smooth_sandstone_slab",
    "input": {
      "item": "minecraft:smooth_sandstone_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:smooth_sandstone",
      "minecraft:smooth_sandstone",
      "minecraft:smooth_sandstone",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:smooth_sandstone",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "smooth_sandstone_stairs",
    "input": {
      "item": "minecraft:smooth_sandstone_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:smooth_sandstone",
      None,
      None,
      "minecraft:smooth_sandstone",
      "minecraft:smooth_sandstone",
      None,
      "minecraft:smooth_sandstone",
      "minecraft:smooth_sandstone",
      "minecraft:smooth_sandstone"
    ],
    "output": [
      {
        "id": "minecraft:smooth_sandstone",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "smooth_stone_slab",
    "input": {
      "item": "minecraft:smooth_stone_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:smooth_stone",
      "minecraft:smooth_stone",
      "minecraft:smooth_stone",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:smooth_stone",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "snout_armor_trim_smithing_template",
    "input": {
      "item": "minecraft:snout_armor_trim_smithing_template",
      "count": 2
    },
    "output_display": [
      "minecraft:diamond",
      "minecraft:snout_armor_trim_smithing_template",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:blackstone",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:diamond"
    ],
    "output": [
      {
        "id": "minecraft:diamond",
        "count": 7
      },
      {
        "id": "minecraft:snout_armor_trim_smithing_template",
        "count": 1
      },
      {
        "id": "minecraft:blackstone",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "snow",
    "input": {
      "item": "minecraft:snow",
      "count": 6
    },
    "output_display": [
      "minecraft:snow_block",
      "minecraft:snow_block",
      "minecraft:snow_block",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:snow_block",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "snow_block",
    "input": {
      "item": "minecraft:snow_block",
      "count": 1
    },
    "output_display": [
      "minecraft:snowball",
      "minecraft:snowball",
      None,
      "minecraft:snowball",
      "minecraft:snowball",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:snowball",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "soul_campfire",
    "input": {
      "item": "minecraft:soul_campfire",
      "count": 1
    },
    "output_display": [
      None,
      "minecraft:stick",
      None,
      "minecraft:stick",
      "#minecraft:soul_fire_base_blocks",
      "minecraft:stick",
      "minecraft:oak_log",
      "minecraft:oak_log",
      "minecraft:oak_log"
    ],
    "output": [
      {
        "id": "minecraft:stick",
        "count": 3
      },
      {
        "id": "#minecraft:soul_fire_base_blocks",
        "count": 1
      },
      {
        "id": "minecraft:oak_log",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "soul_lantern",
    "input": {
      "item": "minecraft:soul_lantern",
      "count": 1
    },
    "output_display": [
      "minecraft:iron_nugget",
      "minecraft:iron_nugget",
      "minecraft:iron_nugget",
      "minecraft:iron_nugget",
      "minecraft:soul_torch",
      "minecraft:iron_nugget",
      "minecraft:iron_nugget",
      "minecraft:iron_nugget",
      "minecraft:iron_nugget"
    ],
    "output": [
      {
        "id": "minecraft:iron_nugget",
        "count": 8
      },
      {
        "id": "minecraft:soul_torch",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "soul_torch",
    "input": {
      "item": "minecraft:soul_torch",
      "count": 4
    },
    "output_display": [
      "minecraft:coal",
      None,
      None,
      "minecraft:stick",
      None,
      None,
      "#minecraft:soul_fire_base_blocks",
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:coal",
        "count": 1
      },
      {
        "id": "minecraft:stick",
        "count": 1
      },
      {
        "id": "#minecraft:soul_fire_base_blocks",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "spectral_arrow",
    "input": {
      "item": "minecraft:spectral_arrow",
      "count": 2
    },
    "output_display": [
      None,
      "minecraft:glowstone_dust",
      None,
      "minecraft:glowstone_dust",
      "minecraft:arrow",
      "minecraft:glowstone_dust",
      None,
      "minecraft:glowstone_dust",
      None
    ],
    "output": [
      {
        "id": "minecraft:glowstone_dust",
        "count": 4
      },
      {
        "id": "minecraft:arrow",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "spire_armor_trim_smithing_template",
    "input": {
      "item": "minecraft:spire_armor_trim_smithing_template",
      "count": 2
    },
    "output_display": [
      "minecraft:diamond",
      "minecraft:spire_armor_trim_smithing_template",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:purpur_block",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:diamond"
    ],
    "output": [
      {
        "id": "minecraft:diamond",
        "count": 7
      },
      {
        "id": "minecraft:spire_armor_trim_smithing_template",
        "count": 1
      },
      {
        "id": "minecraft:purpur_block",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "spruce_boat",
    "input": {
      "item": "minecraft:spruce_boat",
      "count": 1
    },
    "output_display": [
      "minecraft:spruce_planks",
      None,
      "minecraft:spruce_planks",
      "minecraft:spruce_planks",
      "minecraft:spruce_planks",
      "minecraft:spruce_planks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:spruce_planks",
        "count": 5
      }
    ]
  },
  {
    "crafting_recipe_name": "spruce_button",
    "input": {
      "item": "minecraft:spruce_button",
      "count": 1
    },
    "output_display": [
      "minecraft:spruce_planks",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:spruce_planks",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "spruce_chest_boat",
    "input": {
      "item": "minecraft:spruce_chest_boat",
      "count": 1
    },
    "output_display": [
      "minecraft:chest",
      "minecraft:spruce_boat",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:chest",
        "count": 1
      },
      {
        "id": "minecraft:spruce_boat",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "spruce_door",
    "input": {
      "item": "minecraft:spruce_door",
      "count": 3
    },
    "output_display": [
      "minecraft:spruce_planks",
      "minecraft:spruce_planks",
      None,
      "minecraft:spruce_planks",
      "minecraft:spruce_planks",
      None,
      "minecraft:spruce_planks",
      "minecraft:spruce_planks",
      None
    ],
    "output": [
      {
        "id": "minecraft:spruce_planks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "spruce_fence",
    "input": {
      "item": "minecraft:spruce_fence",
      "count": 3
    },
    "output_display": [
      "minecraft:spruce_planks",
      "minecraft:stick",
      "minecraft:spruce_planks",
      "minecraft:spruce_planks",
      "minecraft:stick",
      "minecraft:spruce_planks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:spruce_planks",
        "count": 4
      },
      {
        "id": "minecraft:stick",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "spruce_fence_gate",
    "input": {
      "item": "minecraft:spruce_fence_gate",
      "count": 1
    },
    "output_display": [
      "minecraft:stick",
      "minecraft:spruce_planks",
      "minecraft:stick",
      "minecraft:stick",
      "minecraft:spruce_planks",
      "minecraft:stick",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:stick",
        "count": 4
      },
      {
        "id": "minecraft:spruce_planks",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "spruce_hanging_sign",
    "input": {
      "item": "minecraft:spruce_hanging_sign",
      "count": 6
    },
    "output_display": [
      "minecraft:chain",
      None,
      "minecraft:chain",
      "minecraft:stripped_spruce_log",
      "minecraft:stripped_spruce_log",
      "minecraft:stripped_spruce_log",
      "minecraft:stripped_spruce_log",
      "minecraft:stripped_spruce_log",
      "minecraft:stripped_spruce_log"
    ],
    "output": [
      {
        "id": "minecraft:chain",
        "count": 2
      },
      {
        "id": "minecraft:stripped_spruce_log",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "spruce_planks",
    "input": {
      "item": "minecraft:spruce_planks",
      "count": 4
    },
    "output_display": [
      "minecraft:spruce_log",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:spruce_log",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "spruce_pressure_plate",
    "input": {
      "item": "minecraft:spruce_pressure_plate",
      "count": 1
    },
    "output_display": [
      "minecraft:spruce_planks",
      "minecraft:spruce_planks",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:spruce_planks",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "spruce_sign",
    "input": {
      "item": "minecraft:spruce_sign",
      "count": 3
    },
    "output_display": [
      "minecraft:spruce_planks",
      "minecraft:spruce_planks",
      "minecraft:spruce_planks",
      "minecraft:spruce_planks",
      "minecraft:spruce_planks",
      "minecraft:spruce_planks",
      None,
      "minecraft:stick",
      None
    ],
    "output": [
      {
        "id": "minecraft:spruce_planks",
        "count": 6
      },
      {
        "id": "minecraft:stick",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "spruce_slab",
    "input": {
      "item": "minecraft:spruce_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:spruce_planks",
      "minecraft:spruce_planks",
      "minecraft:spruce_planks",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:spruce_planks",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "spruce_stairs",
    "input": {
      "item": "minecraft:spruce_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:spruce_planks",
      None,
      None,
      "minecraft:spruce_planks",
      "minecraft:spruce_planks",
      None,
      "minecraft:spruce_planks",
      "minecraft:spruce_planks",
      "minecraft:spruce_planks"
    ],
    "output": [
      {
        "id": "minecraft:spruce_planks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "spruce_trapdoor",
    "input": {
      "item": "minecraft:spruce_trapdoor",
      "count": 2
    },
    "output_display": [
      "minecraft:spruce_planks",
      "minecraft:spruce_planks",
      "minecraft:spruce_planks",
      "minecraft:spruce_planks",
      "minecraft:spruce_planks",
      "minecraft:spruce_planks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:spruce_planks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "spruce_wood",
    "input": {
      "item": "minecraft:spruce_wood",
      "count": 3
    },
    "output_display": [
      "minecraft:spruce_log",
      "minecraft:spruce_log",
      None,
      "minecraft:spruce_log",
      "minecraft:spruce_log",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:spruce_log",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "spyglass",
    "input": {
      "item": "minecraft:spyglass",
      "count": 1
    },
    "output_display": [
      None,
      "minecraft:amethyst_shard",
      None,
      None,
      "minecraft:copper_ingot",
      None,
      None,
      "minecraft:copper_ingot",
      None
    ],
    "output": [
      {
        "id": "minecraft:amethyst_shard",
        "count": 1
      },
      {
        "id": "minecraft:copper_ingot",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "stick",
    "input": {
      "item": "minecraft:stick",
      "count": 4
    },
    "output_display": [
      "minecraft:oak_planks",
      None,
      None,
      "minecraft:oak_planks",
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:oak_planks",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "sticky_piston",
    "input": {
      "item": "minecraft:sticky_piston",
      "count": 1
    },
    "output_display": [
      "minecraft:slime_ball",
      None,
      None,
      "minecraft:piston",
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:slime_ball",
        "count": 1
      },
      {
        "id": "minecraft:piston",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "stick_from_bamboo_item",
    "input": {
      "item": "minecraft:stick",
      "count": 1
    },
    "output_display": [
      "minecraft:bamboo",
      None,
      None,
      "minecraft:bamboo",
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:bamboo",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "stonecutter",
    "input": {
      "item": "minecraft:stonecutter",
      "count": 1
    },
    "output_display": [
      None,
      "minecraft:iron_ingot",
      None,
      "minecraft:stone",
      "minecraft:stone",
      "minecraft:stone",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:iron_ingot",
        "count": 1
      },
      {
        "id": "minecraft:stone",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "stone_axe",
    "input": {
      "item": "minecraft:stone_axe",
      "count": 1
    },
    "output_display": [
      "minecraft:cobblestone",
      "minecraft:cobblestone",
      None,
      "minecraft:cobblestone",
      "minecraft:stick",
      None,
      None,
      "minecraft:stick",
      None
    ],
    "output": [
      {
        "id": "minecraft:cobblestone",
        "count": 3
      },
      {
        "id": "minecraft:stick",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "stone_bricks",
    "input": {
      "item": "minecraft:stone_bricks",
      "count": 4
    },
    "output_display": [
      "minecraft:stone",
      "minecraft:stone",
      None,
      "minecraft:stone",
      "minecraft:stone",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:stone",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "stone_brick_slab",
    "input": {
      "item": "minecraft:stone_brick_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:stone_bricks",
      "minecraft:stone_bricks",
      "minecraft:stone_bricks",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:stone_bricks",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "stone_brick_stairs",
    "input": {
      "item": "minecraft:stone_brick_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:stone_bricks",
      None,
      None,
      "minecraft:stone_bricks",
      "minecraft:stone_bricks",
      None,
      "minecraft:stone_bricks",
      "minecraft:stone_bricks",
      "minecraft:stone_bricks"
    ],
    "output": [
      {
        "id": "minecraft:stone_bricks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "stone_brick_wall",
    "input": {
      "item": "minecraft:stone_brick_wall",
      "count": 6
    },
    "output_display": [
      "minecraft:stone_bricks",
      "minecraft:stone_bricks",
      "minecraft:stone_bricks",
      "minecraft:stone_bricks",
      "minecraft:stone_bricks",
      "minecraft:stone_bricks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:stone_bricks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "stone_button",
    "input": {
      "item": "minecraft:stone_button",
      "count": 1
    },
    "output_display": [
      "minecraft:stone",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:stone",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "stone_hoe",
    "input": {
      "item": "minecraft:stone_hoe",
      "count": 1
    },
    "output_display": [
      "minecraft:cobblestone",
      "minecraft:cobblestone",
      None,
      None,
      "minecraft:stick",
      None,
      None,
      "minecraft:stick",
      None
    ],
    "output": [
      {
        "id": "minecraft:cobblestone",
        "count": 2
      },
      {
        "id": "minecraft:stick",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "stone_pickaxe",
    "input": {
      "item": "minecraft:stone_pickaxe",
      "count": 1
    },
    "output_display": [
      "minecraft:cobblestone",
      "minecraft:cobblestone",
      "minecraft:cobblestone",
      None,
      "minecraft:stick",
      None,
      None,
      "minecraft:stick",
      None
    ],
    "output": [
      {
        "id": "minecraft:cobblestone",
        "count": 3
      },
      {
        "id": "minecraft:stick",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "stone_pressure_plate",
    "input": {
      "item": "minecraft:stone_pressure_plate",
      "count": 1
    },
    "output_display": [
      "minecraft:stone",
      "minecraft:stone",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:stone",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "stone_shovel",
    "input": {
      "item": "minecraft:stone_shovel",
      "count": 1
    },
    "output_display": [
      "minecraft:cobblestone",
      None,
      None,
      "minecraft:stick",
      None,
      None,
      "minecraft:stick",
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:cobblestone",
        "count": 1
      },
      {
        "id": "minecraft:stick",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "stone_slab",
    "input": {
      "item": "minecraft:stone_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:stone",
      "minecraft:stone",
      "minecraft:stone",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:stone",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "stone_stairs",
    "input": {
      "item": "minecraft:stone_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:stone",
      None,
      None,
      "minecraft:stone",
      "minecraft:stone",
      None,
      "minecraft:stone",
      "minecraft:stone",
      "minecraft:stone"
    ],
    "output": [
      {
        "id": "minecraft:stone",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "stone_sword",
    "input": {
      "item": "minecraft:stone_sword",
      "count": 1
    },
    "output_display": [
      "minecraft:cobblestone",
      None,
      None,
      "minecraft:cobblestone",
      None,
      None,
      "minecraft:stick",
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:cobblestone",
        "count": 2
      },
      {
        "id": "minecraft:stick",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "stripped_acacia_wood",
    "input": {
      "item": "minecraft:stripped_acacia_wood",
      "count": 3
    },
    "output_display": [
      "minecraft:stripped_acacia_log",
      "minecraft:stripped_acacia_log",
      None,
      "minecraft:stripped_acacia_log",
      "minecraft:stripped_acacia_log",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:stripped_acacia_log",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "stripped_birch_wood",
    "input": {
      "item": "minecraft:stripped_birch_wood",
      "count": 3
    },
    "output_display": [
      "minecraft:stripped_birch_log",
      "minecraft:stripped_birch_log",
      None,
      "minecraft:stripped_birch_log",
      "minecraft:stripped_birch_log",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:stripped_birch_log",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "stripped_cherry_wood",
    "input": {
      "item": "minecraft:stripped_cherry_wood",
      "count": 3
    },
    "output_display": [
      "minecraft:stripped_cherry_log",
      "minecraft:stripped_cherry_log",
      None,
      "minecraft:stripped_cherry_log",
      "minecraft:stripped_cherry_log",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:stripped_cherry_log",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "stripped_crimson_hyphae",
    "input": {
      "item": "minecraft:stripped_crimson_hyphae",
      "count": 3
    },
    "output_display": [
      "minecraft:stripped_crimson_stem",
      "minecraft:stripped_crimson_stem",
      None,
      "minecraft:stripped_crimson_stem",
      "minecraft:stripped_crimson_stem",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:stripped_crimson_stem",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "stripped_dark_oak_wood",
    "input": {
      "item": "minecraft:stripped_dark_oak_wood",
      "count": 3
    },
    "output_display": [
      "minecraft:stripped_dark_oak_log",
      "minecraft:stripped_dark_oak_log",
      None,
      "minecraft:stripped_dark_oak_log",
      "minecraft:stripped_dark_oak_log",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:stripped_dark_oak_log",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "stripped_jungle_wood",
    "input": {
      "item": "minecraft:stripped_jungle_wood",
      "count": 3
    },
    "output_display": [
      "minecraft:stripped_jungle_log",
      "minecraft:stripped_jungle_log",
      None,
      "minecraft:stripped_jungle_log",
      "minecraft:stripped_jungle_log",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:stripped_jungle_log",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "stripped_mangrove_wood",
    "input": {
      "item": "minecraft:stripped_mangrove_wood",
      "count": 3
    },
    "output_display": [
      "minecraft:stripped_mangrove_log",
      "minecraft:stripped_mangrove_log",
      None,
      "minecraft:stripped_mangrove_log",
      "minecraft:stripped_mangrove_log",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:stripped_mangrove_log",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "stripped_oak_wood",
    "input": {
      "item": "minecraft:stripped_oak_wood",
      "count": 3
    },
    "output_display": [
      "minecraft:stripped_oak_log",
      "minecraft:stripped_oak_log",
      None,
      "minecraft:stripped_oak_log",
      "minecraft:stripped_oak_log",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:stripped_oak_log",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "stripped_pale_oak_wood",
    "input": {
      "item": "minecraft:stripped_pale_oak_wood",
      "count": 3
    },
    "output_display": [
      "minecraft:stripped_pale_oak_log",
      "minecraft:stripped_pale_oak_log",
      None,
      "minecraft:stripped_pale_oak_log",
      "minecraft:stripped_pale_oak_log",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:stripped_pale_oak_log",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "stripped_spruce_wood",
    "input": {
      "item": "minecraft:stripped_spruce_wood",
      "count": 3
    },
    "output_display": [
      "minecraft:stripped_spruce_log",
      "minecraft:stripped_spruce_log",
      None,
      "minecraft:stripped_spruce_log",
      "minecraft:stripped_spruce_log",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:stripped_spruce_log",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "stripped_warped_hyphae",
    "input": {
      "item": "minecraft:stripped_warped_hyphae",
      "count": 3
    },
    "output_display": [
      "minecraft:stripped_warped_stem",
      "minecraft:stripped_warped_stem",
      None,
      "minecraft:stripped_warped_stem",
      "minecraft:stripped_warped_stem",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:stripped_warped_stem",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "sugar_from_honey_bottle",
    "input": {
      "item": "minecraft:sugar",
      "count": 3
    },
    "output_display": [
      "minecraft:honey_bottle",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:honey_bottle",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "sugar_from_sugar_cane",
    "input": {
      "item": "minecraft:sugar",
      "count": 1
    },
    "output_display": [
      "minecraft:sugar_cane",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:sugar_cane",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "suspicious_stew_from_allium",
    "input": {
      "item": "minecraft:suspicious_stew",
      "count": 1
    },
    "output_display": [
      "minecraft:bowl",
      "minecraft:brown_mushroom",
      "minecraft:red_mushroom",
      "minecraft:allium",
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:bowl",
        "count": 1
      },
      {
        "id": "minecraft:brown_mushroom",
        "count": 1
      },
      {
        "id": "minecraft:red_mushroom",
        "count": 1
      },
      {
        "id": "minecraft:allium",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "suspicious_stew_from_azure_bluet",
    "input": {
      "item": "minecraft:suspicious_stew",
      "count": 1
    },
    "output_display": [
      "minecraft:bowl",
      "minecraft:brown_mushroom",
      "minecraft:red_mushroom",
      "minecraft:azure_bluet",
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:bowl",
        "count": 1
      },
      {
        "id": "minecraft:brown_mushroom",
        "count": 1
      },
      {
        "id": "minecraft:red_mushroom",
        "count": 1
      },
      {
        "id": "minecraft:azure_bluet",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "suspicious_stew_from_blue_orchid",
    "input": {
      "item": "minecraft:suspicious_stew",
      "count": 1
    },
    "output_display": [
      "minecraft:bowl",
      "minecraft:brown_mushroom",
      "minecraft:red_mushroom",
      "minecraft:blue_orchid",
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:bowl",
        "count": 1
      },
      {
        "id": "minecraft:brown_mushroom",
        "count": 1
      },
      {
        "id": "minecraft:red_mushroom",
        "count": 1
      },
      {
        "id": "minecraft:blue_orchid",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "suspicious_stew_from_closed_eyeblossom",
    "input": {
      "item": "minecraft:suspicious_stew",
      "count": 1
    },
    "output_display": [
      "minecraft:bowl",
      "minecraft:brown_mushroom",
      "minecraft:red_mushroom",
      "minecraft:closed_eyeblossom",
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:bowl",
        "count": 1
      },
      {
        "id": "minecraft:brown_mushroom",
        "count": 1
      },
      {
        "id": "minecraft:red_mushroom",
        "count": 1
      },
      {
        "id": "minecraft:closed_eyeblossom",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "suspicious_stew_from_cornflower",
    "input": {
      "item": "minecraft:suspicious_stew",
      "count": 1
    },
    "output_display": [
      "minecraft:bowl",
      "minecraft:brown_mushroom",
      "minecraft:red_mushroom",
      "minecraft:cornflower",
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:bowl",
        "count": 1
      },
      {
        "id": "minecraft:brown_mushroom",
        "count": 1
      },
      {
        "id": "minecraft:red_mushroom",
        "count": 1
      },
      {
        "id": "minecraft:cornflower",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "suspicious_stew_from_dandelion",
    "input": {
      "item": "minecraft:suspicious_stew",
      "count": 1
    },
    "output_display": [
      "minecraft:bowl",
      "minecraft:brown_mushroom",
      "minecraft:red_mushroom",
      "minecraft:dandelion",
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:bowl",
        "count": 1
      },
      {
        "id": "minecraft:brown_mushroom",
        "count": 1
      },
      {
        "id": "minecraft:red_mushroom",
        "count": 1
      },
      {
        "id": "minecraft:dandelion",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "suspicious_stew_from_lily_of_the_valley",
    "input": {
      "item": "minecraft:suspicious_stew",
      "count": 1
    },
    "output_display": [
      "minecraft:bowl",
      "minecraft:brown_mushroom",
      "minecraft:red_mushroom",
      "minecraft:lily_of_the_valley",
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:bowl",
        "count": 1
      },
      {
        "id": "minecraft:brown_mushroom",
        "count": 1
      },
      {
        "id": "minecraft:red_mushroom",
        "count": 1
      },
      {
        "id": "minecraft:lily_of_the_valley",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "suspicious_stew_from_open_eyeblossom",
    "input": {
      "item": "minecraft:suspicious_stew",
      "count": 1
    },
    "output_display": [
      "minecraft:bowl",
      "minecraft:brown_mushroom",
      "minecraft:red_mushroom",
      "minecraft:open_eyeblossom",
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:bowl",
        "count": 1
      },
      {
        "id": "minecraft:brown_mushroom",
        "count": 1
      },
      {
        "id": "minecraft:red_mushroom",
        "count": 1
      },
      {
        "id": "minecraft:open_eyeblossom",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "suspicious_stew_from_orange_tulip",
    "input": {
      "item": "minecraft:suspicious_stew",
      "count": 1
    },
    "output_display": [
      "minecraft:bowl",
      "minecraft:brown_mushroom",
      "minecraft:red_mushroom",
      "minecraft:orange_tulip",
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:bowl",
        "count": 1
      },
      {
        "id": "minecraft:brown_mushroom",
        "count": 1
      },
      {
        "id": "minecraft:red_mushroom",
        "count": 1
      },
      {
        "id": "minecraft:orange_tulip",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "suspicious_stew_from_oxeye_daisy",
    "input": {
      "item": "minecraft:suspicious_stew",
      "count": 1
    },
    "output_display": [
      "minecraft:bowl",
      "minecraft:brown_mushroom",
      "minecraft:red_mushroom",
      "minecraft:oxeye_daisy",
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:bowl",
        "count": 1
      },
      {
        "id": "minecraft:brown_mushroom",
        "count": 1
      },
      {
        "id": "minecraft:red_mushroom",
        "count": 1
      },
      {
        "id": "minecraft:oxeye_daisy",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "suspicious_stew_from_pink_tulip",
    "input": {
      "item": "minecraft:suspicious_stew",
      "count": 1
    },
    "output_display": [
      "minecraft:bowl",
      "minecraft:brown_mushroom",
      "minecraft:red_mushroom",
      "minecraft:pink_tulip",
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:bowl",
        "count": 1
      },
      {
        "id": "minecraft:brown_mushroom",
        "count": 1
      },
      {
        "id": "minecraft:red_mushroom",
        "count": 1
      },
      {
        "id": "minecraft:pink_tulip",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "suspicious_stew_from_poppy",
    "input": {
      "item": "minecraft:suspicious_stew",
      "count": 1
    },
    "output_display": [
      "minecraft:bowl",
      "minecraft:brown_mushroom",
      "minecraft:red_mushroom",
      "minecraft:poppy",
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:bowl",
        "count": 1
      },
      {
        "id": "minecraft:brown_mushroom",
        "count": 1
      },
      {
        "id": "minecraft:red_mushroom",
        "count": 1
      },
      {
        "id": "minecraft:poppy",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "suspicious_stew_from_red_tulip",
    "input": {
      "item": "minecraft:suspicious_stew",
      "count": 1
    },
    "output_display": [
      "minecraft:bowl",
      "minecraft:brown_mushroom",
      "minecraft:red_mushroom",
      "minecraft:red_tulip",
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:bowl",
        "count": 1
      },
      {
        "id": "minecraft:brown_mushroom",
        "count": 1
      },
      {
        "id": "minecraft:red_mushroom",
        "count": 1
      },
      {
        "id": "minecraft:red_tulip",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "suspicious_stew_from_torchflower",
    "input": {
      "item": "minecraft:suspicious_stew",
      "count": 1
    },
    "output_display": [
      "minecraft:bowl",
      "minecraft:brown_mushroom",
      "minecraft:red_mushroom",
      "minecraft:torchflower",
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:bowl",
        "count": 1
      },
      {
        "id": "minecraft:brown_mushroom",
        "count": 1
      },
      {
        "id": "minecraft:red_mushroom",
        "count": 1
      },
      {
        "id": "minecraft:torchflower",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "suspicious_stew_from_white_tulip",
    "input": {
      "item": "minecraft:suspicious_stew",
      "count": 1
    },
    "output_display": [
      "minecraft:bowl",
      "minecraft:brown_mushroom",
      "minecraft:red_mushroom",
      "minecraft:white_tulip",
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:bowl",
        "count": 1
      },
      {
        "id": "minecraft:brown_mushroom",
        "count": 1
      },
      {
        "id": "minecraft:red_mushroom",
        "count": 1
      },
      {
        "id": "minecraft:white_tulip",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "suspicious_stew_from_wither_rose",
    "input": {
      "item": "minecraft:suspicious_stew",
      "count": 1
    },
    "output_display": [
      "minecraft:bowl",
      "minecraft:brown_mushroom",
      "minecraft:red_mushroom",
      "minecraft:wither_rose",
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:bowl",
        "count": 1
      },
      {
        "id": "minecraft:brown_mushroom",
        "count": 1
      },
      {
        "id": "minecraft:red_mushroom",
        "count": 1
      },
      {
        "id": "minecraft:wither_rose",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "target",
    "input": {
      "item": "minecraft:target",
      "count": 1
    },
    "output_display": [
      None,
      "minecraft:redstone",
      None,
      "minecraft:redstone",
      "minecraft:hay_block",
      "minecraft:redstone",
      None,
      "minecraft:redstone",
      None
    ],
    "output": [
      {
        "id": "minecraft:redstone",
        "count": 4
      },
      {
        "id": "minecraft:hay_block",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "tide_armor_trim_smithing_template",
    "input": {
      "item": "minecraft:tide_armor_trim_smithing_template",
      "count": 2
    },
    "output_display": [
      "minecraft:diamond",
      "minecraft:tide_armor_trim_smithing_template",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:prismarine",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:diamond"
    ],
    "output": [
      {
        "id": "minecraft:diamond",
        "count": 7
      },
      {
        "id": "minecraft:tide_armor_trim_smithing_template",
        "count": 1
      },
      {
        "id": "minecraft:prismarine",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "tinted_glass",
    "input": {
      "item": "minecraft:tinted_glass",
      "count": 2
    },
    "output_display": [
      None,
      "minecraft:amethyst_shard",
      None,
      "minecraft:amethyst_shard",
      "minecraft:glass",
      "minecraft:amethyst_shard",
      None,
      "minecraft:amethyst_shard",
      None
    ],
    "output": [
      {
        "id": "minecraft:amethyst_shard",
        "count": 4
      },
      {
        "id": "minecraft:glass",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "tnt",
    "input": {
      "item": "minecraft:tnt",
      "count": 1
    },
    "output_display": [
      "minecraft:gunpowder",
      "minecraft:sand",
      "minecraft:gunpowder",
      "minecraft:sand",
      "minecraft:gunpowder",
      "minecraft:sand",
      "minecraft:gunpowder",
      "minecraft:sand",
      "minecraft:gunpowder"
    ],
    "output": [
      {
        "id": "minecraft:gunpowder",
        "count": 5
      },
      {
        "id": "minecraft:sand",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "tnt_minecart",
    "input": {
      "item": "minecraft:tnt_minecart",
      "count": 1
    },
    "output_display": [
      "minecraft:tnt",
      "minecraft:minecart",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:tnt",
        "count": 1
      },
      {
        "id": "minecraft:minecart",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "torch",
    "input": {
      "item": "minecraft:torch",
      "count": 4
    },
    "output_display": [
      "minecraft:coal",
      None,
      None,
      "minecraft:stick",
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:coal",
        "count": 1
      },
      {
        "id": "minecraft:stick",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "trapped_chest",
    "input": {
      "item": "minecraft:trapped_chest",
      "count": 1
    },
    "output_display": [
      "minecraft:chest",
      "minecraft:tripwire_hook",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:chest",
        "count": 1
      },
      {
        "id": "minecraft:tripwire_hook",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "tripwire_hook",
    "input": {
      "item": "minecraft:tripwire_hook",
      "count": 2
    },
    "output_display": [
      "minecraft:iron_ingot",
      None,
      None,
      "minecraft:stick",
      None,
      None,
      "minecraft:oak_planks",
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:iron_ingot",
        "count": 1
      },
      {
        "id": "minecraft:stick",
        "count": 1
      },
      {
        "id": "minecraft:oak_planks",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "tuff_bricks",
    "input": {
      "item": "minecraft:tuff_bricks",
      "count": 4
    },
    "output_display": [
      "minecraft:polished_tuff",
      "minecraft:polished_tuff",
      None,
      "minecraft:polished_tuff",
      "minecraft:polished_tuff",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:polished_tuff",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "tuff_brick_slab",
    "input": {
      "item": "minecraft:tuff_brick_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:tuff_bricks",
      "minecraft:tuff_bricks",
      "minecraft:tuff_bricks",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:tuff_bricks",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "tuff_brick_stairs",
    "input": {
      "item": "minecraft:tuff_brick_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:tuff_bricks",
      None,
      None,
      "minecraft:tuff_bricks",
      "minecraft:tuff_bricks",
      None,
      "minecraft:tuff_bricks",
      "minecraft:tuff_bricks",
      "minecraft:tuff_bricks"
    ],
    "output": [
      {
        "id": "minecraft:tuff_bricks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "tuff_brick_wall",
    "input": {
      "item": "minecraft:tuff_brick_wall",
      "count": 6
    },
    "output_display": [
      "minecraft:tuff_bricks",
      "minecraft:tuff_bricks",
      "minecraft:tuff_bricks",
      "minecraft:tuff_bricks",
      "minecraft:tuff_bricks",
      "minecraft:tuff_bricks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:tuff_bricks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "tuff_slab",
    "input": {
      "item": "minecraft:tuff_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:tuff",
      "minecraft:tuff",
      "minecraft:tuff",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:tuff",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "tuff_stairs",
    "input": {
      "item": "minecraft:tuff_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:tuff",
      None,
      None,
      "minecraft:tuff",
      "minecraft:tuff",
      None,
      "minecraft:tuff",
      "minecraft:tuff",
      "minecraft:tuff"
    ],
    "output": [
      {
        "id": "minecraft:tuff",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "tuff_wall",
    "input": {
      "item": "minecraft:tuff_wall",
      "count": 6
    },
    "output_display": [
      "minecraft:tuff",
      "minecraft:tuff",
      "minecraft:tuff",
      "minecraft:tuff",
      "minecraft:tuff",
      "minecraft:tuff",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:tuff",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "turtle_helmet",
    "input": {
      "item": "minecraft:turtle_helmet",
      "count": 1
    },
    "output_display": [
      "minecraft:turtle_scute",
      "minecraft:turtle_scute",
      "minecraft:turtle_scute",
      "minecraft:turtle_scute",
      None,
      "minecraft:turtle_scute",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:turtle_scute",
        "count": 5
      }
    ]
  },
  {
    "crafting_recipe_name": "vex_armor_trim_smithing_template",
    "input": {
      "item": "minecraft:vex_armor_trim_smithing_template",
      "count": 2
    },
    "output_display": [
      "minecraft:diamond",
      "minecraft:vex_armor_trim_smithing_template",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:cobblestone",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:diamond"
    ],
    "output": [
      {
        "id": "minecraft:diamond",
        "count": 7
      },
      {
        "id": "minecraft:vex_armor_trim_smithing_template",
        "count": 1
      },
      {
        "id": "minecraft:cobblestone",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "ward_armor_trim_smithing_template",
    "input": {
      "item": "minecraft:ward_armor_trim_smithing_template",
      "count": 2
    },
    "output_display": [
      "minecraft:diamond",
      "minecraft:ward_armor_trim_smithing_template",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:cobbled_deepslate",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:diamond"
    ],
    "output": [
      {
        "id": "minecraft:diamond",
        "count": 7
      },
      {
        "id": "minecraft:ward_armor_trim_smithing_template",
        "count": 1
      },
      {
        "id": "minecraft:cobbled_deepslate",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "warped_button",
    "input": {
      "item": "minecraft:warped_button",
      "count": 1
    },
    "output_display": [
      "minecraft:warped_planks",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:warped_planks",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "warped_door",
    "input": {
      "item": "minecraft:warped_door",
      "count": 3
    },
    "output_display": [
      "minecraft:warped_planks",
      "minecraft:warped_planks",
      None,
      "minecraft:warped_planks",
      "minecraft:warped_planks",
      None,
      "minecraft:warped_planks",
      "minecraft:warped_planks",
      None
    ],
    "output": [
      {
        "id": "minecraft:warped_planks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "warped_fence",
    "input": {
      "item": "minecraft:warped_fence",
      "count": 3
    },
    "output_display": [
      "minecraft:warped_planks",
      "minecraft:stick",
      "minecraft:warped_planks",
      "minecraft:warped_planks",
      "minecraft:stick",
      "minecraft:warped_planks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:warped_planks",
        "count": 4
      },
      {
        "id": "minecraft:stick",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "warped_fence_gate",
    "input": {
      "item": "minecraft:warped_fence_gate",
      "count": 1
    },
    "output_display": [
      "minecraft:stick",
      "minecraft:warped_planks",
      "minecraft:stick",
      "minecraft:stick",
      "minecraft:warped_planks",
      "minecraft:stick",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:stick",
        "count": 4
      },
      {
        "id": "minecraft:warped_planks",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "warped_fungus_on_a_stick",
    "input": {
      "item": "minecraft:warped_fungus_on_a_stick",
      "count": 1
    },
    "output_display": [
      "minecraft:fishing_rod",
      None,
      None,
      None,
      "minecraft:warped_fungus",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:fishing_rod",
        "count": 1
      },
      {
        "id": "minecraft:warped_fungus",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "warped_hanging_sign",
    "input": {
      "item": "minecraft:warped_hanging_sign",
      "count": 6
    },
    "output_display": [
      "minecraft:chain",
      None,
      "minecraft:chain",
      "minecraft:stripped_warped_stem",
      "minecraft:stripped_warped_stem",
      "minecraft:stripped_warped_stem",
      "minecraft:stripped_warped_stem",
      "minecraft:stripped_warped_stem",
      "minecraft:stripped_warped_stem"
    ],
    "output": [
      {
        "id": "minecraft:chain",
        "count": 2
      },
      {
        "id": "minecraft:stripped_warped_stem",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "warped_hyphae",
    "input": {
      "item": "minecraft:warped_hyphae",
      "count": 3
    },
    "output_display": [
      "minecraft:warped_stem",
      "minecraft:warped_stem",
      None,
      "minecraft:warped_stem",
      "minecraft:warped_stem",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:warped_stem",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "warped_planks",
    "input": {
      "item": "minecraft:warped_planks",
      "count": 4
    },
    "output_display": [
      "minecraft:warped_stem",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:warped_stem",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "warped_pressure_plate",
    "input": {
      "item": "minecraft:warped_pressure_plate",
      "count": 1
    },
    "output_display": [
      "minecraft:warped_planks",
      "minecraft:warped_planks",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:warped_planks",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "warped_sign",
    "input": {
      "item": "minecraft:warped_sign",
      "count": 3
    },
    "output_display": [
      "minecraft:warped_planks",
      "minecraft:warped_planks",
      "minecraft:warped_planks",
      "minecraft:warped_planks",
      "minecraft:warped_planks",
      "minecraft:warped_planks",
      None,
      "minecraft:stick",
      None
    ],
    "output": [
      {
        "id": "minecraft:warped_planks",
        "count": 6
      },
      {
        "id": "minecraft:stick",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "warped_slab",
    "input": {
      "item": "minecraft:warped_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:warped_planks",
      "minecraft:warped_planks",
      "minecraft:warped_planks",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:warped_planks",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "warped_stairs",
    "input": {
      "item": "minecraft:warped_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:warped_planks",
      None,
      None,
      "minecraft:warped_planks",
      "minecraft:warped_planks",
      None,
      "minecraft:warped_planks",
      "minecraft:warped_planks",
      "minecraft:warped_planks"
    ],
    "output": [
      {
        "id": "minecraft:warped_planks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "warped_trapdoor",
    "input": {
      "item": "minecraft:warped_trapdoor",
      "count": 2
    },
    "output_display": [
      "minecraft:warped_planks",
      "minecraft:warped_planks",
      "minecraft:warped_planks",
      "minecraft:warped_planks",
      "minecraft:warped_planks",
      "minecraft:warped_planks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:warped_planks",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_chiseled_copper",
    "input": {
      "item": "minecraft:waxed_chiseled_copper",
      "count": 1
    },
    "output_display": [
      "minecraft:waxed_cut_copper_slab",
      None,
      None,
      "minecraft:waxed_cut_copper_slab",
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:waxed_cut_copper_slab",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_chiseled_copper_from_honeycomb",
    "input": {
      "item": "minecraft:waxed_chiseled_copper",
      "count": 1
    },
    "output_display": [
      "minecraft:chiseled_copper",
      "minecraft:honeycomb",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:chiseled_copper",
        "count": 1
      },
      {
        "id": "minecraft:honeycomb",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_copper_block_from_honeycomb",
    "input": {
      "item": "minecraft:waxed_copper_block",
      "count": 1
    },
    "output_display": [
      "minecraft:copper_block",
      "minecraft:honeycomb",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:copper_block",
        "count": 1
      },
      {
        "id": "minecraft:honeycomb",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_copper_bulb",
    "input": {
      "item": "minecraft:waxed_copper_bulb",
      "count": 4
    },
    "output_display": [
      None,
      "minecraft:waxed_copper_block",
      None,
      "minecraft:waxed_copper_block",
      "minecraft:blaze_rod",
      "minecraft:waxed_copper_block",
      None,
      "minecraft:redstone",
      None
    ],
    "output": [
      {
        "id": "minecraft:waxed_copper_block",
        "count": 3
      },
      {
        "id": "minecraft:blaze_rod",
        "count": 1
      },
      {
        "id": "minecraft:redstone",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_copper_bulb_from_honeycomb",
    "input": {
      "item": "minecraft:waxed_copper_bulb",
      "count": 1
    },
    "output_display": [
      "minecraft:copper_bulb",
      "minecraft:honeycomb",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:copper_bulb",
        "count": 1
      },
      {
        "id": "minecraft:honeycomb",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_copper_door_from_honeycomb",
    "input": {
      "item": "minecraft:waxed_copper_door",
      "count": 1
    },
    "output_display": [
      "minecraft:copper_door",
      "minecraft:honeycomb",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:copper_door",
        "count": 1
      },
      {
        "id": "minecraft:honeycomb",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_copper_grate",
    "input": {
      "item": "minecraft:waxed_copper_grate",
      "count": 4
    },
    "output_display": [
      None,
      "minecraft:waxed_copper_block",
      None,
      "minecraft:waxed_copper_block",
      None,
      "minecraft:waxed_copper_block",
      None,
      "minecraft:waxed_copper_block",
      None
    ],
    "output": [
      {
        "id": "minecraft:waxed_copper_block",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_copper_grate_from_honeycomb",
    "input": {
      "item": "minecraft:waxed_copper_grate",
      "count": 1
    },
    "output_display": [
      "minecraft:copper_grate",
      "minecraft:honeycomb",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:copper_grate",
        "count": 1
      },
      {
        "id": "minecraft:honeycomb",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_copper_trapdoor_from_honeycomb",
    "input": {
      "item": "minecraft:waxed_copper_trapdoor",
      "count": 1
    },
    "output_display": [
      "minecraft:copper_trapdoor",
      "minecraft:honeycomb",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:copper_trapdoor",
        "count": 1
      },
      {
        "id": "minecraft:honeycomb",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_cut_copper",
    "input": {
      "item": "minecraft:waxed_cut_copper",
      "count": 4
    },
    "output_display": [
      "minecraft:waxed_copper_block",
      "minecraft:waxed_copper_block",
      None,
      "minecraft:waxed_copper_block",
      "minecraft:waxed_copper_block",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:waxed_copper_block",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_cut_copper_from_honeycomb",
    "input": {
      "item": "minecraft:waxed_cut_copper",
      "count": 1
    },
    "output_display": [
      "minecraft:cut_copper",
      "minecraft:honeycomb",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:cut_copper",
        "count": 1
      },
      {
        "id": "minecraft:honeycomb",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_cut_copper_slab",
    "input": {
      "item": "minecraft:waxed_cut_copper_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:waxed_cut_copper",
      "minecraft:waxed_cut_copper",
      "minecraft:waxed_cut_copper",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:waxed_cut_copper",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_cut_copper_slab_from_honeycomb",
    "input": {
      "item": "minecraft:waxed_cut_copper_slab",
      "count": 1
    },
    "output_display": [
      "minecraft:cut_copper_slab",
      "minecraft:honeycomb",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:cut_copper_slab",
        "count": 1
      },
      {
        "id": "minecraft:honeycomb",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_cut_copper_stairs",
    "input": {
      "item": "minecraft:waxed_cut_copper_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:waxed_cut_copper",
      None,
      None,
      "minecraft:waxed_cut_copper",
      "minecraft:waxed_cut_copper",
      None,
      "minecraft:waxed_cut_copper",
      "minecraft:waxed_cut_copper",
      "minecraft:waxed_cut_copper"
    ],
    "output": [
      {
        "id": "minecraft:waxed_cut_copper",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_cut_copper_stairs_from_honeycomb",
    "input": {
      "item": "minecraft:waxed_cut_copper_stairs",
      "count": 1
    },
    "output_display": [
      "minecraft:cut_copper_stairs",
      "minecraft:honeycomb",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:cut_copper_stairs",
        "count": 1
      },
      {
        "id": "minecraft:honeycomb",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_exposed_chiseled_copper",
    "input": {
      "item": "minecraft:waxed_exposed_chiseled_copper",
      "count": 1
    },
    "output_display": [
      "minecraft:waxed_exposed_cut_copper_slab",
      None,
      None,
      "minecraft:waxed_exposed_cut_copper_slab",
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:waxed_exposed_cut_copper_slab",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_exposed_chiseled_copper_from_honeycomb",
    "input": {
      "item": "minecraft:waxed_exposed_chiseled_copper",
      "count": 1
    },
    "output_display": [
      "minecraft:exposed_chiseled_copper",
      "minecraft:honeycomb",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:exposed_chiseled_copper",
        "count": 1
      },
      {
        "id": "minecraft:honeycomb",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_exposed_copper_bulb",
    "input": {
      "item": "minecraft:waxed_exposed_copper_bulb",
      "count": 4
    },
    "output_display": [
      None,
      "minecraft:waxed_exposed_copper",
      None,
      "minecraft:waxed_exposed_copper",
      "minecraft:blaze_rod",
      "minecraft:waxed_exposed_copper",
      None,
      "minecraft:redstone",
      None
    ],
    "output": [
      {
        "id": "minecraft:waxed_exposed_copper",
        "count": 3
      },
      {
        "id": "minecraft:blaze_rod",
        "count": 1
      },
      {
        "id": "minecraft:redstone",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_exposed_copper_bulb_from_honeycomb",
    "input": {
      "item": "minecraft:waxed_exposed_copper_bulb",
      "count": 1
    },
    "output_display": [
      "minecraft:exposed_copper_bulb",
      "minecraft:honeycomb",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:exposed_copper_bulb",
        "count": 1
      },
      {
        "id": "minecraft:honeycomb",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_exposed_copper_door_from_honeycomb",
    "input": {
      "item": "minecraft:waxed_exposed_copper_door",
      "count": 1
    },
    "output_display": [
      "minecraft:exposed_copper_door",
      "minecraft:honeycomb",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:exposed_copper_door",
        "count": 1
      },
      {
        "id": "minecraft:honeycomb",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_exposed_copper_from_honeycomb",
    "input": {
      "item": "minecraft:waxed_exposed_copper",
      "count": 1
    },
    "output_display": [
      "minecraft:exposed_copper",
      "minecraft:honeycomb",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:exposed_copper",
        "count": 1
      },
      {
        "id": "minecraft:honeycomb",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_exposed_copper_grate",
    "input": {
      "item": "minecraft:waxed_exposed_copper_grate",
      "count": 4
    },
    "output_display": [
      None,
      "minecraft:waxed_exposed_copper",
      None,
      "minecraft:waxed_exposed_copper",
      None,
      "minecraft:waxed_exposed_copper",
      None,
      "minecraft:waxed_exposed_copper",
      None
    ],
    "output": [
      {
        "id": "minecraft:waxed_exposed_copper",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_exposed_copper_grate_from_honeycomb",
    "input": {
      "item": "minecraft:waxed_exposed_copper_grate",
      "count": 1
    },
    "output_display": [
      "minecraft:exposed_copper_grate",
      "minecraft:honeycomb",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:exposed_copper_grate",
        "count": 1
      },
      {
        "id": "minecraft:honeycomb",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_exposed_copper_trapdoor_from_honeycomb",
    "input": {
      "item": "minecraft:waxed_exposed_copper_trapdoor",
      "count": 1
    },
    "output_display": [
      "minecraft:exposed_copper_trapdoor",
      "minecraft:honeycomb",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:exposed_copper_trapdoor",
        "count": 1
      },
      {
        "id": "minecraft:honeycomb",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_exposed_cut_copper",
    "input": {
      "item": "minecraft:waxed_exposed_cut_copper",
      "count": 4
    },
    "output_display": [
      "minecraft:waxed_exposed_copper",
      "minecraft:waxed_exposed_copper",
      None,
      "minecraft:waxed_exposed_copper",
      "minecraft:waxed_exposed_copper",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:waxed_exposed_copper",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_exposed_cut_copper_from_honeycomb",
    "input": {
      "item": "minecraft:waxed_exposed_cut_copper",
      "count": 1
    },
    "output_display": [
      "minecraft:exposed_cut_copper",
      "minecraft:honeycomb",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:exposed_cut_copper",
        "count": 1
      },
      {
        "id": "minecraft:honeycomb",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_exposed_cut_copper_slab",
    "input": {
      "item": "minecraft:waxed_exposed_cut_copper_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:waxed_exposed_cut_copper",
      "minecraft:waxed_exposed_cut_copper",
      "minecraft:waxed_exposed_cut_copper",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:waxed_exposed_cut_copper",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_exposed_cut_copper_slab_from_honeycomb",
    "input": {
      "item": "minecraft:waxed_exposed_cut_copper_slab",
      "count": 1
    },
    "output_display": [
      "minecraft:exposed_cut_copper_slab",
      "minecraft:honeycomb",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:exposed_cut_copper_slab",
        "count": 1
      },
      {
        "id": "minecraft:honeycomb",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_exposed_cut_copper_stairs",
    "input": {
      "item": "minecraft:waxed_exposed_cut_copper_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:waxed_exposed_cut_copper",
      None,
      None,
      "minecraft:waxed_exposed_cut_copper",
      "minecraft:waxed_exposed_cut_copper",
      None,
      "minecraft:waxed_exposed_cut_copper",
      "minecraft:waxed_exposed_cut_copper",
      "minecraft:waxed_exposed_cut_copper"
    ],
    "output": [
      {
        "id": "minecraft:waxed_exposed_cut_copper",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_exposed_cut_copper_stairs_from_honeycomb",
    "input": {
      "item": "minecraft:waxed_exposed_cut_copper_stairs",
      "count": 1
    },
    "output_display": [
      "minecraft:exposed_cut_copper_stairs",
      "minecraft:honeycomb",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:exposed_cut_copper_stairs",
        "count": 1
      },
      {
        "id": "minecraft:honeycomb",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_oxidized_chiseled_copper",
    "input": {
      "item": "minecraft:waxed_oxidized_chiseled_copper",
      "count": 1
    },
    "output_display": [
      "minecraft:waxed_oxidized_cut_copper_slab",
      None,
      None,
      "minecraft:waxed_oxidized_cut_copper_slab",
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:waxed_oxidized_cut_copper_slab",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_oxidized_chiseled_copper_from_honeycomb",
    "input": {
      "item": "minecraft:waxed_oxidized_chiseled_copper",
      "count": 1
    },
    "output_display": [
      "minecraft:oxidized_chiseled_copper",
      "minecraft:honeycomb",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:oxidized_chiseled_copper",
        "count": 1
      },
      {
        "id": "minecraft:honeycomb",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_oxidized_copper_bulb",
    "input": {
      "item": "minecraft:waxed_oxidized_copper_bulb",
      "count": 4
    },
    "output_display": [
      None,
      "minecraft:waxed_oxidized_copper",
      None,
      "minecraft:waxed_oxidized_copper",
      "minecraft:blaze_rod",
      "minecraft:waxed_oxidized_copper",
      None,
      "minecraft:redstone",
      None
    ],
    "output": [
      {
        "id": "minecraft:waxed_oxidized_copper",
        "count": 3
      },
      {
        "id": "minecraft:blaze_rod",
        "count": 1
      },
      {
        "id": "minecraft:redstone",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_oxidized_copper_bulb_from_honeycomb",
    "input": {
      "item": "minecraft:waxed_oxidized_copper_bulb",
      "count": 1
    },
    "output_display": [
      "minecraft:oxidized_copper_bulb",
      "minecraft:honeycomb",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:oxidized_copper_bulb",
        "count": 1
      },
      {
        "id": "minecraft:honeycomb",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_oxidized_copper_door_from_honeycomb",
    "input": {
      "item": "minecraft:waxed_oxidized_copper_door",
      "count": 1
    },
    "output_display": [
      "minecraft:oxidized_copper_door",
      "minecraft:honeycomb",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:oxidized_copper_door",
        "count": 1
      },
      {
        "id": "minecraft:honeycomb",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_oxidized_copper_from_honeycomb",
    "input": {
      "item": "minecraft:waxed_oxidized_copper",
      "count": 1
    },
    "output_display": [
      "minecraft:oxidized_copper",
      "minecraft:honeycomb",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:oxidized_copper",
        "count": 1
      },
      {
        "id": "minecraft:honeycomb",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_oxidized_copper_grate",
    "input": {
      "item": "minecraft:waxed_oxidized_copper_grate",
      "count": 4
    },
    "output_display": [
      None,
      "minecraft:waxed_oxidized_copper",
      None,
      "minecraft:waxed_oxidized_copper",
      None,
      "minecraft:waxed_oxidized_copper",
      None,
      "minecraft:waxed_oxidized_copper",
      None
    ],
    "output": [
      {
        "id": "minecraft:waxed_oxidized_copper",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_oxidized_copper_grate_from_honeycomb",
    "input": {
      "item": "minecraft:waxed_oxidized_copper_grate",
      "count": 1
    },
    "output_display": [
      "minecraft:oxidized_copper_grate",
      "minecraft:honeycomb",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:oxidized_copper_grate",
        "count": 1
      },
      {
        "id": "minecraft:honeycomb",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_oxidized_copper_trapdoor_from_honeycomb",
    "input": {
      "item": "minecraft:waxed_oxidized_copper_trapdoor",
      "count": 1
    },
    "output_display": [
      "minecraft:oxidized_copper_trapdoor",
      "minecraft:honeycomb",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:oxidized_copper_trapdoor",
        "count": 1
      },
      {
        "id": "minecraft:honeycomb",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_oxidized_cut_copper",
    "input": {
      "item": "minecraft:waxed_oxidized_cut_copper",
      "count": 4
    },
    "output_display": [
      "minecraft:waxed_oxidized_copper",
      "minecraft:waxed_oxidized_copper",
      None,
      "minecraft:waxed_oxidized_copper",
      "minecraft:waxed_oxidized_copper",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:waxed_oxidized_copper",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_oxidized_cut_copper_from_honeycomb",
    "input": {
      "item": "minecraft:waxed_oxidized_cut_copper",
      "count": 1
    },
    "output_display": [
      "minecraft:oxidized_cut_copper",
      "minecraft:honeycomb",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:oxidized_cut_copper",
        "count": 1
      },
      {
        "id": "minecraft:honeycomb",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_oxidized_cut_copper_slab",
    "input": {
      "item": "minecraft:waxed_oxidized_cut_copper_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:waxed_oxidized_cut_copper",
      "minecraft:waxed_oxidized_cut_copper",
      "minecraft:waxed_oxidized_cut_copper",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:waxed_oxidized_cut_copper",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_oxidized_cut_copper_slab_from_honeycomb",
    "input": {
      "item": "minecraft:waxed_oxidized_cut_copper_slab",
      "count": 1
    },
    "output_display": [
      "minecraft:oxidized_cut_copper_slab",
      "minecraft:honeycomb",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:oxidized_cut_copper_slab",
        "count": 1
      },
      {
        "id": "minecraft:honeycomb",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_oxidized_cut_copper_stairs",
    "input": {
      "item": "minecraft:waxed_oxidized_cut_copper_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:waxed_oxidized_cut_copper",
      None,
      None,
      "minecraft:waxed_oxidized_cut_copper",
      "minecraft:waxed_oxidized_cut_copper",
      None,
      "minecraft:waxed_oxidized_cut_copper",
      "minecraft:waxed_oxidized_cut_copper",
      "minecraft:waxed_oxidized_cut_copper"
    ],
    "output": [
      {
        "id": "minecraft:waxed_oxidized_cut_copper",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_oxidized_cut_copper_stairs_from_honeycomb",
    "input": {
      "item": "minecraft:waxed_oxidized_cut_copper_stairs",
      "count": 1
    },
    "output_display": [
      "minecraft:oxidized_cut_copper_stairs",
      "minecraft:honeycomb",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:oxidized_cut_copper_stairs",
        "count": 1
      },
      {
        "id": "minecraft:honeycomb",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_weathered_chiseled_copper",
    "input": {
      "item": "minecraft:waxed_weathered_chiseled_copper",
      "count": 1
    },
    "output_display": [
      "minecraft:waxed_weathered_cut_copper_slab",
      None,
      None,
      "minecraft:waxed_weathered_cut_copper_slab",
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:waxed_weathered_cut_copper_slab",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_weathered_chiseled_copper_from_honeycomb",
    "input": {
      "item": "minecraft:waxed_weathered_chiseled_copper",
      "count": 1
    },
    "output_display": [
      "minecraft:weathered_chiseled_copper",
      "minecraft:honeycomb",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:weathered_chiseled_copper",
        "count": 1
      },
      {
        "id": "minecraft:honeycomb",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_weathered_copper_bulb",
    "input": {
      "item": "minecraft:waxed_weathered_copper_bulb",
      "count": 4
    },
    "output_display": [
      None,
      "minecraft:waxed_weathered_copper",
      None,
      "minecraft:waxed_weathered_copper",
      "minecraft:blaze_rod",
      "minecraft:waxed_weathered_copper",
      None,
      "minecraft:redstone",
      None
    ],
    "output": [
      {
        "id": "minecraft:waxed_weathered_copper",
        "count": 3
      },
      {
        "id": "minecraft:blaze_rod",
        "count": 1
      },
      {
        "id": "minecraft:redstone",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_weathered_copper_bulb_from_honeycomb",
    "input": {
      "item": "minecraft:waxed_weathered_copper_bulb",
      "count": 1
    },
    "output_display": [
      "minecraft:weathered_copper_bulb",
      "minecraft:honeycomb",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:weathered_copper_bulb",
        "count": 1
      },
      {
        "id": "minecraft:honeycomb",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_weathered_copper_door_from_honeycomb",
    "input": {
      "item": "minecraft:waxed_weathered_copper_door",
      "count": 1
    },
    "output_display": [
      "minecraft:weathered_copper_door",
      "minecraft:honeycomb",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:weathered_copper_door",
        "count": 1
      },
      {
        "id": "minecraft:honeycomb",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_weathered_copper_from_honeycomb",
    "input": {
      "item": "minecraft:waxed_weathered_copper",
      "count": 1
    },
    "output_display": [
      "minecraft:weathered_copper",
      "minecraft:honeycomb",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:weathered_copper",
        "count": 1
      },
      {
        "id": "minecraft:honeycomb",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_weathered_copper_grate",
    "input": {
      "item": "minecraft:waxed_weathered_copper_grate",
      "count": 4
    },
    "output_display": [
      None,
      "minecraft:waxed_weathered_copper",
      None,
      "minecraft:waxed_weathered_copper",
      None,
      "minecraft:waxed_weathered_copper",
      None,
      "minecraft:waxed_weathered_copper",
      None
    ],
    "output": [
      {
        "id": "minecraft:waxed_weathered_copper",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_weathered_copper_grate_from_honeycomb",
    "input": {
      "item": "minecraft:waxed_weathered_copper_grate",
      "count": 1
    },
    "output_display": [
      "minecraft:weathered_copper_grate",
      "minecraft:honeycomb",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:weathered_copper_grate",
        "count": 1
      },
      {
        "id": "minecraft:honeycomb",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_weathered_copper_trapdoor_from_honeycomb",
    "input": {
      "item": "minecraft:waxed_weathered_copper_trapdoor",
      "count": 1
    },
    "output_display": [
      "minecraft:weathered_copper_trapdoor",
      "minecraft:honeycomb",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:weathered_copper_trapdoor",
        "count": 1
      },
      {
        "id": "minecraft:honeycomb",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_weathered_cut_copper",
    "input": {
      "item": "minecraft:waxed_weathered_cut_copper",
      "count": 4
    },
    "output_display": [
      "minecraft:waxed_weathered_copper",
      "minecraft:waxed_weathered_copper",
      None,
      "minecraft:waxed_weathered_copper",
      "minecraft:waxed_weathered_copper",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:waxed_weathered_copper",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_weathered_cut_copper_from_honeycomb",
    "input": {
      "item": "minecraft:waxed_weathered_cut_copper",
      "count": 1
    },
    "output_display": [
      "minecraft:weathered_cut_copper",
      "minecraft:honeycomb",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:weathered_cut_copper",
        "count": 1
      },
      {
        "id": "minecraft:honeycomb",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_weathered_cut_copper_slab",
    "input": {
      "item": "minecraft:waxed_weathered_cut_copper_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:waxed_weathered_cut_copper",
      "minecraft:waxed_weathered_cut_copper",
      "minecraft:waxed_weathered_cut_copper",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:waxed_weathered_cut_copper",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_weathered_cut_copper_slab_from_honeycomb",
    "input": {
      "item": "minecraft:waxed_weathered_cut_copper_slab",
      "count": 1
    },
    "output_display": [
      "minecraft:weathered_cut_copper_slab",
      "minecraft:honeycomb",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:weathered_cut_copper_slab",
        "count": 1
      },
      {
        "id": "minecraft:honeycomb",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_weathered_cut_copper_stairs",
    "input": {
      "item": "minecraft:waxed_weathered_cut_copper_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:waxed_weathered_cut_copper",
      None,
      None,
      "minecraft:waxed_weathered_cut_copper",
      "minecraft:waxed_weathered_cut_copper",
      None,
      "minecraft:waxed_weathered_cut_copper",
      "minecraft:waxed_weathered_cut_copper",
      "minecraft:waxed_weathered_cut_copper"
    ],
    "output": [
      {
        "id": "minecraft:waxed_weathered_cut_copper",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "waxed_weathered_cut_copper_stairs_from_honeycomb",
    "input": {
      "item": "minecraft:waxed_weathered_cut_copper_stairs",
      "count": 1
    },
    "output_display": [
      "minecraft:weathered_cut_copper_stairs",
      "minecraft:honeycomb",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:weathered_cut_copper_stairs",
        "count": 1
      },
      {
        "id": "minecraft:honeycomb",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "wayfinder_armor_trim_smithing_template",
    "input": {
      "item": "minecraft:wayfinder_armor_trim_smithing_template",
      "count": 2
    },
    "output_display": [
      "minecraft:diamond",
      "minecraft:wayfinder_armor_trim_smithing_template",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:terracotta",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:diamond"
    ],
    "output": [
      {
        "id": "minecraft:diamond",
        "count": 7
      },
      {
        "id": "minecraft:wayfinder_armor_trim_smithing_template",
        "count": 1
      },
      {
        "id": "minecraft:terracotta",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "weathered_chiseled_copper",
    "input": {
      "item": "minecraft:weathered_chiseled_copper",
      "count": 1
    },
    "output_display": [
      "minecraft:weathered_cut_copper_slab",
      None,
      None,
      "minecraft:weathered_cut_copper_slab",
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:weathered_cut_copper_slab",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "weathered_copper_bulb",
    "input": {
      "item": "minecraft:weathered_copper_bulb",
      "count": 4
    },
    "output_display": [
      None,
      "minecraft:weathered_copper",
      None,
      "minecraft:weathered_copper",
      "minecraft:blaze_rod",
      "minecraft:weathered_copper",
      None,
      "minecraft:redstone",
      None
    ],
    "output": [
      {
        "id": "minecraft:weathered_copper",
        "count": 3
      },
      {
        "id": "minecraft:blaze_rod",
        "count": 1
      },
      {
        "id": "minecraft:redstone",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "weathered_copper_grate",
    "input": {
      "item": "minecraft:weathered_copper_grate",
      "count": 4
    },
    "output_display": [
      None,
      "minecraft:weathered_copper",
      None,
      "minecraft:weathered_copper",
      None,
      "minecraft:weathered_copper",
      None,
      "minecraft:weathered_copper",
      None
    ],
    "output": [
      {
        "id": "minecraft:weathered_copper",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "weathered_cut_copper",
    "input": {
      "item": "minecraft:weathered_cut_copper",
      "count": 4
    },
    "output_display": [
      "minecraft:weathered_copper",
      "minecraft:weathered_copper",
      None,
      "minecraft:weathered_copper",
      "minecraft:weathered_copper",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:weathered_copper",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "weathered_cut_copper_slab",
    "input": {
      "item": "minecraft:weathered_cut_copper_slab",
      "count": 6
    },
    "output_display": [
      "minecraft:weathered_cut_copper",
      "minecraft:weathered_cut_copper",
      "minecraft:weathered_cut_copper",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:weathered_cut_copper",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "weathered_cut_copper_stairs",
    "input": {
      "item": "minecraft:weathered_cut_copper_stairs",
      "count": 4
    },
    "output_display": [
      "minecraft:weathered_cut_copper",
      None,
      None,
      "minecraft:weathered_cut_copper",
      "minecraft:weathered_cut_copper",
      None,
      "minecraft:weathered_cut_copper",
      "minecraft:weathered_cut_copper",
      "minecraft:weathered_cut_copper"
    ],
    "output": [
      {
        "id": "minecraft:weathered_cut_copper",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "wheat",
    "input": {
      "item": "minecraft:wheat",
      "count": 9
    },
    "output_display": [
      "minecraft:hay_block",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:hay_block",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "white_banner",
    "input": {
      "item": "minecraft:white_banner",
      "count": 1
    },
    "output_display": [
      "minecraft:white_wool",
      "minecraft:white_wool",
      "minecraft:white_wool",
      "minecraft:white_wool",
      "minecraft:white_wool",
      "minecraft:white_wool",
      None,
      "minecraft:stick",
      None
    ],
    "output": [
      {
        "id": "minecraft:white_wool",
        "count": 6
      },
      {
        "id": "minecraft:stick",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "white_bed",
    "input": {
      "item": "minecraft:white_bed",
      "count": 1
    },
    "output_display": [
      "minecraft:white_wool",
      "minecraft:white_wool",
      "minecraft:white_wool",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:white_wool",
        "count": 3
      },
      {
        "id": "minecraft:oak_planks",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "white_candle",
    "input": {
      "item": "minecraft:white_candle",
      "count": 1
    },
    "output_display": [
      "minecraft:candle",
      "minecraft:white_dye",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:candle",
        "count": 1
      },
      {
        "id": "minecraft:white_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "white_carpet",
    "input": {
      "item": "minecraft:white_carpet",
      "count": 3
    },
    "output_display": [
      "minecraft:white_wool",
      "minecraft:white_wool",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:white_wool",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "white_concrete_powder",
    "input": {
      "item": "minecraft:white_concrete_powder",
      "count": 8
    },
    "output_display": [
      "minecraft:white_dye",
      "minecraft:sand",
      "minecraft:sand",
      "minecraft:sand",
      "minecraft:sand",
      "minecraft:gravel",
      "minecraft:gravel",
      "minecraft:gravel",
      "minecraft:gravel"
    ],
    "output": [
      {
        "id": "minecraft:white_dye",
        "count": 1
      },
      {
        "id": "minecraft:sand",
        "count": 4
      },
      {
        "id": "minecraft:gravel",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "white_dye",
    "input": {
      "item": "minecraft:white_dye",
      "count": 1
    },
    "output_display": [
      "minecraft:bone_meal",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:bone_meal",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "white_dye_from_lily_of_the_valley",
    "input": {
      "item": "minecraft:white_dye",
      "count": 1
    },
    "output_display": [
      "minecraft:lily_of_the_valley",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:lily_of_the_valley",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "white_stained_glass",
    "input": {
      "item": "minecraft:white_stained_glass",
      "count": 8
    },
    "output_display": [
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:white_dye",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass"
    ],
    "output": [
      {
        "id": "minecraft:glass",
        "count": 8
      },
      {
        "id": "minecraft:white_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "white_stained_glass_pane",
    "input": {
      "item": "minecraft:white_stained_glass_pane",
      "count": 16
    },
    "output_display": [
      "minecraft:white_stained_glass",
      "minecraft:white_stained_glass",
      "minecraft:white_stained_glass",
      "minecraft:white_stained_glass",
      "minecraft:white_stained_glass",
      "minecraft:white_stained_glass",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:white_stained_glass",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "white_stained_glass_pane_from_glass_pane",
    "input": {
      "item": "minecraft:white_stained_glass_pane",
      "count": 8
    },
    "output_display": [
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:white_dye",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane"
    ],
    "output": [
      {
        "id": "minecraft:glass_pane",
        "count": 8
      },
      {
        "id": "minecraft:white_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "white_terracotta",
    "input": {
      "item": "minecraft:white_terracotta",
      "count": 8
    },
    "output_display": [
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:white_dye",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta"
    ],
    "output": [
      {
        "id": "minecraft:terracotta",
        "count": 8
      },
      {
        "id": "minecraft:white_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "white_wool_from_string",
    "input": {
      "item": "minecraft:white_wool",
      "count": 1
    },
    "output_display": [
      "minecraft:string",
      "minecraft:string",
      None,
      "minecraft:string",
      "minecraft:string",
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:string",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "wild_armor_trim_smithing_template",
    "input": {
      "item": "minecraft:wild_armor_trim_smithing_template",
      "count": 2
    },
    "output_display": [
      "minecraft:diamond",
      "minecraft:wild_armor_trim_smithing_template",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:mossy_cobblestone",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:diamond",
      "minecraft:diamond"
    ],
    "output": [
      {
        "id": "minecraft:diamond",
        "count": 7
      },
      {
        "id": "minecraft:wild_armor_trim_smithing_template",
        "count": 1
      },
      {
        "id": "minecraft:mossy_cobblestone",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "wind_charge",
    "input": {
      "item": "minecraft:wind_charge",
      "count": 4
    },
    "output_display": [
      "minecraft:breeze_rod",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:breeze_rod",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "wolf_armor",
    "input": {
      "item": "minecraft:wolf_armor",
      "count": 1
    },
    "output_display": [
      "minecraft:armadillo_scute",
      None,
      None,
      "minecraft:armadillo_scute",
      "minecraft:armadillo_scute",
      "minecraft:armadillo_scute",
      "minecraft:armadillo_scute",
      None,
      "minecraft:armadillo_scute"
    ],
    "output": [
      {
        "id": "minecraft:armadillo_scute",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "wooden_axe",
    "input": {
      "item": "minecraft:wooden_axe",
      "count": 1
    },
    "output_display": [
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      None,
      "minecraft:oak_planks",
      "minecraft:stick",
      None,
      None,
      "minecraft:stick",
      None
    ],
    "output": [
      {
        "id": "minecraft:oak_planks",
        "count": 3
      },
      {
        "id": "minecraft:stick",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "wooden_hoe",
    "input": {
      "item": "minecraft:wooden_hoe",
      "count": 1
    },
    "output_display": [
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      None,
      None,
      "minecraft:stick",
      None,
      None,
      "minecraft:stick",
      None
    ],
    "output": [
      {
        "id": "minecraft:oak_planks",
        "count": 2
      },
      {
        "id": "minecraft:stick",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "wooden_pickaxe",
    "input": {
      "item": "minecraft:wooden_pickaxe",
      "count": 1
    },
    "output_display": [
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      None,
      "minecraft:stick",
      None,
      None,
      "minecraft:stick",
      None
    ],
    "output": [
      {
        "id": "minecraft:oak_planks",
        "count": 3
      },
      {
        "id": "minecraft:stick",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "wooden_shovel",
    "input": {
      "item": "minecraft:wooden_shovel",
      "count": 1
    },
    "output_display": [
      "minecraft:oak_planks",
      None,
      None,
      "minecraft:stick",
      None,
      None,
      "minecraft:stick",
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:oak_planks",
        "count": 1
      },
      {
        "id": "minecraft:stick",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "wooden_sword",
    "input": {
      "item": "minecraft:wooden_sword",
      "count": 1
    },
    "output_display": [
      "minecraft:oak_planks",
      None,
      None,
      "minecraft:oak_planks",
      None,
      None,
      "minecraft:stick",
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:oak_planks",
        "count": 2
      },
      {
        "id": "minecraft:stick",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "writable_book",
    "input": {
      "item": "minecraft:writable_book",
      "count": 1
    },
    "output_display": [
      "minecraft:book",
      "minecraft:ink_sac",
      "minecraft:feather",
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:book",
        "count": 1
      },
      {
        "id": "minecraft:ink_sac",
        "count": 1
      },
      {
        "id": "minecraft:feather",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "yellow_banner",
    "input": {
      "item": "minecraft:yellow_banner",
      "count": 1
    },
    "output_display": [
      "minecraft:yellow_wool",
      "minecraft:yellow_wool",
      "minecraft:yellow_wool",
      "minecraft:yellow_wool",
      "minecraft:yellow_wool",
      "minecraft:yellow_wool",
      None,
      "minecraft:stick",
      None
    ],
    "output": [
      {
        "id": "minecraft:yellow_wool",
        "count": 6
      },
      {
        "id": "minecraft:stick",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "yellow_bed",
    "input": {
      "item": "minecraft:yellow_bed",
      "count": 1
    },
    "output_display": [
      "minecraft:yellow_wool",
      "minecraft:yellow_wool",
      "minecraft:yellow_wool",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      "minecraft:oak_planks",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:yellow_wool",
        "count": 3
      },
      {
        "id": "minecraft:oak_planks",
        "count": 3
      }
    ]
  },
  {
    "crafting_recipe_name": "yellow_candle",
    "input": {
      "item": "minecraft:yellow_candle",
      "count": 1
    },
    "output_display": [
      "minecraft:candle",
      "minecraft:yellow_dye",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:candle",
        "count": 1
      },
      {
        "id": "minecraft:yellow_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "yellow_carpet",
    "input": {
      "item": "minecraft:yellow_carpet",
      "count": 3
    },
    "output_display": [
      "minecraft:yellow_wool",
      "minecraft:yellow_wool",
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:yellow_wool",
        "count": 2
      }
    ]
  },
  {
    "crafting_recipe_name": "yellow_concrete_powder",
    "input": {
      "item": "minecraft:yellow_concrete_powder",
      "count": 8
    },
    "output_display": [
      "minecraft:yellow_dye",
      "minecraft:sand",
      "minecraft:sand",
      "minecraft:sand",
      "minecraft:sand",
      "minecraft:gravel",
      "minecraft:gravel",
      "minecraft:gravel",
      "minecraft:gravel"
    ],
    "output": [
      {
        "id": "minecraft:yellow_dye",
        "count": 1
      },
      {
        "id": "minecraft:sand",
        "count": 4
      },
      {
        "id": "minecraft:gravel",
        "count": 4
      }
    ]
  },
  {
    "crafting_recipe_name": "yellow_dye_from_dandelion",
    "input": {
      "item": "minecraft:yellow_dye",
      "count": 1
    },
    "output_display": [
      "minecraft:dandelion",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:dandelion",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "yellow_dye_from_sunflower",
    "input": {
      "item": "minecraft:yellow_dye",
      "count": 2
    },
    "output_display": [
      "minecraft:sunflower",
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:sunflower",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "yellow_stained_glass",
    "input": {
      "item": "minecraft:yellow_stained_glass",
      "count": 8
    },
    "output_display": [
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:yellow_dye",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass",
      "minecraft:glass"
    ],
    "output": [
      {
        "id": "minecraft:glass",
        "count": 8
      },
      {
        "id": "minecraft:yellow_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "yellow_stained_glass_pane",
    "input": {
      "item": "minecraft:yellow_stained_glass_pane",
      "count": 16
    },
    "output_display": [
      "minecraft:yellow_stained_glass",
      "minecraft:yellow_stained_glass",
      "minecraft:yellow_stained_glass",
      "minecraft:yellow_stained_glass",
      "minecraft:yellow_stained_glass",
      "minecraft:yellow_stained_glass",
      None,
      None,
      None
    ],
    "output": [
      {
        "id": "minecraft:yellow_stained_glass",
        "count": 6
      }
    ]
  },
  {
    "crafting_recipe_name": "yellow_stained_glass_pane_from_glass_pane",
    "input": {
      "item": "minecraft:yellow_stained_glass_pane",
      "count": 8
    },
    "output_display": [
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:yellow_dye",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane",
      "minecraft:glass_pane"
    ],
    "output": [
      {
        "id": "minecraft:glass_pane",
        "count": 8
      },
      {
        "id": "minecraft:yellow_dye",
        "count": 1
      }
    ]
  },
  {
    "crafting_recipe_name": "yellow_terracotta",
    "input": {
      "item": "minecraft:yellow_terracotta",
      "count": 8
    },
    "output_display": [
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:yellow_dye",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta",
      "minecraft:terracotta"
    ],
    "output": [
      {
        "id": "minecraft:terracotta",
        "count": 8
      },
      {
        "id": "minecraft:yellow_dye",
        "count": 1
      }
    ]
  }
]


slot_dict = {
  0:"6b",
  1:"7b",
  2:"8b",
  3:'15b',
  4:'16b',
  5:'17b',
  6:'24b',
  7:'25b',
  8:'26b',
}


folder_path = "data/gui/function/barrel/decrafter/decraft_recipes"

# for filename in os.listdir(folder_path):
#    file_path = os.path.join(folder_path, filename)
#    if os.path.isfile(file_path):
#       os.remove(file_path)



# print(crafting_recipe)
for recipe in crafting_recipe:
  # continue
  recipe_name = recipe['crafting_recipe_name']
  input_name = recipe['input']['item']
  input_quantity = recipe['input']['count']


# data modify storage minecraft:ui decraft.output set value [{id:"minecraft:oak_planks",count:4,Slot:0b},{id:"minecraft:stick",count:2,Slot:1b}]
# function gui:barrel/decrafter/send_to_result with storage minecraft:ui decraft
# return 1

  if os.path.isfile(f"data/gui/function/barrel/decrafter/decraft_recipes/{input_quantity}_{input_name[10:]}.mcfunction"):
    continue
  f = open(f"data/gui/function/barrel/decrafter/decraft_recipes/{input_quantity}_{input_name[10:]}.mcfunction", "x")
  line = "data modify storage minecraft:ui decraft.output set value ["
  for index_output in range(len(recipe['output'])):
    output = recipe['output'][index_output]
    output_name = output['id']
    output_quantity = output['count']
    line += "{id:\"" + output_name + "\",count:" + str(output_quantity) + ",Slot:" + str(index_output) + "b}"
    if index_output == len(recipe['output'])-1:
      line += "]\n"
    else:
      line += ","
  f.write(line)
  f.write("function gui:barrel/decrafter/send_to_result with storage minecraft:ui decraft\n")
  f.close()
  
# data modify storage minecraft:ui DecraftResult[3] set value {Slot:15b,id:"minecraft:oak_planks","components":{"minecraft:custom_data":{ui_item:1,actions:{}}}}
# data modify storage minecraft:ui DecraftResult[4] set value {Slot:16b,id:"minecraft:stick","components":{"minecraft:custom_data":{ui_item:1,actions:{}}}}
# data modify storage minecraft:ui DecraftResult[5] set value {Slot:17b,id:"minecraft:oak_planks","components":{"minecraft:custom_data":{ui_item:1,actions:{}}}}
# data modify storage minecraft:ui DecraftResult[6] set value {Slot:24b,id:"minecraft:oak_planks","components":{"minecraft:custom_data":{ui_item:1,actions:{}}}}
# data modify storage minecraft:ui DecraftResult[7] set value {Slot:25b,id:"minecraft:stick","components":{"minecraft:custom_data":{ui_item:1,actions:{}}}}
# data modify storage minecraft:ui DecraftResult[8] set value {Slot:26b,id:"minecraft:oak_planks","components":{"minecraft:custom_data":{ui_item:1,actions:{}}}}
  if os.path.isfile(f"data/gui/function/barrel/decrafter/decraft_recipes/{input_quantity}_{input_name[10:]}_display.mcfunction"):
    continue
  f = open(f"data/gui/function/barrel/decrafter/decraft_recipes/{input_quantity}_{input_name[10:]}_display.mcfunction", "x")
  for index_output in range(len(recipe['output_display'])):
    output_id = recipe['output_display'][index_output]
    if output_id == None:
      continue
    f.write("data modify storage minecraft:ui DecraftResult[" + str(index_output) + "] set value {Slot:" + slot_dict[index_output] + ",id:\"" + output_id + "\",\"components\":{\"minecraft:custom_data\":{ui_item:1,actions:{}}}}\n")
  f.write("return 1")
  f.close()


# execute at @s if data block ~ ~ ~ Items[{Slot:1b,id:"minecraft:oak_fence",count:3}] run return run function gui:barrel/decrafter/decraft_recipes/oak_fence

  # with open("data/gui/function/barrel/decrafter/try_decraft.mcfunction", 'a') as file:
  # # print("execute at @s if data block ~ ~ ~ Items[{Slot:1b,id:\"" + input_name + "\",count:" + str(input_quantity) + "}] run return run function gui:barrel/decrafter/decraft_recipes/" + recipe_name)
  #   file.write("execute at @s if data block ~ ~ ~ Items[{Slot:1b,id:\"" + input_name + "\",count:" + str(input_quantity) + "}] run return run function gui:barrel/decrafter/decraft_recipes/" + recipe_name + "\n")
  # with open("data/gui/function/barrel/decrafter/try_decraft_display.mcfunction", 'a') as file:
  # # print("execute at @s if data block ~ ~ ~ Items[{Slot:1b,id:\"" + input_name + "\",count:" + str(input_quantity) + "}] run return run function gui:barrel/decrafter/decraft_recipes/" + recipe_name)
  #   file.write("execute at @s if data block ~ ~ ~ Items[{Slot:1b,id:\"" + input_name + "\",count:" + str(input_quantity) + "}] run return run function gui:barrel/decrafter/decraft_recipes/" + recipe_name + "_display\n")