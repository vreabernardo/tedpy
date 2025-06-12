import requests
import json
import math
import time
from tqdm import tqdm
from datetime import datetime


class SearchTed:
    def __init__(self):
        self.search_url = "https://api.ted.europa.eu/v3/notices/search"
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Host": "api.ted.europa.eu"
        }
        
    def execute(self, query, fields, scope, only_latest_versions):         
        payload = {
            "query": query,
            "fields": fields,
            "scope": scope,
            "onlyLatestVersions": only_latest_versions,
            "paginationMode": "PAGE_NUMBER",
            "limit": 1,
            "page": 1
        }
        
        try:
            response = requests.post(self.search_url, json=payload, headers=self.headers)
            return response.json()
            
        except Exception as e:
            raise e

if __name__ == "__main__":
    ted = SearchTed()
    
    filename = ted.execute(
        query="OJ = () SORT BY publication-number DESC",
        fields=["notice-title"],
        scope="ACTIVE",
        only_latest_versions=True
    )
    print(filename)