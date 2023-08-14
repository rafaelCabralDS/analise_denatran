import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import numpy as np

# Carregar os dados do arquivo CSV
df = pd.read_csv('C:\\Users\Admin\Meu Drive\Mestrado\[4] Ciência de Dados\datatran2016.csv', delimiter=';', decimal=',')
df_radares = pd.read_csv('C:\\Users\Admin\Meu Drive\Mestrado\[4] Ciência de Dados\dados_dos_radares.csv', delimiter=';', decimal=',', encoding = "ISO-8859-1")
df_radares = df_radares[df_radares.ano_do_pnv_snv < 2017]

# Criar um mapa utilizando o Plotly Express
fig = px.scatter_mapbox(
    df, 
    lat='latitude', 
    lon='longitude', 
    size='feridos', 
    color='feridos',
    color_continuous_scale=px.colors.sequential.Viridis,
    size_max=34, 
    zoom=10
)

fig.add_scattermapbox(
    lat=df_radares['latitude'],
    lon=df_radares['longitude'],
    mode='markers',
    marker=dict(size=10, color='red', opacity=0.7),
    name='Radares',
)

# Configurar layout do mapa
fig.update_layout(
    mapbox_style='open-street-map',
    margin=dict(l=0, r=0, t=0, b=0),
    height=800
)

# Inicializar a aplicação Dash
app = dash.Dash(__name__)

# Layout da aplicação
app.layout = html.Div(children=[
    html.H1(children='FERIDOS 2016'),
    dcc.Graph(
        id='acidents-2016',
        figure=fig
    )
])

# Executar a aplicação Dash
if __name__ == '__main__':
    app.run_server(debug=True)
