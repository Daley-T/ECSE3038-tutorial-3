from fastapi import FastAPI, HTTPException

app = FastAPI()

readings = [
    {"name": "front-door", "room": "hall",    "temp": 27.4, "online": True},
    {"name": "hall-lamp",  "room": "hall",    "temp": 26.1, "online": True},
    {"name": "attic",      "room": "attic",   "temp": 31.9, "online": True},
    {"name": "fridge",     "room": "kitchen", "temp": 4.2,  "online": False},
    {"name": "patio",      "room": "outside", "temp": 29.8, "online": True},
]

device = readings.copy()

def avg_temp(array):
    avg:float = 0.0
    new_sum:float = 0.0
    for i in range(len(array)):
        new_sum = new_sum + device[i]["temp"]
        avg = round((new_sum / (len(array))),2)
    print("\nAverage Temp. = " ,avg)

avg_temp(device)


def hottest(array):
    hotter:float = 0.0
    index:int = 0
    for i in range(len(array)):
        if device[i]["temp"] > hotter:
            hotter = device[i]["temp"]
            index = i
    print("\nHottest Temp Dictionary:\n",device[index])

hottest(device)