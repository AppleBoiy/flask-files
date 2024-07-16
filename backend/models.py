from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(150), nullable=False)
    users = db.Column(db.String(150), nullable=False)  # Comma-separated list of users

    def __repr__(self):
        return f'<File {self.filename}>'

    def owners(self):
        return self.users.split(',')
