#!/usr/bin/env python3

from ..task_tracker import TaskTracker
import gspread

class GspreadTaskTracker(TaskTracker):
    def __init__(self, config):
        self.keyfile = config['gspreadkey']
        self.sheet_id = config['sheet_id']
        worksheets = config['worksheets']
        self.user_title = worksheets['users']
        self.task_titles = worksheets['tasks']

    def auth(self):
        gc = gspread.service_account(filename=self.keyfile)
        self.gsheet = gc.open_by_key(self.sheet_id)

    def get_user_info(self):
        user_sheet = self.gsheet.worksheet(self.user_title)
        users = user_sheet.get_all_records()
        # TODO: convert into user object lists
        print(users)

    def get_problem_tasks(self):
        pass
