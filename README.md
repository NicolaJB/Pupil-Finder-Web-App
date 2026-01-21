# Pupil Finder Web App

Pupil Finder is a web-based application for locating pupils within a school timetable. Built using Flask for the backend and Jinja2/HTML/CSS for the frontend, the app provides a clean and interactive interface for staff to quickly find pupil locations.

## Features
- Search pupils by full name (case-sensitive)
- Select day of the week to view timetable sessions
- Filter by session - View all sessions or select a specific session (1-11)
- Displays session, subject, start and end times, and location in a structured table
- Automatically highlights current session(s) based on system time (yellow background + "(NOW)" indicator)
- New Search button clears the form and results for another query
- School logo displayed at the top-right for easy branding

## Tech Stack
- Backend: Python 3.11+, Flask 3.0
- Frontend: HTML5, CSS3, Jinja2 templates
- Data Storage: CSV files (ClassData.csv, Monday.csv … Friday.csv)
- Styling: Responsive layout with current session highlighting
- Deployment: Render-ready with Gunicorn

## Folder Structure
```bash
pupil-finder/
├── app.py                  # Flask backend
├── requirements.txt        # Python dependencies
├── render.yaml             # Render deployment config
├── ClassData.csv           # Pupil data
├── Monday.csv              # Monday timetable
├── Tuesday.csv             # Tuesday timetable
├── Wednesday.csv           # Wednesday timetable
├── Thursday.csv            # Thursday timetable
├── Friday.csv              # Friday timetable
├── templates/
│   └── index.html          # Main HTML template
└── static/
    └── images/
        └── avenue_house.gif  # School logo
```
## Getting Started
Prerequisites:
- Python 3.9 or later
- pip or pip3

### Installation
Clone the repository:
```bash
git clone https://github.com/NicolaJB/Pupil-Finder-Web-App.git
cd Pupil-Finder-Web-App
```
### Install dependencies:
```bash
pip3 install -r requirements.txt
````
### Running the App

Running the App locally in development mode:
```bash
python3 app.py
````
Production mode with Gunicorn:
```bash
gunicorn app:app --bind 0.0.0.0:5000
````
The app will be available at: http://127.0.0.1:5000

### Health Check
The app includes a /health endpoint for monitoring:
```bash
curl https://your-app.onrender.com/health
```
Response:
```bash
json{
  "status": "healthy",
  "service": "Pupil Finder",
  "timestamp": "2026-01-03T11:30:00.000000"
}
````
### Usage

**Basic Search:**
- Enter the pupil's full name in the input field (e.g., "Daniel Morris")
- Select the day of the week (defaults to current day if working weekday)
- Click "Find Location" to see all timetable sessions
- Current timetable session will be highlighted in yellow with a (NOW) indicator

**Session Filtering:**
- After entering pupil name and selecting day
- Select a specific session from the dropdown (or leave as "All Sessions")
- Click "Find Location"
- Results will show:
  - "All Sessions" - Full timetable with current session highlighted
  - Specific session - Only that session, highlighted if current

**New Search**
- Click "New Search" to clear the form and start over

### CSV Data Format

**ClassData.csv**

Maps pupil names to their year group:
```csv
Pupil Name,Year
Daniel Morris,5
Reika Tanaka,8
```
**Timetable CSVs (Monday.csv, Tuesday.csv, …)**

Each day has a separate CSV with session details:
```csv
Year,Start,Subject,Session,Location,End
7,09:00,Math,1,Room 101,09:50
8,09:00,English,1,Room 102,09:50
```
Column Details:
- Year - Student year group (matches ClassData.csv)
- Start - Session start time (HH:MM format)
- Subject - Subject name
- Session - Session number (1-11)
- Location - Room/location name
- End - Session end time (HH:MM format)

## Features in Detail
**Current Session Detection**

The app automatically detects which session is currently active based on:
- Current system time (highlights in yellow if the time is current, regardless of day)
- Session start and end times in the CSV

**Error Handling**

The app provides helpful error messages:
- "No pupil sessions found on Monday" - Pupil has no classes that day
- "No session 11 found for this pupil on Friday" - Pupil doesn't have that session

**Configuration**

Environment Variables (Optional):

- PORT - Server port (default: 5000)
- FLASK_ENV - Environment mode (development/production)

**Customisation**
- Session highlighting: Modify is_current_session() in app.py
- School logo: Replace static/images/avenue_house.gif
- Styling: Edit CSS in templates/index.html
- Maximum sessions: Configure via CSV data (supports 1-11+)

## Troubleshooting

Port 5000 already in use:
```bash
Kill process on port 5000
kill -9 $(lsof -ti:5000)
```
Or, use a different port:
```bash
gunicorn app:app --bind 0.0.0.0:8000
```
**CSV files not found**

Ensure CSV files are in the same directory as app.py and use proper encoding:
```python
with open('ClassData.csv', encoding='latin-1') as fh:
    # ...
```
**Python 2.7 errors**

This app requires Python 3. Use python3 and pip3:
```bash
python3 --version  # Should show 3.9+
pip3 install -r requirements.txt
```
**Session dropdown is empty**

The dropdown populates from CSV data. Ensure your timetable CSVs have a "Session" column with values like "1", "2", "3", etc.

## Development
**Local Testing**
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### Install dependencies
pip3 install -r requirements.txt

### Run tests
python3 app.py

### Test health endpoint
curl http://localhost:5000/health

## Notes
- Pupil name search is case-sensitive.
- Maximum session number is 11 (configurable via CSV).
- Ensure all CSV files are present in the root folder for correct functionality.

## Deployment / Live Demo

The Pupil Finder Web App is deployed online via multiple cloud platforms:

- **Azure Web App:** [Access here](https://pupil-finder-azure-e5cne3bxfdf3h5c7.germanywestcentral-01.azurewebsites.net/)

— deployed via GitHub Actions using `gunicorn app:app --bind 0.0.0.0:$PORT --workers 1 --timeout 120`.

- **Render Web App:** [Access here](https://pupil-finder.onrender.com/)

 — configured for production with Gunicorn and Python 3.11.

Both deployments use a production-grade Gunicorn server, demonstrating cloud-ready Python/Flask application design with CI/CD and scalable hosting.

## License
This project is licensed under the MIT License.
