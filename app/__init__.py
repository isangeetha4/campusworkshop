"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgrq5q1mbg5e4khqr330-a.oregon-postgres.render.com",
        database="todo_pqmv",
        user="root",
        password="RGp1ngIa8aAxGqj75Bd9tfWA3wb8WHeU")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
