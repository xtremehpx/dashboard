import pandas as pd
import numpy as np
import panel as pn
import hvplot.pandas
from panel.interact import interact
from holoviews import opts

# Generate random data
np.random.seed(42)
num_rows = 100
data = {
    'Name': [f'Person {i}' for i in range(1, num_rows + 1)],
    'City': np.random.choice(['City A', 'City B', 'City C'], num_rows),
    'Country': np.random.choice(['Country X', 'Country Y', 'Country Z'], num_rows),
    'Color': np.random.choice(['Red', 'Blue', 'Green'], num_rows),
    'Build': np.random.choice(['A', 'B', 'C', 'D'], num_rows),
    'Material': np.random.choice(['Metal', 'Wood', 'Plastic'], num_rows),
    'Data Surface A': np.random.uniform(0, 10, num_rows),
    'Data Surface B': np.random.uniform(0, 10, num_rows),
    'Data Surface C': np.random.uniform(10, 100, num_rows),
    'Data Surface D': np.random.uniform(1000, 3000, num_rows),
    'Data Surface E': np.random.uniform(10000, 20000, num_rows)
}

df = pd.DataFrame(data)

# # Define function to generate grouped bar plot
# def grouped_bar(column, city_selection, build_selection):
#     filtered_data = df[(df['City'].isin(city_selection)) & (df['Build'].isin(build_selection))]
#     grouped_data = (
#         filtered_data.groupby(['Country', 'Color'])
#         .agg({column: 'mean'})
#         .reset_index()
#         .sort_values(by=[column], ascending=False)
#     )

#     return (
#         grouped_data
#         .hvplot.bar(x='Country', y=column, by='Color', stacked=False, rot=90, title=column)
#     )

# # List of data column names
# data_columns = ['Data Surface A', 'Data Surface B', 'Data Surface C', 'Data Surface D', 'Data Surface E']

# # Create selection widgets
# city_selection = pn.widgets.MultiSelect(name='Select Cities', options=list(df['City'].unique()), value=['City A', 'City B'])
# build_selection = pn.widgets.MultiSelect(name='Select Builds', options=list(df['Build'].unique()), value=['A', 'B'])

# # Define the interactive function
# @interact(city=city_selection, build=build_selection)
# def interactive_dashboard(city, build):
#     plots = [grouped_bar(column, city, build) for column in data_columns]
#     plots = [plots[i:i+2] for i in range(0, len(plots), 2)]  # Split into 2x2 grid
#     layout = pn.Column(
#         "# Interactive Data Surface Comparison Dashboard",
#         city_selection,
#         build_selection,
#         *[
#             pn.Row(*plot_row)
#             for plot_row in plots
#         ]
#     )
#     return layout

# # Show the dashboard
# interactive_dashboard.servable()


# Create an interactive DataFrame
interactive_df = pn.widgets.DataFrame(df, name='Interactive DataFrame')

# Create selection widgets
city_selection = pn.widgets.MultiSelect(name='Select Cities', options=list(df['City'].unique()), value=['City A', 'City B'])
build_selection = pn.widgets.MultiSelect(name='Select Builds', options=list(df['Build'].unique()), value=['A', 'B'])

ncols = 3  # Number of columns

# Define function to generate grouped bar plot
def grouped_bar(column):
    filtered_data = interactive_df.value[(interactive_df.value['City'].isin(city_selection.value)) & (interactive_df.value['Build'].isin(build_selection.value))]
    grouped_data = (
        filtered_data.groupby(['Country', 'Color'])
        .agg({column: 'mean'})
        .reset_index()
        .sort_values(by=[column], ascending=False)
    )

    # Calculate percentage width and height based on available space
    total_width = 100  # Total width in percentage
    plot_width = int(total_width / ncols)*10
    plot_height = 200  # Fixed height in percentage

    return (
        grouped_data
        .hvplot.bar(x='Country', y=column, by='Color', stacked=False, rot=90, title=column, width=plot_width, height=plot_height)
    )

# List of data column names
data_columns = ['Data Surface A', 'Data Surface B', 'Data Surface C', 'Data Surface D', 'Data Surface E']

# Create a pipeline for the plots
plots = [grouped_bar(column) for column in data_columns]
responsive_grid = pn.GridBox(
        *plots, 
        ncols=ncols, responsive=True, width_policy="fit", sizing_mode="stretch_width"
    )

dashboard = pn.Column(
    "# Interactive Data Surface Comparison Dashboard",
    city_selection,
    build_selection,
    responsive_grid,
    sizing_mode="stretch_width",
)

pn.extension(sizing_mode="stretch_width")  # Apply sizing mode to the entire dashboard

# Show the dashboard
dashboard.servable()
