# Pupil Finder Web App

**Pupil Finder** is a web-based application for locating pupils within a school timetable. Built using **Flask** for the backend and **Jinja2/HTML/CSS** for the frontend, the app provides a clean and interactive interface for staff to quickly find pupil locations.

---

## Features

- Search pupils by **full name** (case-sensitive).  
- Select **day of the week** to view timetable sessions.  
- Displays **session, subject, start and end times, and location** in a structured table.  
- Highlights the pupil’s **current session(s)** automatically based on system time.  
- **New Search** button clears the form and results for another query.  
- School logo displayed at the **top-right** for easy branding.

---

## Tech Stack

- **Backend:** Python, Flask  
- **Frontend:** HTML, CSS, Jinja2 templates  
- **Data Storage:** CSV files (`ClassData.csv`, `Monday.csv` … `Friday.csv`)  
- **Styling:** Responsive layout with table highlighting  

---

## Folder Structure

```bash
project-root/
├── app.py                  # Flask backend
├── ClassData.csv           # Pupil data
├── Monday.csv              # Timetable CSVs
├── Tuesday.csv
├── Wednesday.csv
├── Thursday.csv
├── Friday.csv
├── templates/
│   └── index.html          # Main HTML template
└── static/
    └── images/
        └── avenue_house.gif  # School logo
```
### Getting Started
Prerequisites:
- Python 3.9 or later
- pip

### Installation
Clone the repository:
```bash
git clone https://github.com/NicolaJB/Pupil-Finder-Web-App.git
cd Pupil-Finder-Web-App
```
### Install dependencies:
```bash
pip install Flask

### Running the App
On macOS/Linux:
```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```
On Windows (Command Prompt):
```bash
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
```
The app will be available at: http://127.0.0.1:5000
### Usage
Enter the pupil’s full name in the input field.

Select the day to query.

Click Find Location to see the pupil’s timetable sessions.

The current session(s) will be highlighted automatically.

Click New Search to clear the form and perform another query.

### CSV Data Format
ClassData.csv
```csv
Pupil Name,Year
Alice Smith,7
Bob Jones,8
```
Timetable CSVs (Monday.csv, Tuesday.csv, …)
```csv
Year,Start,Subject,Session,Location,End
7,09:00,Math,1,Room 101,09:50
8,09:00,English,1,Room 102,09:50
```
### Notes
- Pupil name search is case-sensitive.
- Maximum session number is 11 (configurable via CSV).
- Ensure all CSV files are present in the root folder for correct functionality.

### License
This project is licensed under the MIT License.