import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import csv
from scipy import stats
import glob
import os
from statistics import mean, median,variance,stdev
from collections import OrderedDict
import requests
from bs4 import BeautifulSoup
import time
import dateutil.parser
import datetime
from datetime import datetime

df_amestation = pd.read_csv("M:/UserDir/y_hcr_motohashi/Desktop/data_3/amedas_stations.csv", sep=",")
df_address = pd.read_csv("M:/UserDir/y_hcr_motohashi/Desktop/data_3//Address_xy.csv", sep=",")
df_amestation = df_amestation.drop('Unnamed: 0', axis=1)
df_address = df_address.drop('Unnamed: 0', axis=1)

def cal_rho(lon_a,lat_a):
    list_rho = []
    list_id = []
    ra=6378.140  # equatorial radius (km)
    rb=6356.755  # polar radius (km)
    F=(ra-rb)/ra # flattening of the earth
    for i in range(len(df_amestation)):
        lat_b = df_amestation["latitude"].iloc[i]
        lon_b = df_amestation["longitude"].iloc[i]
        id_ame = df_amestation["amedas_id"].iloc[i]
        rad_lat_a=np.radians(lat_a)
        rad_lon_a=np.radians(lon_a)
        rad_lat_b=np.radians(lat_b)
        rad_lon_b=np.radians(lon_b)
        pa=np.arctan(rb/ra*np.tan(rad_lat_a))
        pb=np.arctan(rb/ra*np.tan(rad_lat_b))
        xx=np.arccos(np.sin(pa)*np.sin(pb)+np.cos(pa)*np.cos(pb)*np.cos(rad_lon_a-rad_lon_b))
        c1=(np.sin(xx)-xx)*(np.sin(pa)+np.sin(pb))**2/np.cos(xx/2)**2
        c2=(np.sin(xx)+xx)*(np.sin(pa)-np.sin(pb))**2/np.sin(xx/2)**2
        dr=F/8*(c1-c2)
        rho=ra*(xx+dr)
        list_rho.append(rho)
        list_id.append(id_ame)
    min_ind = list_rho.index(min(list_rho)) 
    ame_id = list_id[min_ind]   
    return ame_id

cal_rho(34.7083,137.7183)

list_amedas = []
for i in range(len(df_address)):
    lat = df_address["Ido"].iloc[i]
    lon = df_address["Keido"].iloc[i]
    ame_id = cal_rho(lon,lat)
    list_amedas.append(ame_id)

df_amedas = pd.DataFrame({'amedas_ID' : list_amedas})
df_address_new = df_address.drop(['Address','Ido', 'Keido'], axis=1)
df_1 = pd.concat([df_address_new,df_amedas], axis=1)

df_1.to_csv("C:/Users/yunom/Desktop/Output_python/RF_amedas_address.csv")
