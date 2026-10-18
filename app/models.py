from app.extensions import db


class Resource(db.Model):

    __tablename__ = "resources"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    category = db.Column(db.String(50), nullable=False)

    total_units = db.Column(db.Integer, nullable=False)

    available_units = db.Column(db.Integer, nullable=False)