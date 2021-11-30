#!/usr/bin/env python3

from datetime import datetime

class ProblemTask:
    def __init__(self, plat:str, id:int, due:datetime):
        self.plat = plat
        self.id = id
        self.due = due

