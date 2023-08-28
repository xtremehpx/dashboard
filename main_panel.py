import pandas as pd
import numpy as np
import panel as pn
import hvplot.pandas
from holoviews import opts
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

# Create a Panel DataFrame
panel_df = pn.widgets.DataFrame(df)


# List of data column names
data_columns = ['Data Surface A', 'Data Surface B', 'Data Surface C', 'Data Surface D']


# Define function to generate grouped bar plot
def grouped_bar(column):
    grouped_data = df.groupby(['Country', 'Color'])[column].mean().reset_index()
    grouped_data = grouped_data.sort_values(by=[column], ascending=False)
    return grouped_data.hvplot.bar(x='Country', y=column, by='Color', stacked=False, title=column)

    ##### approach 2
    # grouped_data = df.groupby(['Country', 'Color'])[column].mean().reset_index()
    # grouped_data = grouped_data.sort_values(by=[column], ascending=False)
    
    # return (
    #     grouped_data
    #     .hvplot.bar(x='Country', y=column, by='Color', stacked=False, rot=90, title=column)
    #     .opts(opts.Curve(tools=['hover'], show_legend=True))
    # )

    ##### approach 3
    #     grouped_data = df.groupby(['Country', 'Color'])[column].mean().reset_index()
        
    #     fig = px.bar(
    #         grouped_data,
    #         x='Country', y=column,
    #         color='Color',
    #         barmode='group',
    #         title=column,
    #         category_orders={'Country': grouped_data.groupby('Color')[column].mean().sort_values(ascending=False).index}
    #     )
    #     return fig





# Create a list of plots using a list comprehension
plots = [grouped_bar(column) for column in data_columns]

# Combine Panel objects into a layout using Column
layout = pn.Column(
    "# Data Surface Comparison Dashboard",
    *plots  # Unpack the list of plots using *
)

# Show the dashboard
layout.servable()
