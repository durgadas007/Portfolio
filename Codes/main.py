# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 21:07:34 2020

@author: Durga Das
"""

import datetime as dt
import pandas as pd
import requests as re
from requests.exceptions import HTTPError
import pprint as pp



def getData(scheme_code):
    '''Returns json data'''


    url = 'https://api.mfapi.in/mf/'
    try:
        response = re.get(url + str(scheme_code))
        response.encoding = 'utf-8'
        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print('HTTP error occurred:')  # Python 3.6
    except Exception as err:
        print('Other error occurred:')  # Python 3.6
    else:
        print('Success!')

    return response.json()

def getDataFrame(json):
    '''Returns Dataframe from json'''
    start = pd.datetime(2010, 1, 1)
    end = pd.Timestamp("today").strftime("%m/%d/%Y")
    dates = pd.date_range(start,end)
    df1 = pd.DataFrame(index=dates)
    df = pd.DataFrame(json["data"],index=dates)

    print(df1.head())a

    return df1.head()

if __name__ == "__main__":

    #json_data = getData(120166)
    #dff = getDataFrame("json_data")
    #print(dff)

    pp.pprint(x)
