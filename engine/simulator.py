"""Monte Carlo simulation engine for portfolio return modeling.

This module will contain the core simulation logic for generating
portfolio return paths using Monte Carlo methods.
"""
import numpy as np

def normal_returns(mu, sigma, days):
    return np.random.normal(mu, sigma, days)

def stress_returns(mu, sigma, days):
    return np.random.normal(mu, sigma*3, days)

def crash_returns(mu, sigma, days):
    returns = []

    for _ in range(days):
        if np.random.rand() < 0.02:  # 2% chance of a crash
            r = -0.08  # Large negative return
        else:
            r = np.random.normal(mu, sigma)  # Normal return
        returns.append(r)

    return returns

def simulate_portfolio(initial, returns):
    portfolio = [initial]

    for i in returns:
        new_value = portfolio[-1] * (1 + i)
        portfolio.append(new_value)

    return portfolio