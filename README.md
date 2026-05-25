# Insurance Risk Analytics & Predictive Modeling

This project analyzes historical car insurance data for AlphaCare Insurance Solutions (ACIS) to uncover low-risk customer segments, validate statistical hypotheses, and build predictive pricing models.

## Objectives

- Perform exploratory data analysis (EDA)
- Analyze insurance risk patterns
- Conduct hypothesis testing
- Build predictive models for claim severity and probability
- Support risk-based pricing strategies

## Project Structure

- `notebooks/` → Jupyter notebooks
- `src/` → reusable Python modules
- `reports/` → final business reports
- `tests/` → unit tests
- `data/` → datasets tracked with DVC

## Tech Stack

- Python
- Pandas
- Scikit-learn
- XGBoost
- SHAP
- DVC
- GitHub Actions

## Key Metrics

- Loss Ratio = TotalClaims / TotalPremium
- Margin = TotalPremium - TotalClaims

## Key Findings

- The portfolio loss ratio exceeded 100%, indicating profitability challenges.
- Insurance risk varies significantly across provinces and vehicle types.
- Claims distributions are highly skewed with extreme outliers.
- Certain vehicle makes exhibit substantially higher claim severity.
