# Import the main Dash library to create the web app
import dash
# Import dash components for the UI layout and interactivity
from dash import html, dcc, Input, Output
# Import Pandas for data handling and manipulation
import pandas as pd
# Import Plotly Express for creating the interactive charts
import plotly.express as px

# Read the CSV file into a pandas DataFrame
# This data will be available globally for the app to use
df = pd.read_csv("formatted_data.csv")

# Initialize the Dash application
app = dash.Dash(__name__)

# Define the layout of the app (the visual structure of the web page)
app.layout = html.Div([

    # A header title for the dashboard
    html.H1("My Dashboard"),

    # A dropdown menu component for selecting a column
    dcc.Dropdown(
        # The ID is used to target this component in our callback
        id="column-select",
        # Create an option in the dropdown for every column name in our DataFrame
        options=[{"label": col, "value": col} for col in df.columns],
        # Set the default selected value to the first column in the dataset
        value=df.columns[0]
    ),

    # A graph component where our Plotly chart will be rendered
    dcc.Graph(id="main-chart")

])

# Define a callback to update the graph based on the dropdown selection.
# This binds the "value" of the dropdown (Input) to our function,
# and sends the returned "figure" to our graph component (Output).
@app.callback(
    Output("main-chart", "figure"),
    Input("column-select", "value")
)
# This function runs automatically every time the dropdown value changes
def update_graph(column_name):
    # Create a line chart using Plotly Express with the selected column on the x-axis
    fig = px.line(df, x=column_name)
    # Return the created figure to update the graph component
    return fig

# This ensures the app only runs if the script is executed directly (not imported)
if __name__ == "__main__":
    # Run the app locally in debug mode (enables hot-reloading and helpful error messages)
    app.run(debug=True)
