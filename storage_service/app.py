from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://appuser:password@localhost/email_list'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    def serialize(self):
        return {'id': self.id, 'name': self.name, 'email': self.email}

with app.app_context():
    db.create_all()


@app.route('/store-email', methods=['POST'])
def store_email():
    name = request.json['name']
    email = request.json['email']
    new_user = User(name=name, email=email)
    db.session.add(new_user)
    db.session.commit()
    return "Email stored successfully", 200

@app.route('/update', methods=['POST'])
def update_email():
    id = request.json['id']
    new_name = request.json['new_name']
    new_email = request.json['new_email']
    user = User.query.filter_by(id=id).first()
    user.id = id
    user.name = new_name
    user.email = new_email
    
    db.session.commit()
    return "Email updated successfully", 200


@app.route('/admin', methods=['GET'])
def get_list():
    email_list = User.query.all()
    if email_list:
        return jsonify([user.serialize() for user in email_list]), 200
    else:
        return "No emails found", 404

if __name__ == "__main__":
    app.run(port=5001, debug=True)
