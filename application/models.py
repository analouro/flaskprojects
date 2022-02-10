from application import db

class Task (db.Model):
    id_task = db.Column(db.Integer, primary_key=True)
    name_task = db.Column(db.String(300), nullable=False)
    status_task = db.Column(db.String(20), default=False)


