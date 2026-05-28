"""Monte Carlo simulation engine for portfolio return modeling.

This module will contain the core simulation logic for generating
portfolio return paths using Monte Carlo methods.
"""
import numpy as np

def generate_returns(mu, sigma, days):
    return np.random.normal(mu, sigma, days)

def simulate_portfolio(initial, returns):
    portfolio = [initial]

    for i in returns:
        new_value = portfolio[-1] * (1 + i)
        portfolio.append(new_value)

    return portfolio

def run_simulation(initial, mu, sigma, days, simulations):
    all_simulations = []

    for _ in range(simulations):
        returns = generate_returns(mu, sigma, days)
        portfolio_path = simulate_portfolio(initial, returns)
        all_simulations.append(portfolio_path)

    return all_simulations