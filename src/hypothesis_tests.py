from scipy.stats import ttest_ind
from scipy.stats import chi2_contingency
import pandas as pd


def run_ttest(group_a, group_b):
    """
    Run independent t-test between two groups.
    """
    
    t_stat, p_value = ttest_ind(
        group_a,
        group_b,
        nan_policy="omit"
    )
    
    return {
        "t_statistic": t_stat,
        "p_value": p_value
    }


def run_chi_square(contingency_table):
    """
    Run chi-square test.
    """
    
    chi2, p_value, dof, expected = chi2_contingency(
        contingency_table
    )
    
    return {
        "chi2": chi2,
        "p_value": p_value,
        "degrees_of_freedom": dof
    }
