from src.models.users import Users

from config.db.pool import db

with db:
    db.create_tables([Users])
