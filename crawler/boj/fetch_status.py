#!/usr/bin/env python3

from submit_log import SubmitLog
from constants import get_result_code
import requests
from bs4 import BeautifulSoup, element
from datetime import datetime
from typing import List

def fetch_submit_logs(username:str,
                prob_id = -1, result_id = -1, submit_before = -1)\
                -> List[SubmitLog]:
    # Generate URL to request
    req_url = "https://www.acmicpc.net/status?"
    if len(username) > 0:
        req_url += "user_id={}&".format(username)
    req_url += "language_id=-1&problem_id={}&result_id={}".format(\
            prob_id, result_id)
    if submit_before != -1:
        req_url += "&top={}".format(submit_before)
    
    # Request html data
    req = requests.get(req_url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    stat_tbl = soup.select('#status-table > tbody:nth-child(2) > tr')

    # Parse status table
    submit_logs = []
    for row in stat_tbl:
        # Parse columns into SubmitLog struct
        cols = row.find_all("td")
        s_log = parse_submit_log(cols)
        submit_logs.append(s_log)

    return submit_logs


def parse_submit_log(html_tags:List[element.Tag]) -> SubmitLog:
    t_i = 0
    attr = []
    
    # Parse submit id
    submit_id = int(html_tags[t_i].string)
    attr.append(submit_id)
    t_i += 1
    
    # Parse username
    username = str(html_tags[t_i].a.string)
    attr.append(username)
    t_i += 1
    
    # Parse problem ID and problem name
    prob_id = int(html_tags[t_i].a.string)
    attr.append(prob_id)
    prob_name = str(html_tags[t_i].a['title'])
    attr.append(prob_name)
    t_i += 1
    
    # Parse result code
    result_abbrev = str(html_tags[t_i].span['data-color'])
    code = get_result_code(result_abbrev)
    attr.append(code)
    t_i += 1
    
    # Parse memory usage
    mem_tag = html_tags[t_i].find('span')
    mem_str = 'None' if mem_tag is None else str(mem_tag.previousSibling)
    mem_usage = 0 if mem_str == 'None' else int(mem_str)
    attr.append(mem_usage)
    t_i += 1
    
    # Parse time elapsed for solution
    elap_tag = html_tags[t_i].find('span')
    elap_str = 'None' if elap_tag is None else str(elap_tag.previousSibling)
    elap_ms = 0 if elap_str == 'None' else int(elap_str)
    attr.append(elap_ms)
    t_i += 1
    
    # Parse language used in submit
    lang = str(html_tags[t_i].string)
    attr.append(lang)
    t_i += 1
    
    # Parse source length
    src_len = 0
    if html_tags[t_i].find('span') is not None:
        src_len = int(html_tags[t_i].find('span').previousSibling)
    attr.append(src_len)
    t_i += 1
    
    # Parse submit time
    submit_str = str(html_tags[t_i].a['title'])
    submit_time = datetime.strptime(submit_str, "%Y-%m-%d %H:%M:%S")
    attr.append(submit_time)

    return SubmitLog(attr)

