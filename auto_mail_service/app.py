from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os


app = Flask(__name__)
load_dotenv('.env')

@app.route('/sendemail', methods=['POST'])
def send_email():
    data = request.json
    sender = data.get('from', 'koudouva@gmail.com')
    recipient = data['to']
    subject = data['subject']
    body = data['body']
   

    # Create message
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    

    try:
        # Setup server with Gmail
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, os.getenv('EMAIL_SERVER_PASS')) # used environment variable for password
        server.sendmail(sender, recipient, msg.as_string())
        server.quit()
        return jsonify({'message': 'Email sent successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5002)