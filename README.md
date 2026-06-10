# The-Study-Election-App-26
# 🗳️ Student Council Election Management System

A secure Flask-based digital voting platform designed for conducting Student Council Elections within a school environment.

Built for:

**The Study L'Ecole Internationale**

Version: **Final4**

---

# Overview

This application allows students to vote digitally for:

* Head Boy
* Head Girl

The system validates student TS Numbers, prevents duplicate voting, records votes securely, and provides a live administrative dashboard for election monitoring.

The application is designed to run entirely within a local school network and does not require internet access.

---

# Key Features

## Student Authentication

* TS Number based login
* Validation against approved voter list
* Unauthorized students cannot vote

## Vote Protection

* One student = one vote
* Duplicate voting prevention
* Session-controlled voting workflow

## Digital Ballot System

* Candidate photographs
* Candidate selection interface
* Head Boy voting
* Head Girl voting

## Vote Storage

* Automatic vote recording
* CSV-based storage
* Timestamp recording

## Administration

* Live results dashboard
* Total vote count
* Candidate vote counts
* Election monitoring

## API Support

Live election data endpoint:

```text
/api/results
```

Returns JSON formatted election results.

---

# Project Structure

project/

│

├── app.py

├── requirements.txt

├── votes.csv

├── valid_ts_numbers.csv

│

├── static/

│   ├── bg.jpg

│   ├── logo.png

│   ├── hb1.jpg

│   ├── hb2.jpg

│   ├── hb3.jpg

│   ├── hb4.jpg

│   ├── hg1.jpg

│   ├── hg2.jpg

│   ├── hg3.jpg

│   └── hg4.jpg

│

└── templates/

```
├── login.html

├── landing.html

├── headboy.html

├── headgirl.html

├── thanks.html

└── admin.html
```

---

# Installation

## Step 1: Clone / Download

Download the project folder.

---

## Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 3: Run Application

```bash
python app.py
```

Application starts on:

```text
http://127.0.0.1:5000
```

---

# Election Workflow

1. Student enters TS Number
2. System validates TS Number
3. Student votes for Head Boy
4. Student votes for Head Girl
5. Vote is recorded
6. Thank You page displayed
7. Session cleared
8. System returns to login page

---

# Admin Dashboard

Administrative dashboard available at:

```text
/admin
```

Dashboard provides:

* Total votes cast
* Head Boy vote counts
* Head Girl vote counts
* Live election monitoring

---

# Results API

Live election results:

```text
/api/results
```

Example response:

```json
{
    "total_votes": 250,
    "headboy": {
        "Candidate 1": 85,
        "Candidate 2": 60,
        "Candidate 3": 55,
        "Candidate 4": 50
    },
    "headgirl": {
        "Candidate A": 90,
        "Candidate B": 70,
        "Candidate C": 50,
        "Candidate D": 40
    }
}
```

---

# Data Files

## valid_ts_numbers.csv

Contains approved student TS Numbers.

Example:

```csv
TS001
TS002
TS003
TS004
```

---

## votes.csv

Stores all recorded votes.

Example:

```csv
TIMESTAMP,TS_NO,HEAD_BOY,HEAD_GIRL
2026-06-10 09:15:10,TS001,Candidate 1,Candidate A
```

---

# Security Measures

* TS Number verification
* Duplicate vote prevention
* Session management
* Local data storage
* No internet dependency
* Controlled administrative access

---

# Network Deployment

Recommended Setup:

* 1 Admin Laptop
* 4–10 Voting Stations
* Same Wi-Fi / LAN Network

Access application using:

```text
http://<SERVER-IP>:5000
```

Example:

```text
http://192.168.1.100:5000
```

---

# Election Day Checklist

Before opening voting:

* Verify candidate names
* Verify candidate photographs
* Verify TS Number list
* Test valid login
* Test invalid login
* Test duplicate vote prevention
* Test vote recording
* Test admin dashboard
* Backup votes.csv

---

# Technology Stack

* Python 3
* Flask
* HTML
* CSS
* JavaScript
* CSV Storage

---

# License

Developed for educational and institutional election management purposes.

---

© 2026 Student Council Election System
