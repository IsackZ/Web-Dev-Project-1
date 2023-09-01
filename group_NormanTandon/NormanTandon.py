import statistics
song_data = [
    {
        "title": "Groove Machine",
        "artist": "Funk Fusion",
        "genre": "Funk",
        "duration": 180,
        "energy": 0.85,
        "danceability": 0.75,
        "tempo": 110,
    },
    {
        "title": "Sunset Serenade",
        "artist": "Chillwave Collective",
        "genre": "Electronic",
        "duration": 240,
        "energy": 0.55,
        "danceability": 0.65,
        "tempo": 100,
    },
    {
        "title": "Guitar Grooves",
        "artist": "Acoustic Ensemble",
        "genre": "Acoustic",
        "duration": 210,
        "energy": 0.6,
        "danceability": 0.4,
        "tempo": 80,
    },
    {
        "title": "Rock Anthem",
        "artist": "Electric Rebellion",
        "genre": "Rock",
        "duration": 280,
        "energy": 0.9,
        "danceability": 0.6,
        "tempo": 140,
    },
    {
        "title": "Jazz Reflections",
        "artist": "Smooth Jazz Quartet",
        "genre": "Jazz",
        "duration": 320,
        "energy": 0.4,
        "danceability": 0.3,
        "tempo": 90,
    }
]

def collectData(data):
    dataList = []
    i = 0
    while i <= 4:
        dataList.append(song_data[i][data])
        i += 1
    return dataList
print(collectData("duration"))    
durationList = collectData("duration")

def calculateStats(list , operation):
    list.sort()
    if operation == "Median":
        mid = len(list)//2
        median = (list[mid] - list[~mid]) / 2
        print(list[mid])
    elif operation == "Mean":
        print(sum(list)/len(list))
    elif operation == "Mode":
        print(statistics.mode(list))
    else:
        print(Error)

print(calculateStats(durationList, "Mode"))
print(calculateStats(durationList, "Mean"))
print(calculateStats(durationList, "Median"))
