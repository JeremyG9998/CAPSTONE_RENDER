import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
from scripts.DB_queries import winter_simulation_data, winter_data_query

def winter_simulation_chart():
    data = winter_data_query() 
    
    if not data:
        lava, hot_fudge, blizzard, chocolate, vanilla = [0, 0, 0, 0, 0]
    else:  # returns error if sql query is ran with no rows for SUM
        total_data = winter_simulation_data() 
        lava, hot_fudge, blizzard, chocolate, vanilla = total_data

    plt.bar('Lava', lava)
    plt.bar('Hot Fudge', hot_fudge)
    plt.bar('Blizzard', blizzard)
    plt.bar('Chocolate', chocolate)
    plt.bar('Vanilla', vanilla)

    plt.xlabel('Flavor')
    plt.ylabel('Total Purchases')
    plt.title('Winter Simulation')
    plt.grid()
    plt.savefig('static/charts/simulation_chart_Winter.png')
    plt.close()