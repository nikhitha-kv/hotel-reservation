# Hotel Room Reservation System

## Overview

This project is a simple hotel room reservation system developed as part of an assessment.

The system automatically assigns rooms based on availability and travel time rules.  
Priority is given to booking rooms on the same floor. If that is not possible, rooms across floors are selected in a way that minimizes total travel time.

---

## Hotel Details

- Total number of rooms: 97  
- Floors 1 to 9: 10 rooms per floor  
- Floor 10: 7 rooms only  
- Rooms are arranged from left to right  
- Staircase and lift are located on the left side

---

## Travel Time Rules

- Horizontal movement:  
  - 1 minute per adjacent room on the same floor

- Vertical movement:  
  - 2 minutes per floor

Total Travel Time = Vertical Travel + Horizontal Travel


---

## Booking Rules

- A guest can book up to 5 rooms at a time  
- Rooms on the same floor are given first priority  
- If sufficient rooms are not available on one floor, booking spans multiple floors  
- The combination with the minimum travel time is selected  
- Once booked, rooms are marked as occupied

---

## Features

- Input to select number of rooms (1–5)
- Automatic optimal room booking
- Random room occupancy generator
- Reset option to clear all bookings
- Visual representation of hotel rooms

---

## Tech Stack

- Frontend: HTML, CSS, JavaScript  
- Backend: Python (Flask)

---

## Project Structure
```bash
hotel-reservation/
│
├── app.py
├── templates/
│ └── index.html
├── static/
│ └── style.css
└── README.md
```

---

## How to Run the Project

1. Install Flask

`pip install flask`

2. Run the application

`python app.py`

3. Open the browser and visit

[http://127.0.0.1:5000](http://127.0.0.1:5000)


---

## Author

Nikhitha KV

