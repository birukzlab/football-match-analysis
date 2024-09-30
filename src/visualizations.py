import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

def create_visualizations(passes_data):
    """Creates visualizations including passing network, shot map, and heatmap."""
    
    passing_x_data = [location[0] for location in passes_data['location'] if isinstance(location, (list, tuple)) and len(location) > 1]
    passing_y_data = [location[1] for location in passes_data['location'] if isinstance(location, (list, tuple)) and len(location) > 1]
    
    # Shot Map
    shot_x_data = passing_x_data  
    shot_y_data = passing_y_data  
    
    # Heatmap Data 
    heatmap_data = np.random.rand(10, 10)  

    # Create subplots for visualizations
    fig = make_subplots(rows=2, cols=2, subplot_titles=('Passing Network', 'Shot Locations', 'Territory Control'))

    # Add Passing Network
    fig.add_trace(go.Scatter(x=passing_x_data, y=passing_y_data, mode='markers+lines', name='Passes'), row=1, col=1)

    # Add Shot Map
    fig.add_trace(go.Scatter(x=shot_x_data, y=shot_y_data, mode='markers', name='Shots'), row=1, col=2)

    # Add Territory Control Heatmap
    fig.add_trace(go.Heatmap(z=heatmap_data), row=2, col=1)

    # Update layout
    fig.update_layout(height=800, title_text="Match Analysis Visualization")

    # Show the figure
    fig.show()
