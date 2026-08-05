# Job Application Tracker

A Python job application tracker with a command-line interface and Flask REST API. It supports creating, viewing, updating and deleting applications, with local JSON persistence.

## Features

- Add job applications
- View saved applications
- Update an application status
- Delete applications
- Save application data between sessions
- Access application data through a REST API
- Validate missing or incorrect input
- Return suitable HTTP error responses

## Technical overview

- Python command-line interface
- Flask REST API
- GET, POST, PATCH and DELETE endpoints
- JSON persistence for local application data
- Input and request validation
- pytest tests for API responses

## Run the command-line application

Python 3 is required.

```bash
python main.py
```

On Windows, this can also be run with:

```bash
py main.py
```

Application data is stored locally in `applications.json`, which is excluded from version control.

## Run the Flask API

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it with Git Bash:

```bash
source .venv/Scripts/activate
```

Install the required packages:

```bash
python -m pip install -r requirements.txt
```

Start the API:

```bash
python -m flask --app app run --debug
```

The API runs at:

```text
http://127.0.0.1:5000
```

## API endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/applications` | View all applications |
| GET | `/applications/1` | View one application |
| POST | `/applications` | Add an application |
| PATCH | `/applications/1` | Update an application status |
| DELETE | `/applications/1` | Delete an application |

## Run the tests

```bash
python -m pytest
```

The tests check the home endpoint, the applications response and the response for an unknown application.
