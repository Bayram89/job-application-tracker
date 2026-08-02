# Job Application Tracker

A simple command-line app I've made while learning Python.

## What it can do

- Add a job application
- Show saved applications
- Update an application status
- Delete an application
- Save applications in a JSON file

## What I especially practiced with

- Variables and user input
- If and else conditions
- Lists and dictionaries
- While and for loops
- Functions
- Reading and writing a JSON file
- Basic input checking

## Run the project

Make sure Python is installed.

Run `py main.py`.

The application data is saved locally in `applications.json`. This very file is not uploaded to GitHub.

## Flask API

I also wanted to add this project a simple Flask API.

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