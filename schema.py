from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date

db = SQLAlchemy()

class License(db.Model):
    __tablename__ = 'licenses'

    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(32), nullable=False)
    serial = db.Column(db.String(64), unique=True, nullable=False) 
    firmware_version = db.Column(db.String(16), nullable=False)
    valid_until = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<License {self.serial}>'
