import requests
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    
    response = requests.post('http://localhost:5001/store-email', json={'name': name, 'email': email})
    if response.status_code == 200:
        return redirect('/')
    else:
        return "Error in email storage", 400
    
@app.route('/admin')
def admin():
    response = requests.get('http://localhost:5001/admin')
    if response.status_code == 200:
        return render_template('admin.html', email_list = response.json())
    elif response.status_code == 404:
        return render_template('admin.html')
    else:
        return "Error in fetching emails", 400

if __name__ == "__main__":
    app.run(port=5000, debug=True)


