from flask import Flask
from config import Config
from schema import db, License
from datetime import datetime, timedelta, timezone

#define data (fake..)
model = 'ModelA'
serial = 'ABC123456789'
firmware_version = 'v1.0.0'
valid_until = datetime.now(timezone.utc).date() + timedelta(days=365)

# Flask setting
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    #check duplication license key value
    existing = License.query.filter_by(serial=serial).first()
    if existing:
        print(f"Delete existing license values: {existing.serial}")
        db.session.delete(existing)
        db.session.commit()

    #create new license key
    new_license = License(
        model=model,
        serial=serial,
        firmware_version=firmware_version,
        valid_until=valid_until
    )

    db.session.add(new_license)
    db.session.commit()
    print(f"Create New license key value!: {serial}")

    #print database information 
    print("current license value:")
    all_licenses = License.query.all()
    for lic in all_licenses:
        print(f" - [{lic.id}] {lic.model} / {lic.serial} / {lic.firmware_version} / valid_time : {lic.valid_until}")
