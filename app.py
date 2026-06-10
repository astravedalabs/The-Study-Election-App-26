from flask import Flask, render_template, request, redirect, session, jsonify
import csv
import os
from datetime import datetime
from collections import Counter

app = Flask(__name__)
app.secret_key = "STUDENT_ELECTION_2026_SECRET"

CSV_FILE = "votes.csv"
VALID_TS_FILE = "valid_ts_numbers.csv"

# =====================================
# CANDIDATES
# =====================================

HEADBOYS = [
    "Candidate 1",
    "Candidate 2",
    "Candidate 3",
    "Candidate 4"
]

HEADGIRLS = [
    "Candidate A",
    "Candidate B",
    "Candidate C",
    "Candidate D"
]

# =====================================
# LOAD VALID TS NUMBERS
# =====================================

VALID_TS = set()

if os.path.exists(VALID_TS_FILE):

    with open(
        VALID_TS_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        reader = csv.reader(file)

        for row in reader:

            if row:
                VALID_TS.add(row[0].strip())

# =====================================
# CREATE VOTES FILE
# =====================================

if (
    not os.path.exists(CSV_FILE)
    or
    os.path.getsize(CSV_FILE) == 0
):

    with open(
        CSV_FILE,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "TIMESTAMP",
            "TS_NO",
            "HEAD_BOY",
            "HEAD_GIRL"
        ])

# =====================================
# HELPERS
# =====================================

def valid_ts_number(ts_no):

    return ts_no in VALID_TS


def already_voted(ts_no):

    try:

        with open(
            CSV_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:

                if row["TS_NO"] == ts_no:
                    return True

    except Exception:
        pass

    return False

# =====================================
# LOGIN
# =====================================

@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        ts_no = request.form["ts_no"].strip()

        # ADMIN ACCESS
        if ts_no == "AVLadmin123":

            return redirect("/admin")

        if not valid_ts_number(ts_no):

            return """
            <h2>TS Number Not Found</h2>
            <a href="/">Back</a>
            """

        if already_voted(ts_no):

            return """
            <h2>This TS Number Has Already Voted</h2>
            <a href="/">Back</a>
            """

        session.clear()

        session["ts_no"] = ts_no

        return redirect("/headboy")

    return render_template("login.html")

# =====================================
# HEAD BOY
# =====================================

@app.route("/headboy", methods=["GET", "POST"])
def headboy():

    if "ts_no" not in session:
        return redirect("/")

    if request.method == "POST":

        candidate = request.form.get("candidate")

        if not candidate:
            return redirect("/headboy")

        session["headboy_vote"] = candidate

        return redirect("/headgirl")

    return render_template(
        "headboy.html",
        candidates=HEADBOYS
    )

# =====================================
# HEAD GIRL
# =====================================

@app.route("/headgirl", methods=["GET", "POST"])
def headgirl():

    if "ts_no" not in session:
        return redirect("/")

    if "headboy_vote" not in session:
        return redirect("/headboy")

    if request.method == "POST":

        candidate = request.form.get("candidate")

        if not candidate:
            return redirect("/headgirl")

        with open(
            CSV_FILE,
            "a",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),
                session["ts_no"],
                session["headboy_vote"],
                candidate
            ])

        session.clear()

        return redirect("/thanks")

    return render_template(
        "headgirl.html",
        candidates=HEADGIRLS
    )

# =====================================
# THANK YOU
# =====================================

@app.route("/thanks")
def thanks():

    return render_template("thanks.html")

# =====================================
# LIVE RESULTS API
# =====================================

@app.route("/api/results")
def api_results():

    headboy = Counter()
    headgirl = Counter()

    total_votes = 0

    try:

        with open(
            CSV_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:

                total_votes += 1

                headboy[row["HEAD_BOY"]] += 1
                headgirl[row["HEAD_GIRL"]] += 1

    except Exception as e:

        print("API ERROR:", e)

    return jsonify({
        "total_votes": total_votes,
        "headboy": dict(headboy),
        "headgirl": dict(headgirl)
    })

# =====================================
# ADMIN DASHBOARD
# =====================================

@app.route("/admin")
def admin():

    return render_template("admin.html")

# =====================================
# RESET SESSION
# =====================================

@app.route("/reset")
def reset():

    session.clear()

    return redirect("/")

# =====================================
# RUN SERVER
# =====================================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False,
        threaded=True
    )