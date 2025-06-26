import sqlite3
from database_layer import DB_PATH

def flavor_counts_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM flavor_count")
    flavor_data = cursor.fetchall()
    conn.close()
    return flavor_data

def get_last_flavor_count():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM flavor_count ORDER BY id DESC LIMIT 1")
    last_entry = cursor.fetchone()  
    conn.close()
    return last_entry

def get_day_number():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(id) FROM flavor_count")
    result = cursor.fetchone()
    
    if result[0] is None:
        day_number = 1
    else:
        day_number = result[0] + 1    
    conn.close()
    return day_number

def truck_report_logic():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT
            CEIL(id / 10.0) AS period,
            MIN(id) AS start_day,
            MAX(id) AS end_day,
            SUM(lava) AS lava,
            SUM(hot_fudge) AS hot_fudge,
            SUM(blizzard) AS blizzard,
            SUM(chocolate) AS chocolate,
            SUM(vanilla) AS vanilla
        FROM flavor_count
        GROUP BY period
        ORDER BY period
    """)
    totals = cursor.fetchall()
    conn.close()
    return totals

def total_purchases_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM total_purchases")
    flavor_data = cursor.fetchall()
    conn.close()
    return flavor_data

def total_flavor_counts_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT
            lava,
            hot_fudge,
            blizzard,
            chocolate,
            vanilla
        FROM total_purchases
    """)
    totals = cursor.fetchone() 
    conn.close()
    return totals  

def average_purchases():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT 
            AVG(lava), AVG(hot_fudge), AVG(blizzard), AVG(chocolate), AVG(vanilla)
        FROM flavor_count
    """)
    data = cursor.fetchone()
    conn.close()
    return data

def average_truck_order_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            AVG(lava), AVG(hot_fudge), AVG(blizzard), AVG(chocolate), AVG(vanilla)
        FROM truck_report
    """)
    data = cursor.fetchone()
    conn.close()
    return data

def avg_customer_simulation_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT AVG(lava), AVG(hot_fudge), AVG(blizzard), AVG(chocolate), AVG(vanilla)
        FROM simulation_type
        WHERE class_name = 'CustomerSimulation'
    """)
    data = cursor.fetchone()
    conn.close()
    return data

def summer_data_query():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT * 
        FROM simulation_type
        WHERE class_name IN ('Summer', 'SummerHT', 'SummerLT', 'SummerHP', 'SummerLP', 'SummerHPHT', 'SummerLPLT')
    """)
    data = cursor.fetchall()
    conn.close()
    return data

def winter_data_query():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT * 
        FROM simulation_type
        WHERE class_name IN ('Winter', 'WinterHT', 'WinterLT', 'WinterHP', 'WinterLP', 'WinterHPHT', 'WinterLPLT')
    """)
    data = cursor.fetchall()
    conn.close()
    return data

def normal_data_query():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT * 
        FROM simulation_type
        WHERE class_name IN ('CustomerSimulation', 'NormalLP', 'NormalHP', 'NormalHT', 'NormalLT', 'NormalHPHT', 'NormalLPLT')
    """)
    data = cursor.fetchall()
    conn.close()
    return data

def customer_simulation_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT SUM(lava), SUM(hot_fudge), SUM(blizzard), SUM(chocolate), SUM(vanilla)
        FROM simulation_type
        WHERE class_name IN ('CustomerSimulation', 'NormalLP', 'NormalHP', 'NormalHT', 'NormalLT', 'NormalHPHT', 'NormalLPLT')
    """)
    totals = cursor.fetchone()
    conn.close()
    return totals

def summer_simulation_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT SUM(lava), SUM(hot_fudge), SUM(blizzard), SUM(chocolate), SUM(vanilla)
        FROM simulation_type
        WHERE class_name IN ('Summer', 'SummerHT', 'SummerLT', 'SummerHP', 'SummerLP', 'SummerHPHT', 'SummerLPLT')
    """)
    totals = cursor.fetchone()
    conn.close()
    return totals

def winter_simulation_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT SUM(lava), SUM(hot_fudge), SUM(blizzard), SUM(chocolate), SUM(vanilla)
        FROM simulation_type
        WHERE class_name IN ('Winter', 'WinterHT', 'WinterLT', 'WinterHP', 'WinterLP', 'WinterHPHT', 'WinterLPLT')
    """)
    totals = cursor.fetchone()
    conn.close()
    return totals