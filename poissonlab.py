# Standard data science
import pandas as pd
import numpy as np

np.random.seed(42)

# Display all cell outputs
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = 'all'

# Visualizations
import chart_studio.plotly as py
import plotly.graph_objs as go
from plotly.offline import iplot

# Cufflinks for dataframes
import cufflinks as cf
cf.go_offline()
cf.set_config_file(world_readable=True, theme='pearl')
