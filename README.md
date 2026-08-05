# Job Application Tracker

A Python job application tracker with a command-line interface and Flask REST API. It supports creating, viewing, updating and deleting applications, with local JSON persistence.

## What it can do

- Add a job application
- Show saved applications
- Update an application status
- Delete an application
- Save applications in a JSON file

- ## Technical overview

- Python command-line interface for managing applications
- Flask REST API with GET, POST, PATCH and DELETE endpoints
- JSON persistence for local application data
- Request validation and HTTP error responses
- pytest tests for API responses

## Run the project

Make sure Python is installed.

Run `py main.py`.

The application data is saved locally in `applications.json`. This very file is not uploaded to GitHub.

## Flask API

The project also provides a Flask REST API for managing applications through HTTP requests.

Create and activate a virtual environment:

`py -m venv .venv`

`source .venv/Scripts/activate`

Install the packages:

`python -m pip install -r requirements.txt`

Start the API:

`python -m flask --app app run --debug`

The API runs at `http://127.0.0.1:5000`.

## API endpoints

- `GET /applications` shows all applications
- `GET /applications/1` shows application number 1
- `POST /applications` adds an application
- `PATCH /applications/1` updates application number 1
- `DELETE /applications/1` deletes application number 1

## Tests

Run the tests with:

`python -m pytest`
