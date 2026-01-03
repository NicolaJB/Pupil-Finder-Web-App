from flask import Flask, render_template, request
import csv
import logging
import os
from datetime import datetime

# Logging setup
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

app = Flask(__name__)

# Get base directory for CSV files
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]


# Load pupils data from CSV
def load_pupils():
    pupils = {}
    csv_path = os.path.join(BASE_DIR, 'ClassData.csv')
    try:
        with open(csv_path, encoding='latin-1') as fh:
            reader = csv.reader(fh)
            for k, v in reader:
                pupils[k] = v
        log.info(f"Loaded {len(pupils)} pupils from ClassData.csv")
    except FileNotFoundError:
        log.error(f"ClassData.csv not found at {csv_path}")
    return pupils


# Load timetable for a given day
def get_timetable(day):
    csv_path = os.path.join(BASE_DIR, f"{day}.csv")
    try:
        with open(csv_path, encoding='latin-1') as fh:
            reader = csv.reader(fh)
            timetable = list(reader)
            log.info(f"Loaded timetable for {day} with {len(timetable)} entries.")
            return timetable
    except FileNotFoundError:
        log.error(f"{day}.csv not found at {csv_path}")
        return []


# Extract all start times for dropdown
def get_start_times(timetable):
    times = sorted({row[1] for row in timetable if len(row) > 1})
    return times


# Check if current system time is within a session
def is_current_session(start_time, end_time):
    try:
        now = datetime.now().strftime("%H:%M")
        return start_time <= now <= end_time
    except:
        return False


# Locate pupil for the day, mark current sessions
def locate_pupil_by_time(pupil_name, pupil_year, timetable, day):
    results = []
    for each in timetable:
        if len(each) > 5 and each[0] == pupil_year:
            result = {
                "day": day,
                "name": pupil_name,
                "year": pupil_year,
                "subject": each[2],
                "start": each[1],
                "end": each[5],
                "location": each[4],
                "session": each[3],
                "current": is_current_session(each[1], each[5])
            }
            results.append(result)

    if not results:
        results.append({"error": f"No pupil sessions found on {day}."})

    return results


# Determine current weekday for default selection
def get_current_weekday():
    weekday_index = datetime.today().weekday()  # Monday=0, Sunday=6
    if weekday_index < 5:
        return DAYS[weekday_index]
    return DAYS[0]


@app.route("/", methods=["GET", "POST"])
def index():
    pupils = load_pupils()
    selected_day = get_current_weekday()
    pupil_name = ""
    results = []

    if request.method == "POST":
        pupil_name = request.form.get("pupil_name", "").strip()
        selected_day = request.form.get("day", selected_day)

    pupil_year = pupils.get(pupil_name)
    timetable = get_timetable(selected_day)

    if pupil_year:
        results = locate_pupil_by_time(pupil_name, pupil_year, timetable, selected_day)

    time_options = get_start_times(timetable)

    return render_template(
        "index.html",
        days=DAYS,
        results=results,
        selected_day=selected_day,
        pupil_name=pupil_name,
        time_options=time_options
    )


@app.route("/health")
def health():
    """Health check endpoint for Render"""
    return {
               "status": "healthy",
               "service": "Pupil Finder",
               "timestamp": datetime.now().isoformat()
           }, 200


if __name__ == "__main__":
    # Production-ready configuration
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_ENV") == "development"
    app.run(host="0.0.0.0", port=port, debug=debug)