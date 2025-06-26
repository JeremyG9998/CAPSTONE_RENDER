import os
from flask import Flask, session, redirect, render_template
from routes.login_routes import login_routes 
from routes.stats_routes import stats_routes 
from routes.home_routes import home_routes
from routes.weather_type_routes import weather_type_routes 
from scripts.simulation import *
from database_layer import DB_PATH
import sqlite3

app = Flask(__name__) 
app.debug = True
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default_secret_key')
db_setup()

app.register_blueprint(login_routes, url_prefix='/')
app.register_blueprint(stats_routes, url_prefix='/')
app.register_blueprint(home_routes, url_prefix='/')
app.register_blueprint(weather_type_routes, url_prefix='/')

@app.route('/logout')
def logout():
    session.clear()  
    return redirect('/login')

@app.route('/home')
def home():
    user_id = session.get('user_id')
    if not user_id:
        return redirect('/login')
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
    user = cursor.fetchone()
    conn.close()

    if user:
        return render_template('home_templates/home.html', current_user=user)
    return redirect('/login')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

