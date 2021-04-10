import os
from dotenv import load_dotenv
load_dotenv()
"""Add products categories"""
Categories = [
    'Chocolate',
    'Pizza',
    'Drink',
    'Cheese',
]
"""Use environment variables to the DB connection"""
DB_USER = os.environ.get("DB_USER")
DB_NAME = os.environ.get("DB_NAME")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_HOST = os.environ.get("DB_HOST")
