from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate


###########################################################  BACK END  ##########################################################################################################

import datetime
import random
def tip_of_the_week():
    tip = ""
    tips =  [
            "We are never too safe !",
            "Always be careful about H2S !",
            "Stay hydrated !",
            "Don't forget your belongings when going back onshore.",
            "Are you ofshore certification still valide ?",
            "Avoid screen before going bed.",
            "Smile :)"


            ]


    
    currDate = datetime.datetime.now()
    currDateMonth = currDate.month
    currDateDay =  currDate.day
    if currDateMonth == 12 and currDateDay > 10 and currDateDay > 25:
        tip = "Cover yourself, winter is comming"
    elif currDateMonth == 5 and currDateDay > 1 and currDateDay > 9:
        tip = "Don't forget interational mother's day !"
    elif currDateMonth == 3 and currDateDay > 1 and currDateDay > 9:
        tip = "Don't forget interational women's day !"
    elif currDateMonth == 11 and currDateDay > 11 and currDateDay > 20:
        tip = "Don't forget interational men's day !"
    elif currDateMonth == 6 and currDateDay > 11 and currDateDay > 20:
        tip = "Don't forget interational father's day !"


    if tip == "":
        i = currDateMonth
        if i > len(tips):
            i = len(tips)
        tip = random.choice(tips)
    return html.Li(tip)

############################################################### FRONT END ###################################################################################################




app = Dash(__name__)
server = app.server

app.layout = dbc.Container(
[
      dbc.Alert("Welcome", color="primary", style = dict(height = '7vh', fontSize = '35px', marginBottom = '5vh')),
      html.Div([
          html.H2("Recent messages"),
           dbc.Card(
                        dbc.CardBody(
                        [
                            html.H4("- 2022-05-30", className="card-title"),
                            html.P(
                                "Dear user, our new app will receive huge improvement in the upcoming month",                                
                                className="card-text", style = dict(marginLeft =  '5%', fontSize = '25px')
                            ),
                            
                        ], style = dict())
                   ),
            dbc.Card(
                    dbc.CardBody(
                    [
                        html.H4("- 2022-05-30", className="card-title"),
                        html.P(
                            "My Smart Status just launch !",
                            className="card-text", style = dict(marginLeft =  '5%', fontSize = '25px')
                        ),
                        
                    ],style = dict()),
                    style = dict(marginTop= '1vh')
                )
        ],style = dict()
        ),
        html.Div(
            dbc.Container(
                    dbc.Accordion(
                        [
                            dbc.AccordionItem(
                                [html.Div(tip_of_the_week())],
                                title="Tip of the week ",
                                style= dict(fontSize = "25px")
                            ),
                            dbc.AccordionItem(
                                [html.Li(html.A("WE CARE",href = "https://itsm.hubtotal.net/sp")),html.Li(html.A("Permit to work audit", href = "https://permit-to-work-audit.herokuapp.com/"))],
                                title="Usefull link",
                                style= dict(fontSize = "25px")
                            ),

                        ],
                        always_open=True,
                        style= dict(fontSize = "25px")
                                )   
    ),
    style= dict(marginTop = '25vh')
    ),
    html.Div([
    html.H2("Past messages"),
        html.Div([
                dbc.Card(
                        dbc.CardBody(
                        [
                            html.H4("- 2022-05-03", className="card-title"),
                            html.P(
                                "Hey, we should create a app this amazing web app",
                                className="card-text", style = dict(marginLeft =  '5%', fontSize = '25px')
                            ),
                            
                        ]),
                        style = dict(marginTop= '1vh')
                    )
            ],style = dict()
            )
    ],style = dict(marginTop = '10vh')),
],
    className="p-5",style= dict(marginTop = '5vh')
)


if __name__ == '__main__':
  app.run_server(debug = False)
