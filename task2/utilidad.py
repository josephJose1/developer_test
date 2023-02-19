import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from coresite.settings import BASE_DIR
from task2.scraper.pipelines import save_item,count_table
import datetime


def get_cuantity(data):
    '''scrap page to get cuantity of rows for all tables'''
    if data.find("Número de páginas:") != -1:
        text=data.split("Número de páginas: ")
        cuantity=(text[1].split("\n"))[0]
        return cuantity.replace(',','')
    return None

def create_directory(directory):
    '''Generate path in filsystem to store new file'''
    #The getcwd() method of the os module in Python returns a string that contains the 
    # absolute path of the current working directory. The returned string does not include 
    path_find = os.getcwd()
    print("path find", path_find)
    # Parent Directory path
    path = os.path.join(path_find, directory)
    print(f"LA nueva ruta \n {path}")
    try:
        os.mkdir(path)#create  #descomentar linea
    except:
        print("An exception occurred. Probably, the folder already exist. ")
    else:
        print("Creation goes well")
    return path

def save_json(df=None):
    '''save json file in spacific folder inside task2 app '''
    
    pathfolder = 'task2'
    create_directory(pathfolder)
    pathfolder = 'task2/data'
    x = datetime.datetime.now()
    mystr = '-'.join[x.strftime("%d"),x.strftime("%m")]
    mtime = '-'.join[x.strftime("%M"),x.strftime("%S")]
    n = ''.join['data', mystr, mtime]
    filename = '.'.join[n,'json']
    mypath = os.path.join(create_directory(pathfolder), filename)
    # mypath = 'data.json'
    df[-1].to_json(mypath,orient='table')#DATAFRAME TO JSON                   

def main_process():
    '''MAKE REQUEST TO THE URL, SCRAP PAGE, SAVE TR BY ITEMS IN DB'''
    df = []
    mydate = None
    cantidadperpage=10
    base_URL = "https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php"
    
    page = requests.get(base_URL)
    # start_page = count_table(cantidadperpage)+1 #uncomment
    start_page = 1
    if page.status_code == 200:
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find("div",id="info_resultado")
        cuantity=get_cuantity(results.prettify())
        if cuantity is not None:
            cuantity = int(cuantity)
            for table in range(start_page,4):#change 2 _> cuantity
                query_params = f"?_paginador_fila_actual={table}"
                page = requests.get(base_URL + query_params)
                if page.status_code == 200:
                    soup = BeautifulSoup(page.content, "html.parser")
                    results = soup.find('table', class_="tabla_datos")
                    col =[]
                    for td in results.thead.tr:
                        if td.text.strip() != '':
                            col.append(str(td.text.strip()))
                    # Defining of the dataframe
                    df.append(pd.DataFrame(columns=[c for c in col if c != ''])) 
                    for tr in results.tbody.find_all('tr'):
                        coltd=tr.find_all('td') 
                        # Find all data for each column
                        
                        if(coltd != []): #extrac data from components tag                            
                            id = coltd[0].text.strip()
                            name = coltd[1].text.strip()
                            tipo = coltd[2].contents[0].strip('&0.')
                            region = coltd[3].contents[0].strip('&0.')
                            tipologia = coltd[4].contents[0].strip('&0.')
                            
                            try:
                                titular = coltd[5].contents[0].strip('&0.')
                                # print(coltd[5].contents[0])
                            except TypeError:
                                titular = coltd[5].text.strip()
                                
                            inversion = coltd[6].contents[0].strip()
                            date= (coltd[7].contents[0].strip('&0.')).split('/')
                            # mydate = date.split('/')
                            mydate = "-".join([date[2], date[1], date[0]])
                            
                            estado = coltd[8].contents[0].strip('&0.')
                            try:
                                map = coltd[9].a.get('onclick')
                                s1 = map.split('(')
                                s0=s1[1].split(',')  
                                map = 'https://seia.sea.gob.cl' + s0[0].replace("'", '')
                            except AttributeError:
                                map = ''
                            
                            #save details item to pipelines
                            save_item(int(id), name, tipo, region, tipologia, titular, inversion, mydate, estado, map)
                            
                            new_row = pd.Series({
                                            col[0]: int(id), col[1] : name, col[2] : tipo, col[3] : region, col[4] : tipologia,col[5] : titular,col[6] : inversion,col[7] : mydate,col[8] : estado,col[9]: map,})
                            #concat row to df
                            new_df = pd.DataFrame([new_row])
                            df[table-1] = pd.concat([df[table-1], new_df], axis=0, ignore_index=True)
                            pd.concat([df[table-1], new_row.to_frame().T], ignore_index=True)
                if table > start_page:
                    #concat last df with new df 
                    df[table-1] = pd.concat([df[table-2], df[table-1]])
           #save df to json file in certain folder 
            save_json(df)
        else:
            return "PAGE was CHANGED, WE NEED TO UPDATE SCRIPT"