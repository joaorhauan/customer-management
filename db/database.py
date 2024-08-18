import os
from peewee import PostgresqlDatabase
from dotenv import load_dotenv

load_dotenv()

databaseURI = os.getenv('DATABASE_URI', '')

db = PostgresqlDatabase(databaseURI)