#Hotel Room Reservation System
##Overview

This project is a hotel room booking system developed as part of an assessment.

The system automatically assigns rooms based on availability and travel time rules.
Priority is given to booking rooms on the same floor, and if that is not possible, rooms across floors are selected in a way that minimizes total travel distance.

##Hotel Details

  Total rooms: 97

  Floors 1–9: 10 rooms each

  Floor 10: 7 rooms

  Rooms are arranged from left to right

  Staircase and lift are on the left side

##Travel Time Rules

###Horizontal movement:

  1 minute per adjacent room on the same floor

###Vertical movement:

  2 minutes per floor

Total Travel Time = Vertical Time + Horizontal Time

##Booking Rules

  A guest can book up to 5 rooms

  Same floor rooms are preferred

  If not available, booking spans multiple floors

  Rooms are chosen based on minimum travel time

  Once booked, rooms become unavailable

##Features

  Enter number of rooms to book

  Book rooms automatically

  Generate random room occupancy

  Reset all bookings

  Visual representation of rooms

##Tech Stack

  Frontend: HTML, CSS, JavaScript

  Backend: Python (Flask)

##Project Structure
'''
hotel-reservation/
│
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── README.md
'''

##How to Run

 Install Flask
'''
pip install flask
'''

 Run the application
'''
python app.py
'''

Open browser
'''
http://127.0.0.1:5000
'''


###Author

**Nikhitha KV**