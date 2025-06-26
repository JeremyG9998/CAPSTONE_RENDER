from scripts.simulation import *

def get_simulation(simulation_type):
    run1 = Winter()
    run2 = WinterHT()
    run3 = WinterLT()
    run4 = WinterHP()
    run5 = WinterLP()
    run6 = WinterHPHT()
    run7 = WinterLPLT()
    run8 = Summer()
    run9 = SummerHT()
    run10 = SummerLT()
    run11 = SummerHP()
    run12 = SummerLP()
    run13 = SummerHPHT()
    run14 = SummerLPLT()
    run15 = CustomerSimulation()
    run16 = NormalLP()
    run17 = NormalHP()
    run18 = NormalHT()
    run19 = NormalLT()
    run20 = NormalHPHT()
    run21 = NormalLPLT()

    if simulation_type == 'run1':
        return run1
    elif simulation_type == 'run2':
        return run2
    elif simulation_type == 'run3':
        return run3
    elif simulation_type == 'run4':
        return run4
    elif simulation_type == 'run5':
        return run5
    elif simulation_type == 'run6':
        return run6
    elif simulation_type == 'run7':
        return run7
    elif simulation_type == 'run8':
        return run8
    elif simulation_type == 'run9':
        return run9
    elif simulation_type == 'run10':
        return run10
    elif simulation_type == 'run11':
        return run11
    elif simulation_type == 'run12':
        return run12
    elif simulation_type == 'run13':
        return run13
    elif simulation_type == 'run14':
        return run14
    elif simulation_type == 'run15':
        return run15
    elif simulation_type == 'run16':
        return run16
    elif simulation_type == 'run17':
        return run17
    elif simulation_type == 'run18':
        return run18
    elif simulation_type == 'run19':
        return run19
    elif simulation_type == 'run20':
        return run20
    elif simulation_type == 'run21':
        return run21