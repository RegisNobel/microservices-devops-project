import requests
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    email = request.form["email"]
    response = requests.post(
        "http://storage_service:5001/store-email", json={"name": name, "email": email}
    )
    if response.status_code == 200:
        return redirect("/")
    else:
        return "Error in email storage", 400


@app.route("/admin")
def admin(email_sent=0):
    response = requests.get("http://storage_service:5001/admin")
    if response.status_code == 200:
        return render_template(
            "admin.html", email_list=response.json(), email_snt=email_sent
        )
    elif response.status_code == 404:
        return render_template("admin.html", email_snt=email_sent)
    else:
        return "Error in fetching emails", 400


@app.route("/update", methods=["GET", "POST"])
def update():
    data = request.form
    id = data["id"]
    new_name = data["new_name"]
    new_email = data["new_email"]

    response = requests.post(
        "http://storage_service:5001/update",
        json={"id": id, "new_name": new_name, "new_email": new_email},
    )
    if response.status_code == 200:
        return redirect("/admin")
    else:
        return "Error in updating data", 400


@app.route("/delete", methods=["POST"])
def delete():
    data = request.form
    id = data["id"]

    response = requests.post("http://storage_service:5001/delete", json={"id": id})
    if response.status_code == 200:
        return redirect("/admin")
    else:
        return "Error in deleting data", 400


@app.route("/sendemail", methods=["POST"])
def send_email():
    data = request.form
    to = data["email"]
    subject = "Test Email"
    body = "This is a test email"

    try:
        response = requests.post(
            "http://auto_mail_service:5002/sendemail",
            json={"to": to, "subject": subject, "body": body},
        )
        if response.status_code == 200:
            return admin(email_sent=1)
        else:
            return admin(email_sent=2)
    except Exception as e:
        return admin(email_sent=2)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
