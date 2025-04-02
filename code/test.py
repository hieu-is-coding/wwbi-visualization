import pandas as pd
import numpy as np
from dash import Dash, dcc, html, Input, Output
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import seaborn as sns

wwbi_country = pd.read_csv('../data/wwbi_country.csv')
wwbi_data = pd.read_csv('../data/wwbi_data.csv')
wwbi_series = pd.read_csv('../data/wwbi_series.csv')


def process_and_integrate_vietnam_data(wwbi_data_vietnam):
    # Define the mapping between indicator codes and metadata
    indicator_mapping = {
        # Public sector
        'BI.PWK.PUBS.SN.FE.ZS': {'sector': 'Public', 'occupation': 'Managers', 'level': 'High'},
        'BI.PWK.PUBS.PN.FE.ZS': {'sector': 'Public', 'occupation': 'Professionals', 'level': 'High'},
        'BI.PWK.PUBS.TN.FE.ZS': {'sector': 'Public', 'occupation': 'Technicians', 'level': 'High'},
        'BI.PWK.PUBS.CK.FE.ZS': {'sector': 'Public', 'occupation': 'Clerks', 'level': 'Low'},
        'BI.PWK.PUBS.EO.FE.ZS': {'sector': 'Public', 'occupation': 'Elementary', 'level': 'Low'},
        
        # Private sector
        'BI.PWK.PRVS.SN.FE.ZS': {'sector': 'Private', 'occupation': 'Managers', 'level': 'High'},
        'BI.PWK.PRVS.PN.FE.ZS': {'sector': 'Private', 'occupation': 'Professionals', 'level': 'High'},
        'BI.PWK.PRVS.TN.FE.ZS': {'sector': 'Private', 'occupation': 'Technicians', 'level': 'High'},
        'BI.PWK.PRVS.CK.FE.ZS': {'sector': 'Private', 'occupation': 'Clerks', 'level': 'Low'},
        'BI.PWK.PRVS.EO.FE.ZS': {'sector': 'Private', 'occupation': 'Elementary', 'level': 'Low'}
    }
    
    # Filter data to only include indicators we're interested in
    relevant_indicators = list(indicator_mapping.keys())
    filtered_data = wwbi_data_vietnam[wwbi_data_vietnam['indicator_code'].isin(relevant_indicators)].copy()
    
    # Add metadata columns based on indicator_code
    for column, data in indicator_mapping.items():
        mask = filtered_data['indicator_code'] == column
        for key, value in data.items():
            filtered_data.loc[mask, key] = value
    
    # Define occupation order
    occupation_order = ['Managers', 'Professionals', 'Technicians', 'Clerks', 'Elementary']
    
    # Convert occupation to ordered categorical
    filtered_data['occupation'] = pd.Categorical(
        filtered_data['occupation'],
        categories=occupation_order,
        ordered=True
    )
    
    # Convert sector and level to categorical
    filtered_data['sector'] = pd.Categorical(filtered_data['sector'], categories=['Public', 'Private'])
    filtered_data['level'] = pd.Categorical(filtered_data['level'], categories=['High', 'Low'])
    
    # Convert values to percentages 
    if filtered_data['value'].max() < 1:
        filtered_data['value'] = filtered_data['value'] * 100
    
    return filtered_data

wwbi_data_vietnam = wwbi_data[wwbi_data['country_code'] == 'VNM']
integrated_df = process_and_integrate_vietnam_data(wwbi_data_vietnam)
app = Dash(__name__)

app.title = "Female Representation Dashboard"

app.layout = html.Div([
    html.H1("Female Representation by Occupation Type in Vietnam (2010–2016)",
            style={'textAlign': 'center'}),

    html.Div([
        html.Label("Select Sector(s):"),
        dcc.Dropdown(
            options=[{'label': s, 'value': s} for s in integrated_df['sector'].unique()],
            value=['Public', 'Private'],
            multi=True,
            id='sector-dropdown'
        ),
        html.Label("Select Occupation(s):", style={'marginTop': '1em'}),
        dcc.Dropdown(
            options=[{'label': o, 'value': o} for o in sorted(integrated_df['occupation'].unique())],
            value=sorted(integrated_df['occupation'].unique()),
            multi=True,
            id='occupation-dropdown'
        )
    ], style={'width': '40%', 'margin': 'auto'}),

    dcc.Graph(id='bar-chart')
])

@app.callback(
    Output('bar-chart', 'figure'),
    Input('sector-dropdown', 'value'),
    Input('occupation-dropdown', 'value')
)
def update_bar_chart(selected_sectors, selected_occupations):
    filtered = integrated_df[
        integrated_df['sector'].isin(selected_sectors) &
        integrated_df['occupation'].isin(selected_occupations)
    ]

    grouped = filtered.groupby(['sector', 'occupation', 'year'])['value'].mean().reset_index()
    years = sorted(grouped['year'].unique())

    # Build the figure with subplots
    fig = go.Figure()
    for sector in selected_sectors:
        sector_data = grouped[grouped['sector'] == sector]
        for occupation in selected_occupations:
            occ_data = sector_data[sector_data['occupation'] == occupation]
            year_value_map = {year: 0 for year in years}
            year_value_map.update(dict(zip(occ_data['year'], occ_data['value'])))

            fig.add_trace(go.Bar(
                x=years,
                y=[year_value_map[year] for year in years],
                name=f'{sector} - {occupation}',
                hovertemplate='Year: %{x}<br>Value: %{y:.2f}%',
            ))

    fig.update_layout(
        barmode='group',
        xaxis_title='Year',
        yaxis_title='Female Representation (%)',
        yaxis=dict(range=[0, 100], dtick=10),
        template='plotly_white',
        legend_title='Sector & Occupation'
    )
    return fig

app.run(debug=True)
