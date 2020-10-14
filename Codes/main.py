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

    x={'current_user_url': 'https://api.github.com/user', 'current_user_authorizations_html_url': 'https://github.com/settings/connections/applications{/client_id}', 'authorizations_url': 'https://api.github.com/authorizations', 'code_search_url': 'https://api.github.com/search/code?q={query}{&page,per_page,sort,order}', 'commit_search_url': 'https://api.github.com/search/commits?q={query}{&page,per_page,sort,order}', 'emails_url': 'https://api.github.com/user/emails', 'emojis_url': 'https://api.github.com/emojis', 'events_url': 'https://api.github.com/events', 'feeds_url': 'https://api.github.com/feeds', 'followers_url': 'https://api.github.com/user/followers', 'following_url': 'https://api.github.com/user/following{/target}', 'gists_url': 'https://api.github.com/gists{/gist_id}', 'hub_url': 'https://api.github.com/hub', 'issue_search_url': 'https://api.github.com/search/issues?q={query}{&page,per_page,sort,order}', 'issues_url': 'https://api.github.com/issues', 'keys_url': 'https://api.github.com/user/keys', 'notifications_url': 'https://api.github.com/notifications', 'organization_repositories_url': 'https://api.github.com/orgs/{org}/repos{?type,page,per_page,sort}', 'organization_url': 'https://api.github.com/orgs/{org}', 'public_gists_url': 'https://api.github.com/gists/public', 'rate_limit_url': 'https://api.github.com/rate_limit', 'repository_url': 'https://api.github.com/repos/{owner}/{repo}', 'repository_search_url': 'https://api.github.com/search/repositories?q={query}{&page,per_page,sort,order}', 'current_user_repositories_url': 'https://api.github.com/user/repos{?type,page,per_page,sort}', 'starred_url': 'https://api.github.com/user/starred{/owner}{/repo}', 'starred_gists_url': 'https://api.github.com/gists/starred', 'team_url': 'https://api.github.com/teams', 'user_url': 'https://api.github.com/users/{user}', 'user_organizations_url': 'https://api.github.com/user/orgs', 'user_repositories_url': 'https://api.github.com/users/{user}/repos{?type,page,per_page,sort}', 'user_search_url': 'https://api.github.com/search/users?q={query}{&page,per_page,sort,order}'}

    pp.pprint(x)
