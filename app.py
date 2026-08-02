import json

from flask import Flask

app = Flask(__name__)


def load_applications():
    try:
        with open("applications.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


@app.route("/")
def home():
    return {"message": "Job Application Tracker API"}


@app.route("/applications")
def get_applications():
    return load_applications()

@app.route("/applications/<int:application_number>")
def get_application(application_number):
    applications = load_applications()

    if application_number >= 1 and application_number <= len(applications):
        return applications[application_number - 1]

    return {"error": "Application not found"}, 404