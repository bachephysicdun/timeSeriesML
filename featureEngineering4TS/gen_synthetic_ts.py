
from typing import List, Tuple
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# seasonality component
def complex_seasonality(time, configs):

    # example for config input:
    # config: (amplitude, period, phase_shift)
    # seasonality_configs = [
    #     (2, 365/6, 0),          # Main yearly seasonality
    #     (1, 365/8, np.pi/4),    # Sub-seasonality with a different period and phase
    #     (0.5, 365/10, np.pi/2)  # Another layer of sub-seasonality
    # ]

    seasonality = np.zeros_like(time, dtype=float) 
    for amplitude, period, phase_shift in configs:
        seasonality += (amplitude * (np.sin((2 * np.pi * time / period) + phase_shift) + 1)/2 + 0.001*time)**2
        seasonality += amplitude * (np.cos((2 * np.pi * time / period) + phase_shift) + 1)/2

    return seasonality


def generate_synthetic_ts(
        seasonality_configs:List[Tuple[int, int, int]] = [(2, 365/6, 0), (1, 365/8, np.pi/4), (0.5, 365/10, np.pi/2)], 
        total_points = 365 * 4,
        trend_slope = 0.001,
        noise_level = 0.8,
        noise_avg_loc = 1,
        random_state:int=73) -> pd.DataFrame:

    # generate simple synthetic timeseries that has trend, seasonality and residual components.
    np.random.seed(random_state) # for reproducibility purpos

    time = np.arange(total_points)
    seasonality = complex_seasonality(time, seasonality_configs)

    # trend component
    trend = trend_slope * time


    # residual component
    residual = np.random.normal(loc=noise_avg_loc, scale=noise_level, size=total_points)


    df = pd.DataFrame(zip(trend, seasonality, residual), columns=['trend', 'seasonality', 'residual'])
    df['DateTime'] = pd.date_range(start='2010-01-01', periods=total_points, freq='D')
    df['Value'] = df['trend'] + df['seasonality'] + df['residual']


    return df