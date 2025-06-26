import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
from scripts.DB_weather_type_query import summer_LPLT_query

def summer_LPLT_chart():
    data = summer_LPLT_query() 
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
    plt.title('Summer Low Probability Low Time Chart')
    plt.grid()
    plt.savefig('static/charts/Summer_LPLT_chart.png')
    plt.close()