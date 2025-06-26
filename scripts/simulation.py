import random
from scripts.insert_DB_script import (
    save_to_purchases_table,
    save_to_flavors_count_table,
    save_simulation_type,
    save_total_purchases,
    save_truck_report,
    save_simulation_type_ref
)
from database_layer import db_setup

class CustomerSimulation:
    def __init__(self):
        self.choice = None
        self.results = []
        self.flavor_count = []
        self.probability = 2
        self.times = 100
        db_setup()
        self.lava = 0
        self.hot_fudge = 0
        self.blizzard = 0
        self.chocolate = 0
        self.vanilla = 0

    def flavors(self):
        flavor_likelihood = ["lava", "hot_fudge", "blizzard", "chocolate", "vanilla"]
        self.choice = random.choice(flavor_likelihood)
        return self.choice
    
    def flavors_count(self):
        if self.choice == "lava":
            self.lava += 1
        elif self.choice == "hot_fudge":
            self.hot_fudge += 1
        elif self.choice == "blizzard":
            self.blizzard += 1
        elif self.choice == "chocolate":
            self.chocolate += 1
        elif self.choice == "vanilla":
            self.vanilla += 1
        self.flavor_count = [self.lava, self.hot_fudge, self.blizzard, self.chocolate, self.vanilla]
        return self.flavor_count
        
    def simulations(self):
        for _ in range(self.times):
            if random.randint(1, self.probability) == 1:
                flavor = self.flavors()
                self.results.append(flavor)
                self.flavors_count()
        save_simulation_type(self)
        save_simulation_type_ref(self)
        save_to_flavors_count_table(self)
        save_truck_report()
        save_to_purchases_table(self)
        save_total_purchases(self)
        return self.results

class Winter(CustomerSimulation): # Winter
    def flavors(self):
        flavor_likelihood = ["lava", "hot_fudge", "chocolate", "vanilla", "blizzard"]
        flavor_likelihood += ["blizzard", "blizzard", "chocolate"] 
        self.choice = random.choice(flavor_likelihood)
        return self.choice

class WinterHT(CustomerSimulation): # Winter High Time
    def flavors(self):
        flavor_likelihood = ["lava", "hot_fudge", "chocolate", "vanilla", "blizzard"]
        flavor_likelihood += ["blizzard", "blizzard", "chocolate"] 
        self.choice = random.choice(flavor_likelihood)
        return self.choice

    def simulations(self):
        self.times = 150
        super().simulations()

class WinterLT(CustomerSimulation): # Winter Short Time
    def flavors(self):
        flavor_likelihood = ["lava", "hot_fudge", "chocolate", "vanilla", "blizzard"]
        flavor_likelihood += ["blizzard", "blizzard", "chocolate"] 
        self.choice = random.choice(flavor_likelihood)
        return self.choice
    
    def simulations(self):
        self.times = 65
        super().simulations()

class WinterHP(CustomerSimulation): # Winter High Probability
    def flavors(self):
        flavor_likelihood = ["lava", "hot_fudge", "chocolate", "vanilla", "blizzard"]
        flavor_likelihood += ["blizzard", "blizzard", "chocolate"] 
        self.choice = random.choice(flavor_likelihood)
        return self.choice
    
    def simulations(self):
        self.probability = 1
        super().simulations()

class WinterLP(CustomerSimulation): # Winter Low Probability
    def flavors(self):
        flavor_likelihood = ["lava", "hot_fudge", "chocolate", "vanilla", "blizzard"]
        flavor_likelihood += ["blizzard", "blizzard", "chocolate"] 
        self.choice = random.choice(flavor_likelihood)
        return self.choice
    
    def simulations(self):
        self.probability = 3
        super().simulations()

class WinterHPHT(CustomerSimulation): # Winter High Probability High Time
    def flavors(self):
        flavor_likelihood = ["lava", "hot_fudge", "chocolate", "vanilla", "blizzard"]
        flavor_likelihood += ["blizzard", "blizzard", "chocolate"] 
        self.choice = random.choice(flavor_likelihood)
        return self.choice
    
    def simulations(self):
        self.probability = 1
        self.times = 150
        super().simulations()

class WinterLPLT(CustomerSimulation): # Winter Low Probability Low Time
    def flavors(self):
        flavor_likelihood = ["lava", "hot_fudge", "chocolate", "vanilla", "blizzard"]
        flavor_likelihood += ["blizzard", "blizzard", "chocolate"] 
        self.choice = random.choice(flavor_likelihood)
        return self.choice
    
    def simulations(self):
        self.probability = 3
        self.times = 65
        super().simulations()

class Summer(CustomerSimulation): # Summer
    def flavors(self):
        flavor_likelihood = ["lava", "hot_fudge", "chocolate", "vanilla", "blizzard"]
        flavor_likelihood += ["lava", "lava", "hot_fudge"]  
        self.choice = random.choice(flavor_likelihood)
        return self.choice

class SummerHT(CustomerSimulation): # Summer High Time
    def flavors(self):
        flavor_likelihood = ["lava", "hot_fudge", "chocolate", "vanilla", "blizzard"]
        flavor_likelihood += ["lava", "lava", "hot_fudge"]  
        self.choice = random.choice(flavor_likelihood)
        return self.choice
    
    def simulations(self):
        self.times = 150
        super().simulations()

class SummerLT(CustomerSimulation): # Summer Low Time
    def flavors(self):
        flavor_likelihood = ["lava", "hot_fudge", "chocolate", "vanilla", "blizzard"]
        flavor_likelihood += ["lava", "lava", "hot_fudge"]  
        self.choice = random.choice(flavor_likelihood)
        return self.choice
    
    def simulations(self):
        self.times = 65
        super().simulations()

class SummerHP(CustomerSimulation): # Summer High Probability
    def flavors(self):
        flavor_likelihood = ["lava", "hot_fudge", "chocolate", "vanilla", "blizzard"]
        flavor_likelihood += ["lava", "lava", "hot_fudge"]  
        self.choice = random.choice(flavor_likelihood)
        return self.choice
    
    def simulations(self):
        self.probability = 1
        super().simulations()

class SummerLP(CustomerSimulation): # Summer Low Probability
    def flavors(self):
        flavor_likelihood = ["lava", "hot_fudge", "chocolate", "vanilla", "blizzard"]
        flavor_likelihood += ["lava", "lava", "hot_fudge"]  
        self.choice = random.choice(flavor_likelihood)
        return self.choice
    
    def simulations(self):
        self.probability = 3
        super().simulations()

class SummerHPHT(CustomerSimulation): # Summer High Probability High Time
    def flavors(self):
        flavor_likelihood = ["lava", "hot_fudge", "chocolate", "vanilla", "blizzard"]
        flavor_likelihood += ["lava", "lava", "hot_fudge"]  
        self.choice = random.choice(flavor_likelihood)
        return self.choice
    
    def simulations(self):
        self.probability = 1
        self.times = 150
        super().simulations()

class SummerLPLT(CustomerSimulation): # Summer Low Probability Low Time
    def flavors(self):
        flavor_likelihood = ["lava", "hot_fudge", "chocolate", "vanilla", "blizzard"]
        flavor_likelihood += ["lava", "lava", "hot_fudge"]  
        self.choice = random.choice(flavor_likelihood)
        return self.choice
    
    def simulations(self):
        self.probability = 3
        self.times = 65
        super().simulations()

class NormalLP(CustomerSimulation): # Normal Low Probability
    def simulations(self):
        self.probability = 3
        super().simulations()

class NormalHP(CustomerSimulation): # Normal High Probability
    def simulations(self):
        self.probability = 1
        super().simulations()

class NormalHT(CustomerSimulation): # Normal High Time
    def simulations(self):
        self.times = 150
        super().simulations()

class NormalLT(CustomerSimulation): # Normal Low Time
    def simulations(self):
        self.times = 65
        super().simulations()

class NormalHPHT(CustomerSimulation): # Normal High Probability High Time
    def simulations(self):
        self.probability = 1
        self.times = 150
        super().simulations()

class NormalLPLT(CustomerSimulation): # Normal Low Probability Low Time
    def simulations(self):
        self.probability = 3
        self.times = 65
        super().simulations()

if __name__ == "__main__":
    run = Winter()  
    run.simulations()