import sqlite3
import os

DB_PATH = os.environ.get('DATABASE_URL', '/tmp/site.db')

def db_setup():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_name VARCHAR(20) UNIQUE NOT NULL,
            email VARCHAR(20) UNIQUE NOT NULL,
            password VARCHAR(20) NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS purchases (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            flavor TEXT,
            flavor_count_id INTEGER,
            simulation_type_name TEXT,
            truck_id INT,
            FOREIGN KEY (flavor_count_id) REFERENCES flavor_count(id),
            FOREIGN KEY (simulation_type_name) REFERENCES simulation_type_ref(class_name),
            FOREIGN KEY (truck_id) REFERENCES truck_report(period)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS flavor_count (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            lava INT, hot_fudge INT, blizzard INT, chocolate INT, vanilla INT,
            simulation_type_name TEXT,
            FOREIGN KEY (simulation_type_name) REFERENCES simulation_type_ref(class_name)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS simulation_type (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            class_name TEXT UNIQUE,
            lava INT, hot_fudge INT, blizzard INT, chocolate INT, vanilla INT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS truck_report (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            period INT UNIQUE, start_day INT, end_day INT,
            lava INT, hot_fudge INT, blizzard INT, chocolate INT, vanilla INT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS total_purchases (
            id INTEGER PRIMARY KEY, 
            lava INT, hot_fudge INT, blizzard INT, chocolate INT, vanilla INT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS simulation_type_ref (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            class_name TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()