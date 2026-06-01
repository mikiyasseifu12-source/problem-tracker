# Problem Tracker API

A full stack web application for tracking problems and tasks. Built with Flask, SQLite, and vanilla JavaScript.

## Live Demo
- **API:** https://problem-tracker-vkli.onrender.com
- **Frontend:** Open index.html in your browser

## Features
- Add new problems
- View all problems
- Mark problems as solved or unsolved
- Delete problems

## Tech Stack
- **Backend:** Python, Flask, Flask-SQLAlchemy, Flask-CORS
- **Database:** SQLite
- **Frontend:** HTML, CSS, JavaScript
- **Deployment:** Render

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /problems | Get all problems |
| POST | /problems | Add a new problem |
| PUT | /problems/<id> | Update a problem |
| DELETE | /problems/<id> | Delete a problem |

## Run Locally
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `python app.py`
4. Open `http://127.0.0.1:5000`

## Author
Mikiyas Seifu — CS Student at Addis Ababa University