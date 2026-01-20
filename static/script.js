function bookRooms() {

    let count = document.getElementById("count").value;

    fetch("/book", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ count: count })
    })
    .then(res => res.json())
    .then(data => {

        let msg = document.getElementById("message");

        if (data.error) {
            msg.innerText = data.error;
            return;
        }

        msg.innerText = "Booked rooms: " + data.rooms.join(", ");

        setTimeout(() => {
            location.reload();
        }, 800);
    });
}

function randomFill() {
    fetch("/random", { method: "POST" })
        .then(() => location.reload());
}

function resetAll() {
    fetch("/reset", { method: "POST" })
        .then(() => location.reload());
}
