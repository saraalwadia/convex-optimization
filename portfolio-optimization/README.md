# Portfolio Optimization with CVXPY

This project demonstrates **portfolio optimization** using Python and CVXPY. The goal is to **minimize portfolio risk (variance)** while achieving a **minimum expected return**.

---

## Description

The code performs the following:

- Defines the expected return vector for 3 assets.
- Defines the covariance matrix of the assets.
- Sets up a **convex optimization problem** to minimize portfolio variance.
- Includes constraints:
  - The expected return of the portfolio must be above a minimum threshold.
  - The sum of investment weights must equal 1.
  - No short-selling (weights >= 0).
- Solves the optimization problem using CVXPY.
- Displays the **optimal investment weights** and **minimum portfolio variance**.
- Plots a bar chart showing the allocation to each asset.

---

## Requirements

- Python 3.x
- `cvxpy`  
- `numpy`  
- `matplotlib`  
