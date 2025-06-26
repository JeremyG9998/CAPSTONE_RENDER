import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
from scripts.DB_queries import customer_simulation_data, normal_data_query

def customer_simulation_chart():
    data = normal_data_query()
    if not data:
        lava, hot_fudge, blizzard, chocolate, vanilla = [0, 0, 0, 0, 0]
    else:  # returns error if sql query is ran with no rows for SUM
        total_data = customer_simulation_data() 
        lava, hot_fudge, blizzard, chocolate, vanilla = total_data

    plt.bar('Lava', lava)
    plt.bar('Hot Fudge', hot_fudge)
    plt.bar('Blizzard', blizzard)
    plt.bar('Chocolate', chocolate)
    plt.bar('Vanilla', vanilla)

    plt.xlabel('Flavor')
    plt.ylabel('Total Purchases')
    plt.title('Customer Simulation')
    plt.grid()
    plt.savefig('static/charts/simulation_chart_Customer.png')
    plt.close()