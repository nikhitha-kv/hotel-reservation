from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)


def create_rooms():
    rooms = []

    for floor in range(1, 10):
        for i in range(1, 11):
            rooms.append({
                "room": floor * 100 + i,
                "floor": floor,
                "pos": i,
                "occupied": False
            })


    for i in range(1, 8):
        rooms.append({
            "room": 1000 + i,
            "floor": 10,
            "pos": i,
            "occupied": False
        })

    return rooms


rooms = create_rooms()


def travel_time(group):
    floors = [r["floor"] for r in group]
    positions = [r["pos"] for r in group]

    vertical = (max(floors) - min(floors)) * 2
    horizontal = max(positions) - min(positions)

    return vertical + horizontal



@app.route("/")
def home():
    return render_template("index.html", rooms=rooms)


@app.route("/random", methods=["POST"])
def random_fill():
    for r in rooms:
        r["occupied"] = random.choice([True, False, False])
    return jsonify(success=True)


@app.route("/reset", methods=["POST"])
def reset():
    for r in rooms:
        r["occupied"] = False
    return jsonify(success=True)


@app.route("/book", methods=["POST"])
def book():
    count = int(request.json["count"])

    if count > 5 or count < 1:
        return jsonify(error="Invalid room count")

    available = [r for r in rooms if not r["occupied"]]

    best = None
    best_time = float("inf")


    floors = {}
    for r in available:
        floors.setdefault(r["floor"], []).append(r)

    for floor_rooms in floors.values():
        if len(floor_rooms) >= count:
            floor_rooms.sort(key=lambda x: x["pos"])
            for i in range(len(floor_rooms) - count + 1):
                group = floor_rooms[i:i+count]
                t = travel_time(group)
                if t < best_time:
                    best = group
                    best_time = t

    if not best:
        available.sort(key=lambda x: (x["floor"], x["pos"]))
        for i in range(len(available) - count + 1):
            group = available[i:i+count]
            t = travel_time(group)
            if t < best_time:
                best = group
                best_time = t

    if not best:
        return jsonify(error="Not enough rooms")

    for r in best:
        r["occupied"] = True

    return jsonify(booked=[r["room"] for r in best])


if __name__ == "__main__":
    app.run(debug=True)
