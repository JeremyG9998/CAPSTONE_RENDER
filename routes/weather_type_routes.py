from flask import Blueprint, render_template
from scripts.charts.winter_charts.winter_HT_chart import *
from scripts.charts.winter_charts.winter_HP_chart import *
from scripts.charts.winter_charts.winter_LP_chart import *
from scripts.charts.winter_charts.winter_LT_chart import *
from scripts.charts.winter_charts.winter_HPHT_chart import *
from scripts.charts.winter_charts.winter_LPLT_chart import *
from scripts.charts.summer_charts.summer_HT_chart import *
from scripts.charts.summer_charts.summer_HP_chart import *
from scripts.charts.summer_charts.summer_LP_chart import *
from scripts.charts.summer_charts.summer_LT_chart import *
from scripts.charts.summer_charts.summer_HPHT_chart import *
from scripts.charts.summer_charts.summer_LPLT_chart import *
from scripts.charts.normal_charts.normal_HT_chart import *
from scripts.charts.normal_charts.normal_HP_chart import *
from scripts.charts.normal_charts.normal_LP_chart import *
from scripts.charts.normal_charts.normal_LT_chart import *
from scripts.charts.normal_charts.normal_HPHT_chart import *
from scripts.charts.normal_charts.normal_LPLT_chart import *

weather_type_routes = Blueprint('weather_type_routes', __name__)

@weather_type_routes.route('/winter_types')
def winter_simulation_type_routes():
    winter_HP_chart()
    winter_LP_chart()
    winter_LT_chart()
    winter_HT_chart()  
    winter_HPHT_chart()
    winter_LPLT_chart()
    return render_template('chart_templates/winter_types_chart.html', 
    chart1='static/charts/Winter_HT_chart.png', chart2='static/charts/Winter_LT_chart.png', 
    chart3='static/charts/Winter_HP_chart.png', chart4='static/charts/Winter_LP_chart.png', 
    chart5='static/charts/Winter_HPHT_chart.png', chart6='static/charts/Winter_LPLT_chart.png')

@weather_type_routes.route('/summer_types')
def summer_simulation_type_routes():
    summer_HP_chart()
    summer_LP_chart()
    summer_LT_chart()
    summer_HT_chart() 
    summer_HPHT_chart()
    summer_LPLT_chart()
    return render_template('chart_templates/summer_types_chart.html', 
    chart1='static/charts/Summer_HT_chart.png', chart2='static/charts/Summer_LT_chart.png', 
    chart3='static/charts/Summer_HP_chart.png', chart4='static/charts/Summer_LP_chart.png', 
    chart5='static/charts/Summer_HPHT_chart.png', chart6='static/charts/Summer_LPLT_chart.png')

@weather_type_routes.route('/normal_types')
def normal_simulation_type_routes():
    normal_HP_chart()
    normal_LP_chart()
    normal_LT_chart()
    normal_HT_chart() 
    normal_HPHT_chart()
    normal_LPLT_chart()
    return render_template('chart_templates/normal_types_chart.html', 
    chart1='static/charts/Normal_HT_chart.png', chart2='static/charts/Normal_LT_chart.png', 
    chart3='static/charts/Normal_HP_chart.png', chart4='static/charts/Normal_LP_chart.png', 
    chart5='static/charts/Normal_HPHT_chart.png', chart6='static/charts/Normal_LPLT_chart.png')