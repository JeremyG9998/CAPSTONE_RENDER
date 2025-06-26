import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
from scripts.DB_weather_type_query import normal_HP_query

def normal_HP_chart():
    data = normal_HP_query() 
    if not data:
        data = [0, 0, 0, 0, 0]
    lava, hot_fudge, blizzard, chocolate, vanilla = data
    
    plt.bar('Lava', lava)
    plt.bar('Hot Fudge', hot_fudge)
    plt.bar('Blizzard', blizzard)
    plt.bar('Chocolate', chocolate)
    plt.bar('Vanilla', vanilla)

    plt.xlabel('All Flavors')
    plt.ylabel('Total Purchases')
    plt.title('Normal High Probability Chart')
    plt.grid()
    plt.savefig('static/charts/Normal_HP_chart.png')
    plt.close() 