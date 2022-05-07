from dash import Dash, dcc, html
import dash_loading_spinners as dls
import dash_mantine_components as dmc
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime
import psycopg2
from dash.exceptions import PreventUpdate


###########################################################  BACK END  ##########################################################################################################



#wip

############################################################### FRONT END ###################################################################################################



app = Dash(__name__)#, external_stylesheets=external_stylesheets)
server = app.server


app.layout = html.Div("placeholder")


if __name__ == '__main__':
  app.run_server(debug = False)
