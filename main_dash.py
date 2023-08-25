import pandas as pd
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output  # Import Input component
import plotly.express as px

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

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div([
    html.H1("Data Surface Comparison Dashboard"),
    dcc.Graph(id="data-surface-a"),
    dcc.Graph(id="data-surface-b"),
    dcc.Graph(id="data-surface-c"),
    dcc.Graph(id="data-surface-d"),
    dcc.Interval(
        id='interval-component',
        interval=60000,  # in milliseconds, so 60 seconds
        n_intervals=0
    )
])

# Define callback to update the graphs at a regular interval
@app.callback(
    [Output("data-surface-a", "figure"),
     Output("data-surface-b", "figure"),
     Output("data-surface-c", "figure"),
     Output("data-surface-d", "figure")],
    [Input("interval-component", "n_intervals")]
)
def update_graphs(n):
    figures = []
    data_columns = ['Data Surface A', 'Data Surface B', 'Data Surface C', 'Data Surface D']
    
    for column in data_columns:
        grouped_data = df.groupby(['Country', 'Color'])[column].mean().reset_index()
        grouped_data = grouped_data.sort_values(by=[column], ascending=False)
        
        bar_chart = px.bar(grouped_data, x='Country', y=column, color='Color', barmode='group')
        figures.append(bar_chart)
    
    return figures

if __name__ == "__main__":
    app.run_server(debug=True)
