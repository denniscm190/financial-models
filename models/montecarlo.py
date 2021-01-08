import pandas as pd
import numpy as np


def montecarlo(data, days, simulations):
    # Variables for the simulation
    return_std = data['Pct change'].std()  # Compute std of daily pct returns
    print('Standard deviation -> ' + str(return_std))
    days = days
    simulations = simulations

    estimated_df = pd.DataFrame()  # Empty df for the results
    estimated_prices = []

    for simulation in range(simulations):
        print('Simulation -> ' + str(simulation))
        price = data['Close'][-1]
        simulation_prices = [price]

        for day in range(days):
            price = price * (1 + np.random.normal(0, return_std))
            simulation_prices.append(price)
            estimated_prices.append(price)

        estimated_df['Simulation ' + str(simulation)] = simulation_prices

    return estimated_df, estimated_prices
