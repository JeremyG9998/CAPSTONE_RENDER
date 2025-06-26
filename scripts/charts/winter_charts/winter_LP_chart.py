import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
from scripts.DB_weather_type_query import winter_LP_query

def winter_LP_chart():
    data = winter_LP_query() 
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
    plt.title('Winter Low Probability Chart')
    plt.grid()
    plt.savefig('static/charts/Winter_LP_chart.png')
    plt.close()