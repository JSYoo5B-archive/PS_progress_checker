#!/usr/bin/env python3

from datetime import datetime
from typing import List

# BOJ submit tag order
[ \
        SUBMIT_ID, USERNAME, PROB_ID, PROB_NAME, \
        RES_CODE, MEM_USED, ELAPSE_MS, LANG, \
        SRC_LEN, SUBMIT_TIME \
] = [ i for i in range(10) ]

class SubmitLog():
    def __init__(self, args):
        self.s_id = args[SUBMIT_ID]
        self.username = args[USERNAME]
        self.prob_id = args[PROB_ID]
        self.prob_name = args[PROB_NAME]
        self.res_code = args[RES_CODE]
        self.mem_used = args[MEM_USED]
        self.elapsed_ms = args[ELAPSE_MS]
        self.lang = args[LANG]
        self.src_len = args[SRC_LEN]
        self.submit_time = args[SUBMIT_TIME]

