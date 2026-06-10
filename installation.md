# Installation Guide

## Student Council Election Management System

Version: Final4

---

# Introduction

This guide explains how to install, configure, and deploy the Student Council Election Management System on a local school network.

The system is designed to support:

* Student Authentication
* Head Boy Voting
* Head Girl Voting
* Duplicate Vote Prevention
* Real-Time Vote Recording
* Administrative Monitoring

---

# Prerequisites

Before installation, ensure the following software is available.

## Required Software

### Python

Version:

```text
Python 3.10 or higher
```

Recommended:

```text
Python 3.13+
```

Verify Installation:

```bash
python --version
```

Expected Output:

```text
Python 3.x.x
```

---

## Pip

Verify:

```bash
pip --version
```

---

# Project Setup

## Step 1: Download Project

Download or clone the project folder.

Example:

```text
StudentElection/
```

---

## Step 2: Verify Project Structure

Ensure the following structure exists.

```text
StudentElection/

│
├── app.py
├── requirements.txt
├── README.md
├── INSTALLATION.md
├── votes.csv
├── valid_ts_numbers.csv
│
├── templates/
│   ├── login.html
│   ├── headboy.html
│   ├── headgirl.html
│   ├── thanks.html
│   └── admin.html
│
└── static/
    ├── logo.png
    ├── bg.jpg
    ├── hb1.jpg
    ├── hb2.jpg
    ├── hb3.jpg
    ├── hb4.jpg
    ├── hg1.jpg
    ├── hg2.jpg
    ├── hg3.jpg
    └── hg4.jpg
```

---

# Step 3: Open Terminal

Navigate to project folder.

Example:

```bash
cd StudentElection
```

---

# Step 4: Install Dependencies

Install required packages:

```bash
pip install -r requirements.txt
```

Expected Installation:

```text
Flask
```

---

# Configure Candidate Information

## Head Boy Candidates

Open:

```text
app.py
```

Locate:

```python
HEADBOYS = [
    "Candidate 1",
    "Candidate 2",
    "Candidate 3",
    "Candidate 4"
]
```

Replace with actual candidate names.

Example:

```python
HEADBOYS = [
    "Arjun",
    "Rahul",
    "Harish",
    "Vignesh"
]
```

---

## Head Girl Candidates

Locate:

```python
HEADGIRLS = [
    "Candidate A",
    "Candidate B",
    "Candidate C",
    "Candidate D"
]
```

Replace with actual candidate names.

---

# Configure Candidate Images

Place candidate photographs inside:

```text
static/
```

Naming convention:

## Head Boy

```text
hb1.jpg
hb2.jpg
hb3.jpg
hb4.jpg
```

## Head Girl

```text
hg1.jpg
hg2.jpg
hg3.jpg
hg4.jpg
```

---

# Configure School Logo

Place logo file:

```text
logo.png
```

inside:

```text
static/
```

---

# Configure Background Image

Place:

```text
bg.jpg
```

inside:

```text
static/
```

Recommended Resolution:

```text
1920 x 1080
```

---

# Configure Voter Database

Open:

```text
valid_ts_numbers.csv
```

Add one TS Number per line.

Example:

```csv
TS001
TS002
TS003
TS004
TS005
```

For large elections:

```text
700–1000 student records supported
```

---

# Running The Application

Start server:

```bash
python app.py
```

Expected Output:

```text
* Running on http://127.0.0.1:5000
```

---

# Accessing The System

Open browser:

```text
http://127.0.0.1:5000
```

---

# Local Network Deployment

## Find Server IP

On Windows:

```bash
ipconfig
```

Locate:

```text
IPv4 Address
```

Example:

```text
192.168.1.100
```

---

## Voting Stations

Open:

```text
http://192.168.1.100:5000
```

from all voting computers.

Requirements:

* Same Wi-Fi network
  or
* Same LAN network

---

# Administrative Access

Administrator access can be configured through the special login code.

Example:

```text
0000
```

Entering this code opens the administrative dashboard.

---

# Results Dashboard

Dashboard URL:

```text
/admin
```

Provides:

* Total Votes
* Candidate Vote Counts
* Election Monitoring

---

# Results API

API Endpoint:

```text
/api/results
```

Returns live election data.

Example:

```json
{
  "total_votes": 120,
  "headboy": {},
  "headgirl": {}
}
```

---

# Data Storage

## votes.csv

Stores:

* Timestamp
* TS Number
* Head Boy Vote
* Head Girl Vote

Example:

```csv
TIMESTAMP,TS_NO,HEAD_BOY,HEAD_GIRL
2026-06-10 09:30:22,TS001,Arjun,Priya
```

---

# Backup Procedure

Before Election:

```text
Backup valid_ts_numbers.csv
```

During Election:

```text
Periodically backup votes.csv
```

After Election:

```text
Create final backup of votes.csv
```

Recommended:

```text
Google Drive
USB Drive
School Server
```

---

# Election Day Checklist

Before Opening Polls:

☐ Candidate names verified

☐ Candidate photos verified

☐ School logo verified

☐ TS database verified

☐ Admin access tested

☐ Duplicate voting tested

☐ Vote recording tested

☐ Dashboard tested

☐ Network tested

☐ Backup created

---

# Troubleshooting

## Flask Not Installed

Error:

```text
ModuleNotFoundError: No module named 'flask'
```

Solution:

```bash
pip install Flask
```

---

## Images Not Showing

Verify files exist inside:

```text
static/
```

Check filenames exactly.

---

## TS Number Not Accepted

Verify entry exists in:

```text
valid_ts_numbers.csv
```

---

## Duplicate Vote Message

The student has already voted.

Verify:

```text
votes.csv
```

---

## Dashboard Not Loading

Verify:

```text
/admin
```

and

```text
/api/results
```

are accessible.

---

# Recommended Election Setup

Server:

* 1 Admin Laptop

Voting Stations:

* 4–10 Computers

Expected Capacity:

* 700–1000 Students

Network:

* Local Wi-Fi or LAN

---

# Developed Using

* Python
* Flask
* HTML
* CSS
* JavaScript
* CSV Storage

---

# Version Information

Application Version: Final4

Status: Production Ready

Deployment Type: Local Network Election System
