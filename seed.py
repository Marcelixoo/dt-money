from app import create_app, config, db

app = create_app(config)

with app.app_context():
    db.create_all()
