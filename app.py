import pandas as pd
import matplotlib.pyplot as plt
from get_historical_data import *

cardano_data = get_historical_data()


cardano_symbol = ''  # look at the cardano_data object and try to find where the 'symbol' property is and extract it