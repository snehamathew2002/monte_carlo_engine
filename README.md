# Monte Carlo Portfolio Risk Engine

A Python-based quantitative finance project for simulating portfolio risk under different market conditions using Monte Carlo methods.

The engine models thousands of possible future portfolio paths using stochastic returns and evaluates downside risk through metrics such as:

- Value at Risk (VaR)
- Conditional Value at Risk (CVaR / Expected Shortfall)
- Probability of Loss

The project also includes stress-testing frameworks for analyzing portfolio behavior under:
- high-volatility market regimes
- rare crash-event scenarios

---

# Project Motivation

Traditional backtesting evaluates how a strategy performed historically.

Monte Carlo simulation answers a different question:

> “What are the possible future outcomes under uncertainty?”

This project was built to better understand:
- stochastic market behavior
- portfolio risk modeling
- tail-risk exposure
- stress testing under extreme conditions

---

# Core Quantitative Finance Concepts

## 1. Stochastic Returns

Daily portfolio returns are modeled using probabilistic distributions instead of deterministic growth assumptions.

The simulation uses normally distributed returns:

μ → expected return  
σ → volatility

---

## 2. Monte Carlo Simulation

The engine generates thousands of possible future market paths by repeatedly simulating random returns.

Each simulation produces:
- a unique portfolio evolution path
- different final portfolio outcomes

This allows risk to be analyzed as a distribution rather than a single prediction.

---

## 3. Stress Testing

The project supports multiple market regimes:

| Scenario | Description |
|----------|-------------|
| Normal Market | Standard stochastic market conditions |
| Stress Market | Elevated volatility and negative drift |
| Crash Scenario | Rare extreme downside events |

These scenarios help analyze how risk metrics deteriorate under adverse market conditions.

---

# Risk Metrics Implemented

## Value at Risk (VaR)

Measures the worst expected portfolio threshold at a confidence level.

Example:
> VaR(95%) = 8500

Meaning:
> 95% of simulations ended above $8500.

---

## Conditional Value at Risk (CVaR)

Also called Expected Shortfall.

Measures the average portfolio value in the worst-case tail scenarios beyond VaR.

CVaR captures extreme downside risk more effectively than VaR.

---

## Probability of Loss

Measures how frequently simulated portfolios end below initial capital.

This represents:
> likelihood of portfolio loss under simulated market conditions.

---

# How to Run
  1. Clone repository
    git clone https://github.com/snehamathew2002/monte_carlo_engine.git
    cd monte_carlo_engine

  2. Install dependencies  
    pip install numpy matplotlib

  3. Run project
    python main.py

---

# 🧠 Key Takeaways
  ## 1. Risk is distribution-based
      Portfolio analysis should not rely on a single expected outcome.
      Monte Carlo simulation demonstrates how portfolios evolve across thousands of possible future paths.

  ## 2. Tail risk matters
      Standard volatility assumptions underestimate extreme downside events.
      Crash-event simulations revealed substantially worse portfolio outcomes compared to standard market assumptions.
  
  ## 3. Market regimes strongly impact portfolio risk
    Stress testing showed:
      > higher volatility significantly increases downside exposure
      > crash events create asymmetric loss behavior
      > probability of loss rises sharply under adverse conditions

  ## 4. VaR and CVaR capture different dimensions of risk
      VaR identifies downside thresholds
      CVaR measures severity of extreme tail losses

---

# 📌 Author Notes

 ##  This project was built as part of exploring:
      > quantitative finance
      > portfolio risk modeling
      > stochastic simulations
      > systematic financial analysis

The focus was not only on implementation, but also on understanding how market uncertainty and tail risk affect portfolio behavior.
