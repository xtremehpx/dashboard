import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# import plotly.offline as iplot
# import plotly as py
# py.offline.init_notebook_mode(connected = True)


# Generate random data
np.random.seed(42)
num_rows = 100
data = {
    'Name': [f'Person {i}' for i in range(1, num_rows + 1)],
    'City': np.random.choice(['City A', 'City B', 'City C'], num_rows),
    'Country': np.random.choice(['Country X', 'Country Y', 'Country Z'], num_rows),
    'Color': np.random.choice(['Red', 'Blue', 'Green'], num_rows),
    'Build': np.random.choice(['A', 'B', 'C', 'D'], num_rows),
    'Data Surface A': np.random.randint(1, 100, num_rows),
    'Data Surface B': np.random.randint(1, 100, num_rows),
    'Data Surface C': np.random.randint(1, 100, num_rows),
    'Data Surface D': np.random.randint(1, 100, num_rows)
}

df = pd.DataFrame(data)

# Create subplots
fig = make_subplots(rows=2, cols=2, subplot_titles=['Data Surface A', 'Data Surface B', 'Data Surface C', 'Data Surface D'])

# Loop through each data column and create a grouped bar chart
data_columns = ['Data Surface A', 'Data Surface B', 'Data Surface C', 'Data Surface D']
for idx, column in enumerate(data_columns):
    row = idx // 2 + 1
    col = idx % 2 + 1
    
    grouped_data = df.groupby(['Country', 'Color'])[column].mean().reset_index()
    grouped_data = grouped_data.sort_values(by=[column], ascending=False)
    
    bar_chart = px.bar(grouped_data, x='Country', y=column, color='Color', barmode='group')
    fig.add_trace(bar_chart.data[0], row=row, col=col)
    
fig.update_layout(title='Data Surface Comparison by Country and Color', showlegend=False)
    
# Show the interactive dashboard
fig.show()
