#!/usr/bin/env python3

from constants import SUPPORT_SITES

class UserInfo:
    def __init__(self, name:str):
        self.name = name
        self.ids = dict()

    def set_site_ids(self, site:str, id:str):
        # Skip when id string isn't valid
        if len(id) == 0 or len(id.split()) != 1:
            return
        if site in SUPPORT_SITES:
            self.ids[site] = id
    
    def get_site_ids(self, site:str):
        if site in SUPPORT_SITES:
            return self.ids[site]
        else:
            return ""

