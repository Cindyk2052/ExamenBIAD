#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Aqui se hace la conexion de forma local a mongodb
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from bson import json_util, ObjectId

CLIENT = MongoClient('mongodb://localhost:27017')
try:
    CLIENT.admin.command('ismaster')
    print('MongoDB connection: Success')
except ConnectionFailure as cf:
    print('MongoDB connection: failed', cf)


# In[2]:


import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import pandas as pd
import bson
import json
from bson.raw_bson import RawBSONDocument

def find_2nd(string, substring):
    return string.find(substring, string.find(substring) + 1)
def find_1st(string, substring):
    return string.find(substring, string.find(substring))


# In[5]:


response = requests.get("https://www.tiendeo.com.ec/ofertas-catalogos/zara")
soup = BeautifulSoup(response.content, "lxml")

Catalogo=[]
#StockD=[]

post_cat = soup.find_all("h3", class_="Catalogsstyle__Title-sc-blno5s-16 jcqEii")


for element in post_cat:
    #print(element)
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    #print (limpio)
    Catalogo.append(limpio.strip())
print(post_cat)


# In[6]:


#Aqui se pasa el diccionario obtenido a DataFrame y se guarda como csv y json"
Ejergrupal=pd.DataFrame({'Catalogo':Catalogo})
#out = Ejergrupal.to_dict()
Ejergrupal.to_csv('Zara.csv')
Ejergrupal.to_json('Zara.json')


# In[7]:


#Mediante la conexion se establece el nombre de la BD y la colección
db = CLIENT["WScraping"]
Collection = db["zara"]

#Obtiene el documento json generado anteriormente y lo carga en una variable
with open('zara.json') as file:
    file_data = json.load(file)

#Comprueba si hay uno o más llaves en el json. Si hay más de uno aplica .insert_many(),
#caso contrario ejecuta .insert_one() 
if isinstance(file_data, list): 
    Collection.insert_many(file_data) 
else:
    Collection.insert_one(file_data)


# In[ ]:




