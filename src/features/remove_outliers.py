import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import scipy

from sklearn.neighbors import LocalOutlierFactor

# load data --------------------------------
df = pd.read_pickle("../../data/interim/01_data_processed.pkl")
