#!/usr/bin/env python3

from submit_log import SubmitLog
from fetch_status import fetch_submit_logs
from collections import defaultdict
from typing import List

class UserStatus:
    def __init__(self, username):
        self.username = username
        self.submits = defaultdict(list)

    def fetch_submits(self, \
                prob_id = -1, result_id = -1, submit_before = -1):
        # Fetch submit logs
        submits = fetch_submit_logs(self.username, \
                prob_id, result_id, submit_before)

        # Store each submit logs into dictionary
        for s_log in submits:
            # Append into problem logs dict
            self.submits[s_log.prob_id].append(s_log)

        # Return count of fetched submit from current request
        return len(submits)

