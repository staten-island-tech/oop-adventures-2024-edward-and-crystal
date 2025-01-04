import json



rooms = [
    {
        "id": 0,
        "rectangles": [
            [10, 10, 100, 590],
            [10, 10 , 1220, 100],
            [1160, 10, 100, 590],
            [100, 500, 1150, 100],
            [590, 10, 100, 590],
            [10, 270, 1220, 100]
        ],
        "spawntable": {
            "enemy count": [1, 2],
            "slime" : 50,
            "goblin" : 45,
            "orc" : 5,
            "strong slime" : 0,
            "strong orc" : 0,
            "grifter" : 0
        }
    },
    {
        "id": 1,
        "rectangles": [
            [10, 10, 100, 590],
            [10, 10 , 1220, 100],
            [1160, 10, 100, 590],
            [100, 500, 1150, 100],
            [590, 10, 100, 590]
        ],
        "spawntable": {
            "enemy count": [1, 2, 2, 2, 3, 3],
            "slime" : 20,
            "goblin" : 60,
            "orc" : 15,
            "strong slime" : 0,
            "strong orc" : 0,
            "grifter" : 5
        }
    },
    {
        "id": 2,
        "rectangles": [
            [10, 10, 100, 590],
            [10, 300, 1220, 100],
            [1160, 10, 100, 590],
            [300, 10, 100, 590],
            [600, 10, 100, 590],
            [880, 10, 100, 590]
        ],
        "spawntable": {
            "enemy count": [2, 2, 3, 3, 3, 4],
            "slime" : 5,
            "goblin" : 45,
            "orc" : 25,
            "strong slime" : 15,
            "strong orc" : 5,
            "grifter" : 5
        }
    },
    {
        "id": 3,
        "rectangles": [
            [10, 10, 1260, 100],
            [10, 260, 1260, 100],
            [10, 510, 1260, 100],
            [590, 10, 100, 590]
        ],
        "spawntable": {
            "enemy count": [3, 4, 4],
            "slime" : 0,
            "goblin" : 15,
            "orc" : 35,
            "strong slime" : 25,
            "strong orc" : 20,
            "grifter" : 5
        }
    },
    {
        "id": 4,
        "rectangles":
        [
            [10, 260, 1250, 100],
            [210, 10, 1150, 650]
        ],
        "spawntable": {
            "enemy count": [1],
            "slime" : 0,
            "goblin" : 0,
            "orc" : 0,
            "strong slime" : 0,
            "strong orc" : 0,
            "grifter" : 1
        }
            
    },
    {
        "id": 5,
        "rectangles":
        [
            [600, 0, 80, 200],
            [140, 200, 980, 400]
        ],
        "spawntable": {
            "enemy count": [1],
            "slime" : 0,
            "goblin" : 0,
            "orc" : 0,
            "strong slime" : 0,
            "strong orc" : 0,
            "grifter" : 1
        }
            
    }
]

with open('rooms.json', 'w') as file:
    json.dump(rooms, file, indent=2)
