import sqlite3
from scripts.DB_queries import * 
from database_layer import DB_PATH

def save_to_purchases_table(self):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM flavor_count ORDER BY id DESC LIMIT 1")
    flavor_count_id = cursor.fetchone()[0]
    cursor.execute("SELECT class_name FROM simulation_type_ref ORDER BY id DESC LIMIT 1")
    simulation_type_name = cursor.fetchone()[0]
    cursor.execute("SELECT period FROM truck_report ORDER BY period DESC LIMIT 1")
    truck_id = cursor.fetchone()[0]

    for flavor in self.results:
        cursor.execute(f"INSERT INTO purchases (flavor, flavor_count_id, simulation_type_name, truck_id) VALUES ('{flavor}', {flavor_count_id}, '{simulation_type_name}', {truck_id})")
    conn.commit()
    conn.close()

def save_to_flavors_count_table(self):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT class_name FROM simulation_type_ref ORDER BY id DESC LIMIT 1")
    simulation_type_name = cursor.fetchone()[0]

    cursor.execute(f"""
        INSERT INTO flavor_count (lava, hot_fudge, blizzard, chocolate, vanilla, simulation_type_name)
        VALUES ({self.lava}, {self.hot_fudge}, {self.blizzard}, {self.chocolate}, {self.vanilla}, '{simulation_type_name}')
    """)
    conn.commit()
    conn.close()

def save_simulation_type(self):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(f"""
        INSERT INTO simulation_type (class_name, lava, hot_fudge, blizzard, chocolate, vanilla)
        VALUES ('{self.__class__.__name__}', {self.lava}, {self.hot_fudge}, {self.blizzard}, {self.chocolate}, {self.vanilla})
        ON CONFLICT(class_name) 
        DO UPDATE SET 
            lava = lava + {self.lava},
            hot_fudge = hot_fudge + {self.hot_fudge},
            blizzard = blizzard + {self.blizzard},
            chocolate = chocolate + {self.chocolate},
            vanilla = vanilla + {self.vanilla}
    """)
    conn.commit()
    conn.close()

def save_truck_report():
    data = truck_report_logic()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for row in data:
        cursor.execute(f"""
            INSERT INTO truck_report (period, start_day, end_day, lava, hot_fudge, blizzard, chocolate, vanilla)
            VALUES ({row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}, {row[6]}, {row[7]})
            ON CONFLICT(period) DO UPDATE SET
                start_day = {row[1]},
                end_day = {row[2]},
                lava = {row[3]},
                hot_fudge = {row[4]},
                blizzard = {row[5]},
                chocolate = {row[6]},
                vanilla = {row[7]}
        """)
    conn.commit()
    conn.close()

def save_total_purchases(self):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute(f"""
        INSERT INTO total_purchases (id, lava, hot_fudge, blizzard, chocolate, vanilla)
        VALUES (1, {self.lava}, {self.hot_fudge}, {self.blizzard}, {self.chocolate}, {self.vanilla})
        ON CONFLICT(id) DO UPDATE SET
            lava = total_purchases.lava + {self.lava},
            hot_fudge = total_purchases.hot_fudge + {self.hot_fudge},
            blizzard = total_purchases.blizzard + {self.blizzard},
            chocolate = total_purchases.chocolate + {self.chocolate},
            vanilla = total_purchases.vanilla + {self.vanilla}
    """)
    conn.commit()
    conn.close()

def save_simulation_type_ref(self):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(f"""
        INSERT INTO simulation_type_ref (class_name)
        VALUES ('{self.__class__.__name__}')
    """)    
    conn.commit()
    conn.close()

def insert_feedback(message):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(f"""
        INSERT INTO feedback (message)
        VALUES ('{message}')
    """)
    conn.commit()
    conn.close()