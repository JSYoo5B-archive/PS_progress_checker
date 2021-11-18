#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

def get_prob_status(username: str, prob_id = -1):
    url = "https://www.acmicpc.net/status"
    url += "?user_id={}&language_id=-1&result_id=-1&problem_id={}"
    req_url = url.format(username, prob_id)
    
    # Request html data
    req = requests.get(req_url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    stat_tbl = soup.select('#status-table > tbody:nth-child(2) > tr')

    for stat in stat_tbl:
        cols = stat.find_all("td")
        for col in cols:
            print(col)
        print()

