from flask import Flask, render_template, request
import random

app = Flask(__name__)

rooms = []

# create rooms
for f in range(1, 10):
    for i in range(1, 11):
        rooms.append({
            "room": f * 100 + i,
            "floor": f,
            "position": i,
            "occupied": False,
            "just_booked": False
        })

for i in range(1, 8):
    rooms.append({
        "room": 1000 + i,
        "floor": 10,
        "position": i,
        "occupied": False,
        "just_booked": False
    })


def clear_just_booked():
    for r in rooms:
        r["just_booked"] = False


def book_rooms(requested):
    free = [r for r in rooms if not r["occupied"]]

    floors = {}
    for r in free:
        floors.setdefault(r["floor"], []).append(r)

    best = None
    best_spread = None

    # same floor priority
    for fl in floors:
        fr = floors[fl]
        if len(fr) >= requested:
            fr.sort(key=lambda x: x["position"])
            for i in range(len(fr) - requested + 1):
                grp = fr[i:i + requested]
                spread = grp[-1]["position"] - grp[0]["position"]
                if best_spread is None or spread < best_spread:
                    best_spread = spread
                    best = grp

    if best:
        for r in best:
            r["occupied"] = True
            r["just_booked"] = True
        return True

    # multi-floor
    free.sort(key=lambda x: (x["floor"], x["position"]))

    best_time = None
    best = None

    for i in range(len(free) - requested + 1):
        grp = free[i:i + requested]

        floors_used = [r["floor"] for r in grp]
        pos = [r["position"] for r in grp]

        total = (max(floors_used) - min(floors_used)) * 2 + \
                (max(pos) - min(pos))

        if best_time is None or total < best_time:
            best_time = total
            best = grp

    if best:
        for r in best:
            r["occupied"] = True
            r["just_booked"] = True
        return True

    return False


@app.route("/", methods=["GET", "POST"])
def index():
    msg = ""
    msg_type = "info"

    # clear previous highlight
    clear_just_booked()

    if request.method == "POST":
        action = request.form.get("action")

        if action == "random":
            for r in rooms:
                r["occupied"] = random.choice([True, False, False])
            msg = "Random occupancy generated"

        elif action == "reset":
            for r in rooms:
                r["occupied"] = False
            msg = "All rooms reset"

        elif action == "book":
            value = request.form.get("count")

            if not value:
                msg = "Please enter number of rooms"
                msg_type = "error"
            else:
                count = int(value)

                if count < 1 or count > 5:
                    msg = "You can book only 1 to 5 rooms"
                    msg_type = "error"
                else:
                    success = book_rooms(count)
                    if success:
                        msg = "Rooms booked successfully"
                        msg_type = "success"
                    else:
                        msg = "Not enough rooms available"
                        msg_type = "error"

    return render_template(
        "index.html",
        rooms=rooms,
        msg=msg,
        msg_type=msg_type
    )


if __name__ == "__main__":
    app.run(debug=True)
