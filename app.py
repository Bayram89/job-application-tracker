import json

from flask import Flask, request

app = Flask(__name__)


def load_applications():
    try:
        with open("applications.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_applications(application_list):
    with open("applications.json", "w") as file:
        json.dump(application_list, file)


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

@app.route("/applications", methods=["POST"])
def create_application():
    data = request.get_json()

    company = data.get("company")
    position = data.get("position")
    status = data.get("status")

    if not company or not position or not status:
        return {"error": "Company, position and status are required"}, 400

    application = {
        "company": company,
        "position": position,
        "status": status
    }

    applications = load_applications()
    applications.append(application)
    save_applications(applications)

    return application, 201