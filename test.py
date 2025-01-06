import json

enemies = [
  {
    "type": "REGULAR",
    "name": "Goblin",
    "maxhp": 12,
    "currenthp": 12,
    "strength": 5,
    "golddrop": 2,
    "expdrop": 7,
    "weapon": {
      "name": "none",
      "strength": 0,
      "durability": 8192
    },
    "weapondrop": {
      "type": "WEAPON",
      "name": "Goblin Club",
      "strength": 6,
      "durability": 10,
      "cost": 6
    }
  },
  {
    "type": "REGULAR",
    "name": "Orc",
    "maxhp": 17,
    "currenthp": 17,
    "strength": 9,
    "golddrop": 3,
    "expdrop": 13,
    "weapon": {
      "name": "none",
      "strength": 0,
      "durability": 8192
    },
    "weapondrop": {
      "type": "WEAPON",
      "name": "Orc Club",
      "strength": 10,
      "durability": 17,
      "cost": 10
    }
  },
  {
    "type": "REGULAR",
    "name": "Slime",
    "maxhp": 10,
    "currenthp": 10,
    "strength": 4,
    "golddrop": 1,
    "expdrop": 6,
    "weapon": {
      "name": "none",
      "strength": 0,
      "durability": 8192
    },
    "weapondrop": {
      "type": "HEALING ITEM",
      "name": "Secretion",
      "heal": 6,
      "cost": 4
    }
  },
  {
    "type": "REGULAR",
    "name": "Strong Orc",
    "maxhp": 23,
    "currenthp": 23,
    "strength": 15,
    "golddrop": 12,
    "expdrop": 17,
    "weapon": {
      "name": "none",
      "strength": 0,
      "durability": 8192
    },
    "weapondrop": {
      "type": "WEAPON",
      "name": "Gold Orc Club",
      "strength": 23,
      "durability": 20,
      "cost": 18
    }
  },
  {
    "type": "REGULAR",
    "name": "Strong Slime",
    "maxhp": 15,
    "currenthp": 15,
    "strength": 8,
    "golddrop": 9,
    "expdrop": 9,
    "weapon": {
      "name": "none",
      "strength": 0,
      "durability": 8192
    },
    "weapondrop": {
      "type": "HEALING ITEM",
      "name": "Cool Slime Secretion",
      "heal": 14,
      "cost": 10
    }
  },
  {
    "type": "GRIFTER",
    "name": "Grifter",
    "maxhp": 24,
    "currenthp": 24,
    "strength": 0,
    "steal": 7,
    "golddrop": 19,
    "expdrop": 17,
    "weapon": {
      "name": "none",
      "strength": 0,
      "durability": 8192
    },
    "weapondrop": {
      "type": "WEAPON",
      "name": "Grifter Staff",
      "strength": 8,
      "durability": 1000,
      "cost": 19
    }
  },
  {
    "type": "BOSS",
    "name": "King Orc",
    "maxhp": 140,
    "currenthp": 140,
    "strength": 20,
    "expdrop": 39,
    "weapon": {
      "name": "none",
      "strength": 0,
      "durability": 10000
    }
  }
]

with open('enemies.json', 'w') as file:
    json.dump(enemies, file, indent=2)