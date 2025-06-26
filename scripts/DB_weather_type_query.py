import sqlite3
from database_layer import DB_PATH

def winter_HT_query():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT lava, hot_fudge, blizzard, chocolate, vanilla
        FROM simulation_type
        WHERE class_name = 'WinterHT'
    """)
    data = cursor.fetchone()
    conn.close()
    return data

def winter_LT_query():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT lava, hot_fudge, blizzard, chocolate, vanilla
        FROM simulation_type
        WHERE class_name = 'WinterLT'
    """)
    data = cursor.fetchone()
    conn.close()
    return data

def winter_HP_query():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT lava, hot_fudge, blizzard, chocolate, vanilla
        FROM simulation_type
        WHERE class_name = 'WinterHP'
    """)
    data = cursor.fetchone()
    conn.close()
    return data

def winter_LP_query():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT lava, hot_fudge, blizzard, chocolate, vanilla
        FROM simulation_type
        WHERE class_name = 'WinterLP'
    """)
    data = cursor.fetchone()
    conn.close()
    return data

def winter_HPHT_query():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT lava, hot_fudge, blizzard, chocolate, vanilla
        FROM simulation_type
        WHERE class_name = 'WinterHPHT'
    """)
    data = cursor.fetchone()
    conn.close()
    return data

def winter_LPLT_query():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT lava, hot_fudge, blizzard, chocolate, vanilla
        FROM simulation_type
        WHERE class_name = 'WinterLPLT'
    """)
    data = cursor.fetchone()
    conn.close()
    return data

def summer_HT_query():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT lava, hot_fudge, blizzard, chocolate, vanilla
        FROM simulation_type
        WHERE class_name = 'SummerHT'
    """)
    data = cursor.fetchone()
    conn.close()
    return data

def summer_LT_query():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT lava, hot_fudge, blizzard, chocolate, vanilla
        FROM simulation_type
        WHERE class_name = 'SummerLT'
    """)
    data = cursor.fetchone()
    conn.close()
    return data

def summer_HP_query():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT lava, hot_fudge, blizzard, chocolate, vanilla
        FROM simulation_type
        WHERE class_name = 'SummerHP'
    """)
    data = cursor.fetchone()
    conn.close()
    return data

def summer_LP_query():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT lava, hot_fudge, blizzard, chocolate, vanilla
        FROM simulation_type
        WHERE class_name = 'SummerLP'
    """)
    data = cursor.fetchone()
    conn.close()
    return data

def summer_HPHT_query():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT lava, hot_fudge, blizzard, chocolate, vanilla
        FROM simulation_type
        WHERE class_name = 'SummerHPHT'
    """)
    data = cursor.fetchone()
    conn.close()
    return data

def summer_LPLT_query():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT lava, hot_fudge, blizzard, chocolate, vanilla
        FROM simulation_type
        WHERE class_name = 'SummerLPLT'
    """)
    data = cursor.fetchone()
    conn.close()
    return data

def normal_HT_query():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT lava, hot_fudge, blizzard, chocolate, vanilla
        FROM simulation_type
        WHERE class_name = 'NormalHT'
    """)
    data = cursor.fetchone()
    conn.close()
    return data

def normal_LT_query():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT lava, hot_fudge, blizzard, chocolate, vanilla
        FROM simulation_type
        WHERE class_name = 'NormalLT'
    """)
    data = cursor.fetchone()
    conn.close()
    return data

def normal_HP_query():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT lava, hot_fudge, blizzard, chocolate, vanilla
        FROM simulation_type
        WHERE class_name = 'NormalHP'
    """)
    data = cursor.fetchone()
    conn.close()
    return data

def normal_LP_query():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT lava, hot_fudge, blizzard, chocolate, vanilla
        FROM simulation_type
        WHERE class_name = 'NormalLP'
    """)
    data = cursor.fetchone()
    conn.close()
    return data

def normal_HPHT_query():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT lava, hot_fudge, blizzard, chocolate, vanilla
        FROM simulation_type
        WHERE class_name = 'NormalHPHT'
    """)
    data = cursor.fetchone()
    conn.close()
    return data

def normal_LPLT_query():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT lava, hot_fudge, blizzard, chocolate, vanilla
        FROM simulation_type
        WHERE class_name = 'NormalLPLT'
    """)
    data = cursor.fetchone()
    conn.close()
    return data