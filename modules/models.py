from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import date
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Exp1(db.Model):
    __tablename__ = 'exp1'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    shift = db.Column(db.String(10), nullable=False)
    master = db.Column(db.String(100), nullable=False)
    output = db.Column(db.Float, nullable=False)
    operator_count = db.Column(db.Integer, nullable=False)

class Exp2(db.Model):
    __tablename__ = 'exp2'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    shift = db.Column(db.String(10), nullable=False)
    master = db.Column(db.String(100), nullable=False)
    output = db.Column(db.Float, nullable=False)
    operator_count = db.Column(db.Integer, nullable=False)

class Exp3(db.Model):
    __tablename__ = 'exp3'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    shift = db.Column(db.String(10), nullable=False)
    master = db.Column(db.String(100), nullable=False)
    output = db.Column(db.Float, nullable=False)
    operator_count = db.Column(db.Integer, nullable=False)

if __name__ == '__main__':
    if os.path.exists("db.db"):
        os.remove("db.db")

    with app.app_context():
        try:
            db.create_all()
            print("✅ Таблицы успешно созданы.")
        except Exception as e:
            print("❌ Ошибка при создании таблиц:", e)

    app.run(debug=True)
