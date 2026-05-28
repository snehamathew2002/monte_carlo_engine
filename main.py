from engine.simulator import run_simulation
import matplotlib.pyplot as plt

from utils.stats import cvar_95, probability_of_loss, var_95

def main():
    """Run the Monte Carlo simulation workflow."""
    print("Starting Monte Carlo portfolio simulation...")
    initial_portfolio = 10000
    mu = 0.0005        # mean daily return
    sigma = 0.01       # volatility
    days = 252         # 1 trading year
    simulations = 1000

    all_simulations = run_simulation(initial_portfolio, mu, sigma, days, simulations)
    print("Simulation completed.")

    for path in all_simulations[:50]:  # Plot the first 50 simulation paths
        plt.plot(path)

    plt.title("Monte Carlo Simulation of Portfolio Returns")
    plt.show()

    final_values = [sim[-1] for sim in all_simulations]

    print("VaR (95%):", var_95(final_values))
    print("CVaR (95%):", cvar_95(final_values))
    print("Probability of Loss:", probability_of_loss(final_values, initial_portfolio))

    plt.hist(final_values, bins=50)
    plt.title("Distribution of Final Portfolio Values")
    plt.show()

if __name__ == "__main__":
    main()
