#!/usr/bin/env python3

from abc import ABCMeta, abstractmethod

class TaskTracker(metaclass=ABCMeta):
    def GetTaskTracker(config):
        if config['manager'] == 'gspread':
            from .gspread.task_tracker import GspreadTaskTracker 
            return GspreadTaskTracker(config['gspread'])
        else:
            return None

    @abstractmethod
    def auth(self):
        pass

    @abstractmethod
    def get_user_info(self):
        pass

    @abstractmethod
    def get_problem_tasks(self):
        pass

