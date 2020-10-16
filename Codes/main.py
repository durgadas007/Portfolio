# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 21:07:34 2020

@author: Durga Das
"""

import datetime as dt
import pandas as pd
import requests as re
from requests.exceptions import HTTPError
import json
import os


def getData(scheme_code):
    '''Returns json data'''

    url = 'https://api.mfapi.in/mf/'
    try:
        response = re.get(url + str(scheme_code))
        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print('HTTP error occurred:')  # Python 3.6
    except Exception as err:
        print('Other error occurred:')  # Python 3.6
    else:
        print('Success!')

    json_data = json.loads(response.text)

    #Save the json data in the Jsons directory
    #saveSchemeData(scheme_code,json_data)

    return json_data

def getDataFrame(json_data):
    '''Returns Dataframe from json'''

    start = pd.datetime(2010, 1, 1)
    end = pd.Timestamp("today").strftime("%m/%d/%Y")
    dates = pd.date_range(start,end)
    df1 = pd.DataFrame(index=dates)
    df = pd.DataFrame(json["data"],index=dates)
    #print(df1.head())

    return df1.head()


def saveSchemeData(scheme_code,json_data):

    mode = 'w' if os.path.exists("../Jsons/"+str(scheme_code)+".json") else 'x'
    try:
        with open("../Jsons/"+str(scheme_code)+".json", mode, encoding='utf-8') as f:
            json.dump(json_data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print("cant save file"+str(e))


if __name__ == "__main__":

    json_data = getData(118834)
    #dff = getDataFrame("json_data")
    #print(dff)
