from dash import Dash, dcc, html
import dash_loading_spinners as dls
import dash_mantine_components as dmc
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
import numpy as np
import base64
import cv2
from datetime import datetime
import psycopg2
from dash.exceptions import PreventUpdate


class Formulaire:
  def __init__(self, Location, TypeOfPermit, TradeAudited, DepartementAuditor, WorkOnSystem, LifeSavingCheck, Conclusion, Methode, Id, Color):
    self.Location = Location
    self.TypeOfPermit = TypeOfPermit
    self.TradeAudited = TradeAudited
    self.DepartementAuditor = DepartementAuditor
    self.WorkOnSystem = WorkOnSystem
    self.LifeSavingCheck = LifeSavingCheck
    self.Conclusion = Conclusion
    self.Methode = Methode
    self.Id = Id
    self.Color = Color
  def Display_values(self):
    print("Location : ", self.Location)
    print("TypeOfPermit : ", self.TypeOfPermit)
    print("TradeAudited : ", self.TradeAudited)
    print("DepartementAuditor : ", self.DepartementAuditor)
    print("WorkOnSystem : ", self.WorkOnSystem)
    print("LifeSavingCheck : ", self.LifeSavingCheck)
    print("Conclusion : ", self.Conclusion)
    print("Methode : ", self.Methode)
    print("Id : ", self.Id)
  
  def Completed(self):
    if self.Location !=0 and  self.TypeOfPermit !=0 and self.TradeAudited  !=0 and self.DepartementAuditor !=0 and self.WorkOnSystem !=0 and self.LifeSavingCheck !=0 and self.Conclusion !=0 and self.Methode !=0 :
      return True
    return False
  
def handel_undec(img_to_Process):
  return "A error occur when detecting your image, try to let no blank in boxes"


###########################################################  BACK END  ##########################################################################################################

def to_db(): 
  try:
    DATABASE_URL = 'postgres://mkmawyghcxwgke:6e9da941fae462fa5e0134ec46138cddf7ad13ec948e1a7fb093a44661d584ff@ec2-52-49-56-163.eu-west-1.compute.amazonaws.com:5432/dnnn5uljq6l3b'
    conn = psycopg2.connect(DATABASE_URL, sslmode='require', user = "mkmawyghcxwgke", port = "5432",password = "6e9da941fae462fa5e0134ec46138cddf7ad13ec948e1a7fb093a44661d584ff")
    cursor = conn.cursor()
    sql = "SELECT * FROM PERMIT_TO_WORK_AUDIT_NOT_VALIDATED ORDER BY DATE DESC LIMIT 1"
    cursor.execute(sql)
    output = cursor.fetchall()
    conn.commit()
    conn.close()
  except:
    return "Error will selecting to PERMIT_TO_WORK_AUDIT_NOT_VALIDATED, please send a mail to the admin"
  output = list(output[0])
  print("---------", output[0])
  in_db = []
  for i in output:
    in_db.append(i.rstrip())
  in_db = tuple(in_db)
  try:
    DATABASE_URL = 'postgres://mkmawyghcxwgke:6e9da941fae462fa5e0134ec46138cddf7ad13ec948e1a7fb093a44661d584ff@ec2-52-49-56-163.eu-west-1.compute.amazonaws.com:5432/dnnn5uljq6l3b'
    conn = psycopg2.connect(DATABASE_URL, sslmode='require', user = "mkmawyghcxwgke", port = "5432",password = "6e9da941fae462fa5e0134ec46138cddf7ad13ec948e1a7fb093a44661d584ff")
    cursor = conn.cursor()
    sql = "INSERT INTO PERMIT_TO_WORK_AUDIT(LOCATION, TYPE_OF_PERMIT, TRADE_AUDITED, DEPARTMENT_OF_AUDITOR, WORK_ON_SYSTEM, LIFE_SAVING_CHECKS, CONCLUSION, DATE) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(sql,in_db)
    print("output added to PERMIT_TO_WORK_AUDIT successfully........")
    conn.commit()
    conn.close()
  except:
    return "Error will insering to PERMIT_TO_WORK_AUDIT, please send a mail to the admin"
  try:
    DATABASE_URL = 'postgres://mkmawyghcxwgke:6e9da941fae462fa5e0134ec46138cddf7ad13ec948e1a7fb093a44661d584ff@ec2-52-49-56-163.eu-west-1.compute.amazonaws.com:5432/dnnn5uljq6l3b'
    conn = psycopg2.connect(DATABASE_URL, sslmode='require', user = "mkmawyghcxwgke", port = "5432",password = "6e9da941fae462fa5e0134ec46138cddf7ad13ec948e1a7fb093a44661d584ff")
    cursor = conn.cursor()
    sql = "DROP TABLE IF EXISTS PERMIT_TO_WORK_AUDIT_NOT_VALIDATED"
    cursor.execute(sql)
    print("PERMIT_TO_WORK_AUDIT_NOT_VALIDATED Table droped successfully........")
    conn.commit()
    conn.close()
  except:
    return "error wiil droping PERMIT_TO_WORK_AUDIT_NOT_VALIDATED, please send a mail to the admin"
  to_parsed_db()
  return "database updated, thank you."

def to_db_not_val(output):
  try:
    DATABASE_URL = 'postgres://mkmawyghcxwgke:6e9da941fae462fa5e0134ec46138cddf7ad13ec948e1a7fb093a44661d584ff@ec2-52-49-56-163.eu-west-1.compute.amazonaws.com:5432/dnnn5uljq6l3b'

    conn = psycopg2.connect(DATABASE_URL, sslmode='require', user = "mkmawyghcxwgke", port = "5432",password = "6e9da941fae462fa5e0134ec46138cddf7ad13ec948e1a7fb093a44661d584ff")
    cursor = conn.cursor()


    sql ='''CREATE TABLE PERMIT_TO_WORK_AUDIT_NOT_VALIDATED(
       LOCATION CHAR(500) NOT NULL,
       TYPE_OF_PERMIT CHAR(200) NOT NULL,
       TRADE_AUDITED CHAR(200) NOT NULL,
       DEPARTMENT_OF_AUDITOR CHAR(200) NOT NULL,
       WORK_ON_SYSTEM CHAR(200) NOT NULL,
       LIFE_SAVING_CHECKS CHAR(200) NOT NULL,
       CONCLUSION CHAR(200) NOT NULL,
       DATE CHAR(200) NOT NULL

    )'''
    cursor.execute(sql)
    print("PERMIT_TO_WORK_AUDIT_NOT_VALIDATED Table created successfully")
    conn.commit()
    #Closing the connection
    conn.close()
  except:
    return html.H1("error will creating PERMIT_TO_WORK_AUDIT_NOT_VALIDATED, please send a mail to the admin")
  
  try:
    DATABASE_URL = 'postgres://mkmawyghcxwgke:6e9da941fae462fa5e0134ec46138cddf7ad13ec948e1a7fb093a44661d584ff@ec2-52-49-56-163.eu-west-1.compute.amazonaws.com:5432/dnnn5uljq6l3b'
    conn = psycopg2.connect(DATABASE_URL, sslmode='require', user = "mkmawyghcxwgke", port = "5432",password = "6e9da941fae462fa5e0134ec46138cddf7ad13ec948e1a7fb093a44661d584ff")
    cursor = conn.cursor()
    output = list(output)
    
    output[4] = output[4].replace("[","")
    output[4] = output[4].replace("]","")
    output[4] = output[4].replace("'","")
    output[4] = output[4].replace(","," /")
    
    output[3] = output[3].replace("[","")
    output[3] = output[3].replace("]","")
    output[3] = output[3].replace("'","")
    output[3] = output[3].replace(","," /")
    output = tuple(output)
    print(output, " will be added to PERMIT_TO_WORK_AUDIT_NOT_VALIDATED")
    sql = "INSERT INTO PERMIT_TO_WORK_AUDIT_NOT_VALIDATED(LOCATION, TYPE_OF_PERMIT, TRADE_AUDITED, DEPARTMENT_OF_AUDITOR,WORK_ON_SYSTEM ,LIFE_SAVING_CHECKS,CONCLUSION,DATE) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(sql,output) 
    #('Tyra', 'Hot Work - Non-Naked flame', 'Deck', 'RSES / Work on system/equipment that invole inhibits - Yes', 'Work at height - Yes / Confined space - Yes / Lifting operation - No / Hot Work - Naked flame - No / Work on isolated electrical systems - NA / Work on isolated process systems - NA', 'Yellow', '2022-3-23 10:48:13')
    conn.commit()
    print("added to PERMIT_TO_WORK_AUDIT_NOT_VALIDATED successfully")
    conn.close()
  except:
    return "error will adding to PERMIT_TO_WORK_AUDIT_NOT_VALIDATED, please send a mail to the admin"
  

 
def to_db_with_dropdown(v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12): 
  now = datetime.now()
  today = str(now.year) + "-" + str(now.month) + "-" + str(now.day) + " " +str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
  output = [v1,v2,v3,v4,v5,"['"+"Work at height - "+str(v6)+"', '"+"Confined space - "+str(v7)+"', '"+"Lifting operation - "+str(v8)+"', '"+"Hot Work - Naked flame - "+str(v9)+"', '"+"Work on isolated electrical systems - "+str(v10)+"', '"+"Work on isolated process systems - "+str(v11)+"']",v12,today]
  print("---------", output)
  in_db = []
  for i in output:
    in_db.append(i)
  in_db = tuple(in_db)
  print(len(in_db))
  try:
    DATABASE_URL = 'postgres://mkmawyghcxwgke:6e9da941fae462fa5e0134ec46138cddf7ad13ec948e1a7fb093a44661d584ff@ec2-52-49-56-163.eu-west-1.compute.amazonaws.com:5432/dnnn5uljq6l3b'
    conn = psycopg2.connect(DATABASE_URL, sslmode='require', user = "mkmawyghcxwgke", port = "5432",password = "6e9da941fae462fa5e0134ec46138cddf7ad13ec948e1a7fb093a44661d584ff")
    cursor = conn.cursor()
    sql = "INSERT INTO PERMIT_TO_WORK_AUDIT(LOCATION, TYPE_OF_PERMIT, TRADE_AUDITED, DEPARTMENT_OF_AUDITOR, WORK_ON_SYSTEM, LIFE_SAVING_CHECKS, CONCLUSION, DATE) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(sql,in_db)
    print("output added to PERMIT_TO_WORK_AUDIT successfully........")
    conn.commit()
    conn.close()
  except:
    return "Error on insert from dropdown"
  try:
    DATABASE_URL = 'postgres://mkmawyghcxwgke:6e9da941fae462fa5e0134ec46138cddf7ad13ec948e1a7fb093a44661d584ff@ec2-52-49-56-163.eu-west-1.compute.amazonaws.com:5432/dnnn5uljq6l3b'
    conn = psycopg2.connect(DATABASE_URL, sslmode='require', user = "mkmawyghcxwgke", port = "5432",password = "6e9da941fae462fa5e0134ec46138cddf7ad13ec948e1a7fb093a44661d584ff")
    cursor = conn.cursor()
    sql = "DROP TABLE IF EXISTS PERMIT_TO_WORK_AUDIT_NOT_VALIDATED"
    cursor.execute(sql)
    print("PERMIT_TO_WORK_AUDIT_NOT_VALIDATED Table droped successfully........")
    conn.commit()
    conn.close()
  except:
    return "error wiil droping PERMIT_TO_WORK_AUDIT_NOT_VALIDATED, please send a mail to the admin"
  return "database updated, thank you."


def to_parsed_db():

    DATABASE_URL = 'postgres://mkmawyghcxwgke:6e9da941fae462fa5e0134ec46138cddf7ad13ec948e1a7fb093a44661d584ff@ec2-52-49-56-163.eu-west-1.compute.amazonaws.com:5432/dnnn5uljq6l3b'

    conn = psycopg2.connect(DATABASE_URL, sslmode='require', user = "mkmawyghcxwgke", port = "5432",password = "6e9da941fae462fa5e0134ec46138cddf7ad13ec948e1a7fb093a44661d584ff")
    cursor = conn.cursor()
    sql = "SELECT * FROM PERMIT_TO_WORK_AUDIT LIMIT 1"
    cursor.execute(sql)
    out = cursor.fetchall()
    conn.commit()
    #Closing the connection
    conn.close()

    out = pd.DataFrame(out)
    to_delete = []
    for ind,row in out.iterrows():
      if (len((str(row[5]).rstrip())) < 185):
        to_delete.append(int(ind))
      for i in range(0,7):
          if str(row[i].rstrip()) == '0':
            to_delete.append(int(ind))
    out = out.drop(index = to_delete)
    
    conn = psycopg2.connect(DATABASE_URL, sslmode='require', user = "mkmawyghcxwgke", port = "5432",password = "6e9da941fae462fa5e0134ec46138cddf7ad13ec948e1a7fb093a44661d584ff")
    cursor = conn.cursor()

    sql ='''CREATE TABLE IF NOT EXISTS PERMIT_TO_WORK_AUDIT_PARSED(    LOCATION CHAR(50) ,
                                                                TYPE_OF_PERMIT CHAR(250) ,
                                                                TRADE_AUDITED CHAR(250) ,
                                                                DEPARTMENT_OF_AUDITOR CHAR(200) ,
                                                                WORK_ON_SYSTEM CHAR(200) ,
                                                                LIFE_SAVING_CHECKS_W_AT_H CHAR(10) ,
                                                                LIFE_SAVING_CHECKS_C_S CHAR(10) ,
                                                                LIFE_SAVING_CHECKS_L_O CHAR(10) ,
                                                                LIFE_SAVING_CHECKS_H_N CHAR(10) ,
                                                                LIFE_SAVING_CHECKS_W_E_S CHAR(10) ,
                                                                LIFE_SAVING_CHECKS_W_I_S CHAR(10) ,
                                                                CONCLUSION CHAR(100) ,
                                                                DATE CHAR(200) 
                                                                )'''
    cursor.execute(sql)
    print("Table created successfully........")
    conn.commit()

    conn.close()

    conn = psycopg2.connect(DATABASE_URL, sslmode='require', user = "mkmawyghcxwgke", port = "5432",password = "6e9da941fae462fa5e0134ec46138cddf7ad13ec948e1a7fb093a44661d584ff")
    cursor = conn.cursor()

    sql = '''INSERT INTO PERMIT_TO_WORK_AUDIT_PARSED(LOCATION ,
                                                    TYPE_OF_PERMIT  ,
                                                    TRADE_AUDITED  ,
                                                    DEPARTMENT_OF_AUDITOR ,
                                                    WORK_ON_SYSTEM ,
                                                    LIFE_SAVING_CHECKS_W_AT_H  ,
                                                    LIFE_SAVING_CHECKS_C_S ,
                                                    LIFE_SAVING_CHECKS_L_O  ,
                                                    LIFE_SAVING_CHECKS_H_N ,
                                                    LIFE_SAVING_CHECKS_W_E_S  ,
                                                    LIFE_SAVING_CHECKS_W_I_S  ,
                                                    CONCLUSION  ,
                                                    DATE)
                                                    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                                                    '''


    line_to_add = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for ind, row in out.iterrows():
        line_to_add[0] = row[0].rstrip()
        line_to_add[1] = row[1].rstrip()
        line_to_add[2] = row[2].rstrip()
        line_to_add[3] = row[3].rstrip()
        line_to_add[4] = row[4].rstrip()
        W_AT_H = row[5].replace("]","").replace("[","").replace("'","").replace("-","").split(",")[0][-3:].replace(" ","").rstrip()
        C_S = row[5].replace("]","").replace("[","").replace("'","").replace("-","").split(",")[1][-3:].replace(" ","").rstrip()
        L_O = row[5].replace("]","").replace("[","").replace("'","").replace("-","").split(",")[2][-3:].replace(" ","").rstrip()
        H_N = row[5].replace("]","").replace("[","").replace("'","").replace("-","").split(",")[3][-3:].replace(" ","").rstrip()
        W_E_S = row[5].replace("]","").replace("[","").replace("'","").replace("-","").split(",")[4][-3:].replace(" ","").rstrip()
        W_I_S = row[5].replace("]","").replace("[","").replace("'","").replace("-","").split(",")[5].rstrip()[-3:].replace(" ","")
        line_to_add[5] = W_AT_H
        line_to_add[6] = C_S
        line_to_add[7] = L_O
        line_to_add[8] = H_N
        line_to_add[9] = W_E_S
        line_to_add[10] = W_I_S
        line_to_add[11] = row[6].rstrip()
        line_to_add[12] = row[7].rstrip()
        cursor.execute(sql,line_to_add)
        print("row added successfully........")
    conn.commit()
    #Closing the connection
    conn.close()

def backend(img_to_Process):
    try:
      DATABASE_URL = 'postgres://mkmawyghcxwgke:6e9da941fae462fa5e0134ec46138cddf7ad13ec948e1a7fb093a44661d584ff@ec2-52-49-56-163.eu-west-1.compute.amazonaws.com:5432/dnnn5uljq6l3b'
      conn = psycopg2.connect(DATABASE_URL, sslmode='require', user = "mkmawyghcxwgke", port = "5432",password = "6e9da941fae462fa5e0134ec46138cddf7ad13ec948e1a7fb093a44661d584ff")
      cursor = conn.cursor()
      sql = "DROP TABLE IF EXISTS PERMIT_TO_WORK_AUDIT_NOT_VALIDATED;"
      cursor.execute(sql)
      print("Table droped successfully........")
      conn.commit()
      #Closing the connection
      conn.close()
    except:
      return "Database not working, please send a mail to the admin"

    im_bytes = base64.b64decode(img_to_Process.split(",")[1])
    im_arr = np.frombuffer(im_bytes, dtype=np.uint8)
    img = cv2.imdecode(im_arr,0)
    img_to_Process =img


    methods = ['cv2.TM_CCOEFF']
    patterns = ["assets/location.jpg","assets/TypeOfPermit.jpg","assets/TradeAudited.jpg","assets/DepartementAuditor.jpg","assets/AuditAssessement.jpg","assets/LifeSavingCheck.jpg"]
    for meth in methods:
      formu = Formulaire(0,0,0,0,0,[0],0,meth,1,0)
      for pattern in patterns:
        try:
          img = img_to_Process
          down_width = 562
          down_height = 792
          down_points = (down_width, down_height)
          img = cv2.resize(img, down_points, interpolation= cv2.INTER_LINEAR)

          iw, ih = img.shape[::-1]
          
          ## Deleted Header
          template_head = cv2.imread("assets/header.jpg",0)
          w, h = template_head.shape[::-1]


          method = eval('cv2.TM_CCOEFF')

          res = cv2.matchTemplate(img,template_head,method)
          min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

          top_left = max_loc

          bottom_right = (top_left[0] + w, top_left[1] + h)

          img = img[bottom_right[1]:ih,top_left[0]:bottom_right[0]]

          ## detecte pattern

          template_part = cv2.imread(pattern,0)
          w, h = template_part.shape[::-1]


          method = eval(meth)

          res = cv2.matchTemplate(img,template_part,method)
          min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)


          if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
              top_left = min_loc
          else:
              top_left = max_loc

          bottom_right = (top_left[0] + w, top_left[1] + h)
          if pattern == "assets/LifeSavingCheck.jpg":
            ######################################################## TO HANDLE multi select
            r = [53,81,70,98,92,119,107,137,130,165,160,195]
            temp_LifeSavingCheck = []
            cropped_image = img[top_left[1]:bottom_right[1],top_left[0]:bottom_right[0]]
            for i in range(0,len(r),2):
              img = cropped_image
              w, h = img.shape[::-1]
              cropped_image_zoom = img[r[i]:r[i+1],0:w]
              ## detecte circle in pattern
              circle = "assets/circle.jpg"
              template = cv2.imread(circle,0)
              w, h = template.shape[::-1]
              method = eval(meth)
              res = cv2.matchTemplate(cropped_image_zoom,template,method)
              min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

              if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
                  top_left = min_loc
              else:
                  top_left = max_loc
              print("Life :",top_left[0])
              if i == 0:
                if top_left[0] > 135 and top_left[0] < 160:
                  temp_LifeSavingCheck.append("Work at height - NA")
                elif top_left[0] > 162 and top_left[0] < 195:
                  temp_LifeSavingCheck.append("Work at height - Yes")
                elif top_left[0] > 196:
                  temp_LifeSavingCheck.append("Work at height - No")
              elif i == 2:
                if top_left[0] > 135 and top_left[0] < 160:
                  temp_LifeSavingCheck.append("Confined space - NA")
                elif top_left[0] > 162 and top_left[0] < 195:
                  temp_LifeSavingCheck.append("Confined space - Yes")
                elif top_left[0] > 196:
                  temp_LifeSavingCheck.append("Confined space - No")
              elif i == 4:
                if top_left[0] > 135 and top_left[0] < 160:
                  temp_LifeSavingCheck.append("Lifting operation - NA")
                elif top_left[0] > 162 and top_left[0] < 195:
                  temp_LifeSavingCheck.append("Lifting operation - Yes")
                elif top_left[0] > 196:
                  temp_LifeSavingCheck.append("Lifting operation - No")
              elif i == 6:
                if top_left[0] > 135 and top_left[0] < 160:
                  temp_LifeSavingCheck.append("Hot Work - Naked flame - NA")
                elif top_left[0] > 162 and top_left[0] < 195:
                  temp_LifeSavingCheck.append("Hot Work - Naked flame - Yes")
                elif top_left[0] > 196:
                  temp_LifeSavingCheck.append("Hot Work - Naked flame - No")
              elif i == 8:
                if top_left[0] > 135 and top_left[0] < 160:
                  temp_LifeSavingCheck.append("Work on isolated electrical systems - NA")
                elif top_left[0] > 162 and top_left[0] < 195:
                  temp_LifeSavingCheck.append("Work on isolated electrical systems - Yes")
                elif top_left[0] > 196:
                  temp_LifeSavingCheck.append("Work on isolated electrical systems - No")
              elif i == 10:
                if top_left[0] > 135 and top_left[0] < 160:
                  temp_LifeSavingCheck.append("Work on isolated process systems - NA")
                elif top_left[0] > 162 and top_left[0] < 195:
                  temp_LifeSavingCheck.append("Work on isolated process systems - Yes")
                elif top_left[0] > 196:
                  temp_LifeSavingCheck.append("Work on isolated process systems - No")
              else :
                formu.LifeSavingCheck = "Undetected"
            formu.LifeSavingCheck = temp_LifeSavingCheck
            break
            
          elif pattern == "assets/DepartementAuditor.jpg":
            r = [1,61,69,100]
            temp_DepartementAuditor = [0,0]
            cropped_image = img[top_left[1]:bottom_right[1],top_left[0]:bottom_right[0]]
            for i in range(0,len(r),2):
              img = cropped_image
              w, h = img.shape[::-1]
              cropped_image_zoom = img[r[i]:r[i+1],0:w]
              ## detecte circle in pattern
              circle = "assets/circle.jpg"
              template = cv2.imread(circle,0)
              w, h = template.shape[::-1]
              method = eval(meth)
              res = cv2.matchTemplate(cropped_image_zoom,template,method)
              min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

              if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
                  top_left = min_loc
              else:
                  top_left = max_loc
              print("Dep :",top_left[0])
              if i == 0:
                  if  top_left[1] <= 25 :
                    if  top_left[0] >= 5 and top_left[0] <=80:
                      temp_DepartementAuditor[0] = "Maintenance"
                    elif  top_left[0] >= 100 and top_left[0] <=170:
                      temp_DepartementAuditor[0] = "Deck"
                    elif top_left[0] >= 180 and top_left[0] <=240:
                      temp_DepartementAuditor[0] = "Production"
                    elif  top_left[0] >= 250 and top_left[0] <=330:
                      temp_DepartementAuditor[0] = "Well Services"
                    elif top_left[0] >= 340 and top_left[0] <=450:
                      temp_DepartementAuditor[0] = "HSE"

                  elif top_left[1] > 25:
                    if top_left[0] >= 10 and top_left[0] <=80:
                      temp_DepartementAuditor[0] = "Catering"
                    elif top_left[0] >= 85 and top_left[0] <=165:
                      temp_DepartementAuditor[0] = "Campaign"
                    elif top_left[0] >= 166 and top_left[0] <=240:
                      temp_DepartementAuditor[0] = "RSES"
                    elif top_left[0] >= 250 and top_left[0] <=320:
                      temp_DepartementAuditor[0] = "Visitor"
                    elif  top_left[0] >= 330 and top_left[0] <=450:
                      temp_DepartementAuditor[0] = "Other"
                  else :
                      temp_DepartementAuditor[0] = "Undetected"
              elif i == 2:
                if top_left[0] <= 405:
                      temp_DepartementAuditor[1] = "Yes"
                else:
                      temp_DepartementAuditor[1] = "No"
            formu.DepartementAuditor = temp_DepartementAuditor[0]
            formu.WorkOnSystem = temp_DepartementAuditor[1]

            
            ########################################################
          else:
            cropped_image = img[top_left[1]:bottom_right[1],top_left[0]:bottom_right[0]]
          
          ## detecte circle in pattern
          circle = "assets/circle.jpg"
          img = cropped_image
      
          template = cv2.imread(circle,0)
          w, h = template.shape[::-1]

        
          method = eval(meth)
          res = cv2.matchTemplate(img,template,method)
          min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)


          if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
              top_left = min_loc
          else:
              top_left = max_loc

          bottom_right = (top_left[0] + w, top_left[1] + h)

          ## correlate position of circel and value

          if pattern == "assets/location.jpg":
            print("loc ",top_left[0])
            if top_left[0] >= 1 and top_left[0] <=50 :
              formu.Location = "Dan"
            elif top_left[0] >= 51 and top_left[0] <=120 :
              formu.Location = "Gorm"
            elif top_left[0] >= 125 and top_left[0] <=170:
              formu.Location = "Skjold"
            elif top_left[0] >= 171 and top_left[0] <=230 :
              formu.Location = "Halfdan B" 
            elif   top_left[0] >= 240 and top_left[0] <=340:
              formu.Location = "Halfdan A" 
            elif  top_left[0] >= 341 and top_left[0] <=410:
              formu.Location = "Harald"
            elif  top_left[0] >= 411 and top_left[0] <=490 :
              formu.Location = "Tyra"
            else :
              formu.Location = "Undetected"
              


          


          if pattern == "assets/TradeAudited.jpg": 
            print("Trad ",top_left[0])
            if top_left[1] < 25 and bottom_right[1] < 55:
              if  top_left[0] >= 5 and top_left[0] <=25 and bottom_right[0] >= 10 and bottom_right[0] <= 55:
                formu.TradeAudited = "Maintenance"
              elif  top_left[0] >= 80 and top_left[0] <=150 and bottom_right[0] >= 110  and bottom_right[0] <= 190:
                formu.TradeAudited = "Deck"
              elif top_left[0] >= 180 and top_left[0] <=260 and bottom_right[0] >= 210  and bottom_right[0] <= 300:
                formu.TradeAudited = "Production"
              elif top_left[0] >= 280 and top_left[0] <=400 and bottom_right[0] >= 320  and bottom_right[0] <= 410:
                formu.TradeAudited = "Well Services"
            elif top_left[1] > 28 and bottom_right[1] > 58:
              if top_left[0] >= 30 and top_left[0] <=110 and bottom_right[0] >=  35  and bottom_right[0] <= 135:
                formu.TradeAudited = "Campaign"
              else:
                formu.TradeAudited = "Others"
            else :
              formu.TradeAudited = "Undetected"



          if pattern == "assets/TypeOfPermit.jpg":
            print("Type ",top_left[0])
            if bottom_right[1] >= 30 and bottom_right[1] <= 52 and top_left[1] >= 10 and top_left[1] <= 27:

              if  top_left[0] >= 10 and top_left[0] <=100 and bottom_right[0] >= 20 and bottom_right[0] <= 110:
                formu.TypeOfPermit = "Hot Work - Naked flame"
              elif  top_left[0] >= 110 and top_left[0] <=300 and bottom_right[0] >= 115 and bottom_right[0] <= 335:
                formu.TypeOfPermit = "Hot Work - Non-Naked flame"
              elif top_left[0] >= 310 and top_left[0] <=370 and bottom_right[0] >= 340 and bottom_right[0] <= 400:
                formu.TypeOfPermit = "Cold Work"

            elif top_left[1] >= 30 and top_left[1] <= 60 and bottom_right[1] >= 55 and bottom_right[1] <= 100:

              if top_left[0] >= 8 and top_left[0] <=100 and bottom_right[0] >= 10 and bottom_right[0] <= 160:
                formu.TypeOfPermit = "Breaking of containment"
              elif top_left[0] >= 110 and top_left[0] <=300 and bottom_right[0] >= 170 and bottom_right[0] <= 300:
                formu.TypeOfPermit = "Template PTW/Runtime Permit"
              elif top_left[0] >= 310 and top_left[0] <=370 and bottom_right[0] >= 310 and bottom_right[0] <= 450:
                formu.TypeOfPermit = "Confined space entry"

            else :
              formu.TypeOfPermit = "Undetected"


          if pattern == "assets/AuditAssessement.jpg":
            print("Audit ",top_left[0])
            if top_left[1] <= 55 and bottom_right[1] <= 90 :
              formu.Conclusion = "Green"
            elif top_left[1] >= 56 and top_left[1] <= 115 and  bottom_right[1] >= 95 and bottom_right[1] <= 134 :
              formu.Conclusion = "Yellow"
            elif top_left[1] >= 116 and  bottom_right[1] >= 135  :
              formu.Conclusion = "Red"
            else :
              formu.Conclusion = "Undetected"
        except:
            return "A error occur when matching your image please upload a better image"
               

    now = datetime.now()
    today = str(now.year) + "-" + str(now.month) + "-" + str(now.day) + " " +str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
    formu.Id = str(today)
    
    output = [str(formu.Location),str(formu.TypeOfPermit),str(formu.TradeAudited),str(formu.DepartementAuditor),str(formu.WorkOnSystem),str(formu.LifeSavingCheck),str(formu.Conclusion),formu.Id]
    print("out from BE :",output)

    return output





############################################################### FRONT END ###################################################################################################


#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__)#, external_stylesheets=external_stylesheets)
server = app.server


app.layout = html.Div([
    html.Div([
      html.Img(src=app.get_asset_url('logo.png'), style={ 'width': '248',
                                                                    'height': '227',
                                                                     'position': 'relative',
                                                                      'left': '75%'}),
                  html.Span("TotalEnergies EP Danmark A/S",style={    'fontSize': '25px',
    'position': 'absolute',
    'left': '3%',
    'top': '27%',
    'color': 'aliceblue'}),
                  html.Span("Permit to Work Audit",style={    'fontSize': '70px',
    'position': 'absolute',
    'left': '3%',
    'top': '42%',
    'color': 'aliceblue'})],
            style={'background' : '#087dc2', 'height' : '228px', 'width': '100vw','position': 'sticky','top': '0','z-index': '6000'}),
  
    html.H2("Upload your permit to work audit, check information and send it to our database", style = {
            'font-size': 'xxx-large',
            'margin': '30px'
    }),
    dcc.Upload(
        id='upload-image',className="up",
        children=html.Div([
            'Take or upload a photo',
            html.Div(),
            html.Div(html.Img(src=app.get_asset_url('camera-to-take-photos.png'), style={ 'width': '10vh',
                                                                                          'left' : "20%",
                                                                                          'top' : "30%",
                                                                                          'position': 'absolute'
                                                                    })),
            html.Div(html.Img(src=app.get_asset_url('folder.png'), style={                'width': '10vh',
                                                                                          'left' : "65%",
                                                                                          'top' : "30%",
                                                                                          'position': 'absolute'
                                                                    }))
        ]),
        style={
            'height': '15vh',
            'width': '94vw',
            'lineHeight': '80px',
            'borderWidth': '5px',
            'borderStyle': 'dashed',
            'borderColor':  '#CDF3FF',
            'borderRadius': '5px',
            'textAlign': 'center',
            'fontSize': '70px',
            'marginLeft': '26px',
        },        
      # Allow multiple files to be uploaded
        multiple=True

    ),
    
                    dls.DualRing(
                        html.Div(id="loading-output-1"),
                        color="red",
                        width = 250,
                        thickness = 15,
                        
                    ),
    html.Div(id='output-image-upload'),
    html.Button([
        html.Div(html.Span(html.P("Confirmation"))),
        html.Div(html.Span(html.P("Data uploaded")))
        
        ],
        
        id='submit-button-result', type='submit',
        style={},
    
    ),
    html.Div(id='output_div-toDB'),
    html.Div([
                dcc.Dropdown(["placeholder"],'placeholder',id='dropdown-loc'),
                dcc.Dropdown(["placeholder"],'placeholder',id='dropdown-type'),
                dcc.Dropdown(["placeholder"],'placeholder',id='dropdown-trade'),
                dcc.Dropdown(["placeholder"],'placeholder',id='dropdown-dep'),
                dcc.Dropdown(["placeholder"],'placeholder',id='dropdown-inib'),
                dcc.Dropdown(["placeholder"],'placeholder',id='dropdown-lsc0'),
                dcc.Dropdown(["placeholder"],'placeholder',id='dropdown-lsc1'),
                dcc.Dropdown(["placeholder"],'placeholder',id='dropdown-lsc2'),
                dcc.Dropdown(["placeholder"],'placeholder',id='dropdown-lsc3'),
                dcc.Dropdown(["placeholder"],'placeholder',id='dropdown-lsc4'),
                dcc.Dropdown(["placeholder"],'placeholder',id='dropdown-lsc5'),
                dcc.Dropdown(["placeholder"],'placeholder',id='dropdown-conc'),
                dcc.Dropdown(["DATE"],'DATE',id='dropdown-date')
      ],id = "displaynone",style = dict(display = 'none')),
    
  
    html.Div([html.Ul([html.Li(),html.Li(),html.Li(),html.Li(),html.Li(),html.Li(),html.Li(),html.Li(),html.Li(),html.Li()],className="circles")],className="area",id = 'ghost_circle', style = dict()),
])


def parse_contents(contents):
    out = backend(contents)
    for x in out:
      if x == "Undetected":
        return "Something went wrong during the process, please take another picture. Look at a exeample if needed"
    to_db_not_val(out)
    return out
    
    


@app.callback(Output('output-image-upload', 'children'),
              Input('upload-image', 'contents'))
def update_output(list_of_contents):
    if list_of_contents is not None:
        children = [
            parse_contents(c) for c,in
            zip(list_of_contents)]
        if len(children[0]) > 10:
          return html.H4("".join(children[0]))     
        to_show = ["Location ","Type of Permit ","Trade Audited ","Department of Auditor ","Work on system / Equipment that involve inhibits ","Life Saving Checks ","Audit Assessement ","Date of uploading "]

        children[0][5] = children[0][5].replace("[","").replace("]","").replace("'","")
        tmp_LSC = children[0][5].split(",")
        LSC = []
        for l in tmp_LSC:
            LSC.append(l[-3:].replace(" ",""))
        
        return  html.Ul([html.Li(x) for x in [
                html.Div([html.Span(to_show[0],style={'fontWeight': 'bold', 'marginRight' : '1em'}),html.Span(dcc.Dropdown(['Dan', 'Gorm', 'Skjold','Halfdan B',"Halfdan A","Harald",'Tyra'], children[0][0], id='dropdown-loc'),style = dict(verticalAlign = 'top'))]),
                html.Div([html.Span(to_show[1],style={'fontWeight': 'bold', 'marginRight' : '1em'}),html.Span(dcc.Dropdown(['Hot Work - Naked flame', 'Hot Work - Non-Naked flame', 'Cold Work','Breaking of containment','Template PTW/Runtime Permit','Confined space entry'], children[0][1], id='dropdown-type'),style = dict(verticalAlign = 'top'))]),
                html.Div([html.Span(to_show[2],style={'fontWeight': 'bold', 'marginRight' : '1em'}),html.Span(dcc.Dropdown(['Maintenance', 'Deck', 'Production',"Well Services","Campaign","Others"], children[0][2], id='dropdown-trade'),style = dict(verticalAlign = 'top'))]),
                html.Div([html.Span(to_show[3],style={'fontWeight': 'bold', 'marginRight' : '1em'}),html.Span(dcc.Dropdown(['Maintenance', 'Deck', 'Production',"Well Services","HSE","Catering","Campaign","RSES","Visitor","Other"], children[0][3], id='dropdown-dep'),style = dict(verticalAlign = 'top'))]),
                html.Div([html.Span(to_show[4],style={'fontWeight': 'bold', 'marginRight' : '1em'}),html.Div(dcc.Dropdown(['Yes', 'No'], children[0][4], id='dropdown-inib'),style = dict(verticalAlign = 'top'))]),
                html.Div([html.Span(to_show[5],style={'fontWeight': 'bold', 'marginRight' : '1em'}),html.Div([dcc.Dropdown(['Yes', 'No', 'NA'], LSC[0], id='dropdown-lsc0'),dcc.Dropdown(['Yes', 'No', 'NA'], LSC[1], id='dropdown-lsc1'),dcc.Dropdown(['Yes', 'No', 'NA'], LSC[2], id='dropdown-lsc2'),dcc.Dropdown(['Yes', 'No', 'NA'], LSC[3], id='dropdown-lsc3'),dcc.Dropdown(['Yes', 'No', 'NA'], LSC[4], id='dropdown-lsc4'),dcc.Dropdown(['Yes', 'No', 'NA'], LSC[5], id='dropdown-lsc5')],style = dict(verticalAlign = 'top'))]),
                html.Div([html.Span(to_show[6],style={'fontWeight': 'bold', 'marginRight' : '1em'}),html.Span(dcc.Dropdown(['Green', 'Yellow', 'Red'], children[0][6], id='dropdown-conc'),)],style = dict(verticalAlign = 'top')),
                html.Div([html.Span(to_show[-1],style={'fontWeight': 'bold', 'marginRight' : '1em'}),html.Span(children[0][-1])]),
                ]])
                                                  
   
'''      #old way with old func
@app.callback(Output('output_div-toDB', 'children'),
              [Input('submit-button-result', 'n_clicks')])
def update_output_button_toDB(clicks):
    if clicks is not None:
      return to_db()
'''    
@app.callback(Output('output_div-toDB', 'children'),
              Input('submit-button-result', 'n_clicks'),
              Input('dropdown-loc', 'value'),#v1
              Input('dropdown-type', 'value'),#v2
              Input('dropdown-trade', 'value'),#v3
              Input('dropdown-dep', 'value'),#v4
              Input('dropdown-inib', 'value'),#v5
              Input('dropdown-lsc0', 'value'),#v6
              Input('dropdown-lsc1', 'value'),#v7
              Input('dropdown-lsc2', 'value'),#v8
              Input('dropdown-lsc3', 'value'),#v9
              Input('dropdown-lsc4', 'value'),#v10
              Input('dropdown-lsc5', 'value'),#v11
              Input('dropdown-conc', 'value'),#v12
              suppress_callback_exceptions=True
              )
def update_output_button_toDB(clicks,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12):
    if clicks is not None:
        return to_db_with_dropdown(v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12)    

@app.callback(Output('submit-button-result', 'style'),
              Input('upload-image', 'contents'))
def update_output_hid(list_of_contents):
    if list_of_contents is not None:
        style = dict(
                    width= '700vw',
                    height= '250px',
                    fontSize= '70px',
                    position= 'relative',
                    top= '-20px',
                    left= '15vw',
                    textAlign= 'center',
                    marginTop= '40px'
                   ) 
        return style
    else:
        return dict(display = 'none')             

@app.callback(
    Output('dropdown-conc','style'),
    [Input('dropdown-conc','value')])
def color_text(asses_text):
    output = asses_text
    if output == "Green":
        style = dict(color = 'green', fontWeight = 'bold')
        return style
    elif output == "Yellow":
        style = dict(color = 'yellow', fontWeight = 'bold')
        return style
    else:
        style = dict(color = 'Red', fontWeight = 'bold')
        return style

@app.callback(
    Output("loading-output-1", "children"),
    Input("upload-image", "contents"),
)
def func(content):
    if content is not None:
        time.sleep(8)
@app.callback(Output('ghost_circle', 'style'),
              Input('upload-image', 'contents'))
def update_output_ghost_circle(list_of_contents):
    if list_of_contents is not None:
        return  dict(display = 'none')
    else:
        return dict() 
      
if __name__ == '__main__':
  app.run_server(debug = False)
