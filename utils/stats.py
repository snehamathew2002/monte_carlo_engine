import numpy as np

def var_95(final_values):
    return np.percentile(final_values, 5)

def cvar_95(final_values):
    return np.mean([x for x in final_values if x <= var_95(final_values)])

def probability_of_loss(final_values, initial_portfolio):
    losses = [x for x in final_values if x < initial_portfolio]
    return len(losses) / len(final_values)