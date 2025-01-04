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
        "exit": [{
            "destination": 1,
            "rectangles": [1240, 280, 80, 80],
            "coordinates": [40, 300]
        }]
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
        "exit":[
            {
                "destination" : 0,
                "rectangles" : [0, 280, 40, 80],
                "coordinates": [1200, 300]
            },
            {
                "destination": 2,
                "rectangles": [1240, 280, 80, 80],
                "coordinates": [40, 300]
            }]
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
        "exit":[
            {
                "destination" : 1,
                "rectangles" : [0, 280, 40, 80],
                "coordinates": [1200, 300]
            },
            {
                "destination": 3,
                "rectangles": [1240, 280, 80, 80],
                "coordinates": [50, 30]
            },
            {
                "destination" : 5,
                "rectangles" : [610, 580, 80, 40],
                "coordinates" : [630, 40]
            }]
    },
    {
        "id": 3,
        "rectangles": [
            [10, 10, 1260, 100],
            [10, 260, 1260, 100],
            [10, 510, 1260, 100],
            [590, 10, 100, 590]
        ],
        "exit":[
            {
                "destination" : 2,
                "rectangles" : [0, 20, 40, 80],
                "coordinates": [1200, 300]
            },
            {
                "destination": 4,
                "rectangles": [1240, 270, 80, 80],
                "coordinates": [40, 300]
            }]
    },
    {
        "id": 4,
        "rectangles":
        [
            [10, 260, 1250, 100],
            [210, 10, 1150, 650]
        ],
        "exit": [
            {
                "destination" : 3,
                "rectangles" : [0, 270, 40, 80],
                "coordinates": [1200, 280]
            }]
            
    },
    {
        "id": 5,
        "rectangles":
        [
            [600, 0, 80, 200],
            [140, 200, 980, 400]
        ],
        "exit": [
            {
                "destination" : 2,
                "rectangles" : [590, 0, 100, 40],
                "coordinates" : [610, 30]
            }]
            
    }
]

#with open('rooms.json', 'w') as file:
    #json.dump(rooms, file)
