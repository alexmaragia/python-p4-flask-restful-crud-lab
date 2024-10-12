#!/usr/bin/env python3

from app import app
from models import db, Plant

def seed_database():
    with app.app_context():
        print("Clearing database...")
        Plant.query.delete()

        print("Seeding plants...")
        aloe = Plant(
            id=1,
            name="Aloe",
            image="./images/aloe.jpg",
            price=11.50,
            is_in_stock=True,
        )

        zz_plant = Plant(
            id=2,
            name="ZZ Plant",
            image="./images/zz-plant.jpg",
            price=25.98,
            is_in_stock=False,
        )

        db.session.add_all([aloe, zz_plant])
        db.session.commit()

        print("Database seeded!")

if __name__ == "__main__":
    seed_database()