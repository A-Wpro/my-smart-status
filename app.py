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
            "Are your offshore certification still valid ?",
            "Avoid screen before going bed.",
            "Smile :)"
            ]


    
    currDate = datetime.datetime.now()
    currDateMonth = currDate.month
    currDateDay =  currDate.day
    if currDateMonth == 12 and currDateDay > 10 and currDateDay < 25:
        tip = "Cover yourself, winter is comming"
    elif currDateMonth == 5 and currDateDay > 1 and currDateDay < 9:
        tip = "Don't forget interational mother's day !"
    elif currDateMonth == 3 and currDateDay > 1 and currDateDay < 9:
        tip = "Don't forget interational women's day !"
    elif currDateMonth == 11 and currDateDay > 11 and currDateDay < 20:
        tip = "Don't forget interational men's day !"
    elif currDateMonth == 6 and currDateDay > 11 and currDateDay < 20:
        tip = "Don't forget interational father's day !"


    if tip == "":
        i = currDateMonth
        if i > len(tips):
            i = len(tips)
        tip = random.choice(tips)
    return html.Li(tip)

def icon_renderer(user,offline,wifi,g4,VR = 1):
    tmp = []
    tmp1 = []
    if type(user) == str:
        return html.Div(html.Img(src=app.get_asset_url(str(user)+'.png'), style={"maxWidth": "51px", "marginRight": "30px","position" : "relative", "left":"0px", "top":"0vh"}))
    elif user == 0 :
        tmp.append(html.Img(src=app.get_asset_url('all.png'), style={"maxWidth": "51px", "marginRight": "30px","position" : "relative", "left":"235px", "top":"0vh"}))
    elif user == 1:
        tmp.append(html.Img(src=app.get_asset_url('tools.png'),style={"maxWidth": "51px", "marginRight": "30px","position" : "relative", "left":"235px", "top":"0vh"}))
    elif user == 2:
        tmp.append(html.Img(src=app.get_asset_url('oil.png'), style={"maxWidth": "51px", "marginRight": "30px","position" : "relative", "left":"235px", "top":"0vh"}))
    elif user == 3:
        tmp.append(html.Img(src=app.get_asset_url('cranes.png'),style={"maxWidth": "51px", "marginRight": "30px","position" : "relative", "left":"235px", "top":"0vh"}))
    
    if offline == 0:
        tmp1.append(html.Img(src=app.get_asset_url('offline.png'),style={"maxWidth": "51px", "marginRight": "15px","position" : "relative", "left":"40vw", "top":"0vh"}))
    
    if wifi == 0:
        tmp1.append(html.Img(src=app.get_asset_url('wifi.png'),style={"maxWidth": "51px", "marginRight": "15px","position" : "relative", "left":"40vw", "top":"0vh"}))
        
    if g4 == 0:
        tmp1.append(html.Img(src=app.get_asset_url('4g.png'),style={"maxWidth": "51px", "marginRight": "15px","position" : "relative", "left":"40vw", "top":"0vh"}))
        
    if VR == 0:     
        tmp1.append(html.Img(src=app.get_asset_url('vr-glasses.png'),style={"maxWidth": "51px", "marginRight": "15px","position" : "relative", "left":"40vw", "top":"0vh"}))
        
    return html.Div([tmp[0],html.Div(tmp1,style = {"display":"flex"})],style={"display":"flex","maxHeight": "50px", "position":"inherit","left":"250px"})
    
    
############################################################### FRONT END ###################################################################################################



app = Dash(__name__)
server = app.server

app.layout = dbc.Container(
[
      
      html.Div([html.Img(src=app.get_asset_url('header.png'), style={"maxWidth": '100%', "marginBottom": '15px'})]),
      html.Div([#Warning : 
                dbc.Card(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    dbc.CardImg(
                                        src="/assets/warning.png",
                                        className="img-fluid rounded-start",
                                        style = dict(minWidth = "-webkit-fill-available")
                                    ),
                                    className="col-md-4", style = dict(    width = "70px")
                                ),
                                dbc.Col(
                                    dbc.CardBody(
                                        [

                                            html.P(
                                                "Only ATEX approved equipments are authorized at all times."
                                                "This includes devices, headsets and earbuds. ",
                                                
                                                className="card-text",
                                                style = dict(fontSize = "22px")
                                            ),
                                        ],style = {"padding": '0rem 0rem'}
                                    ),
                                    className="col-md-8",
                                ),
                            ],
                            className="g-0 d-flex align-items-center", style = dict(alignContent= 'stretch',
                                                                                    justifyContent= 'space-around',
                                                                                    flexDirection= 'row',
                                                                                    alignItems= 'center')
                        )
                    ],
                    className="mb-3",
                    
                )

                   
                  ]),
      html.Div([
          html.H2("News"),
          html.Div([
           dbc.Card(
                    dbc.CardBody(
                    [
                        html.H4("- 2022-06-05", className="card-title"),
                        html.P(
"Some devices might have out-of-service SIM cards. In case of doubt, contact Telecom team or the field engineer. 4G network is available on Halfdan B. Quality of 4G on other platforms might vary until all platforms are fully 4G-equipped.",
                            
                            className="card-text", style = dict(marginLeft =  '5%', fontSize = '25px')
                        ),

                    ], style = dict()
                    )
                   ),

            ])
        ],style = dict(marginBottom = "20px") 
        ),
    html.Div(       
            dbc.Container(
                    dbc.Accordion(
                        [
                            dbc.AccordionItem(
                                [html.Div(html.P( "● Torben Lauridsen", style = dict(fontSize = "25px",marginLeft = '50px')))],
                                title="● Contact : ",
                                style= dict(fontSize = "25px")
                            ),
                            dbc.AccordionItem(
                                 [
                                 html.Div([
                                     html.Div([
                                         html.P("● mySafety", style = dict(marginRight = "50px")),
                                         html.Div(icon_renderer(0,0,0,0),
                                         style = {"position":"absolute", "left":"0px"})
                                     ],
                                         style = dict(display = 'inline-flex', flexDirection= 'row', marginBottom ="5px")),
                                     html.P("Record your safety observation from the mobile devices. Same application as the desktop-based one",
                                            style= dict(marginLeft = "66px"))
                                 ]),
                                 html.Div([html.Div([html.P("● myTIM", style = dict(marginRight = "50px")),html.Div(icon_renderer(0,0,0,0),style = {"position":"absolute", "left":"0px"})], style = dict(display = 'inline-flex', flexDirection= 'row', marginBottom ="5px")),html.P("Take pictures, and find them back later on myTIM desktop application",style= dict(marginLeft = "66px"))]),
                                 html.Div([html.Div([html.P("● UBIK for FLM rounds", style = dict(marginRight = "50px")),html.Div(icon_renderer(1,1,0,0),style = {"position":"absolute", "left":"0px"})], style = dict(display = 'inline-flex', flexDirection= 'row', marginBottom ="5px")),html.P("FLM rounds",style= dict(marginLeft = "66px"))]),
                                 html.Div([html.Div([html.P("● UBIK for production operator rounds", style = dict(marginRight = "50px")),html.Div(icon_renderer(2,1,0,0),style = {"position":"absolute", "left":"0px"})], style = dict(display = 'inline-flex', flexDirection= 'row', marginBottom ="5px")),html.P("Daily rounds",style= dict(marginLeft = "66px"))]),  
                                 html.Div([html.Div([html.P("● Viibe / MySupport", style = dict(marginRight = "50px")),html.Div(icon_renderer(0,1,0,0,0),style = {"position":"absolute", "left":"0px"})], style = dict(display = 'inline-flex', flexDirection= 'row', marginBottom ="5px")),html.P("Remote collaboration/Visio Conference Apps",style= dict(marginLeft = "66px"))]),
                                 ],  
                                         
                                title="● Supported Apps list :",
                                style= dict(fontSize = "25px")
                            ),
                            dbc.AccordionItem(
                                [
                                html.Div([
                                     html.Div([
                                         html.P("● Teams", style = dict(marginRight = "50px")),
                                         html.Div(icon_renderer("teams",-1,-1,-1))
                                         ],style = dict(display = 'inline-flex', flexDirection= 'row', marginBottom ="5px")
                                         ), 
                                 html.P("Microsoft Teams",
                                 style= dict(marginLeft = "66px"))]), 
                                 
                                html.Div([
                                     html.Div([
                                         html.P("● UBIK for job execution", style = dict(marginRight = "50px")),
                                         html.Div(icon_renderer("SAP",-1,-1,-1))
                                         ],style = dict(display = 'inline-flex', flexDirection= 'row', marginBottom ="5px")
                                         ), 
                                 html.P("",
                                 style= dict(marginLeft = "66px"))]),
                            
                                 html.Div([
                                     html.Div([
                                         html.P("● UBIK for notifications", style = dict(marginRight = "50px")),
                                         html.Div(icon_renderer("SAP",-1,-1,-1))
                                         ],style = dict(display = 'inline-flex', flexDirection= 'row', marginBottom ="5px")
                                         ), 
                                 html.P("",
                                 style= dict(marginLeft = "66px"))]),
                                ],
                                title="● Future apps : ",
                                style= dict(fontSize = "25px")
                            ),
                        ],
                        start_collapsed=False,
                        style= dict(fontSize = "25px")
                                )   
    )),  
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
                                [html.Li(html.A("WE CARE",href = "https://itsm.hubtotal.net/sp")),html.Li(html.A("Permit to work audit",href ="https://permit-to-work-audit.herokuapp.com/"))],
                                title="Usefull link",
                                style= dict(fontSize = "25px")
                            ),

                        ],
                        start_collapsed=True,
                        style= dict(fontSize = "25px")
                                )   
    ),
    style= dict(marginTop = '8vh')
    ),
    html.Div([
    html.H2("Past news"),
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
    ],style = dict(marginTop = '10vh',marginBottom = '10px')),
],
    className="p-5",style= dict(marginTop = '1vh')
)


if __name__ == '__main__':
  app.run_server(debug = False)
