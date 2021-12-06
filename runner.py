#!/usr/bin/env python3

import argparse
import json

def get_runtime_config():
    parser = argparse.ArgumentParser(description='PS progress checker')
    parser.add_argument('configfile', metavar='CONFIG', type=str,\
            nargs=1, help='configuration file for progress checking')
    parser.add_argument('--gspread', dest='gspreadkey',\
            metavar='GSPREAD', type=str, nargs=1,\
            help="Google service account credentials file. "
            "overrides even the path is described in CONFIG. "
            "(valid when manager is gspread)")
    parser.add_argument('--sheet_id', dest='sheet_id',\
            metavar='SHEET_ID', type=str, nargs=1,\
            help="Google spreadsheet ID to manage. "
            "overrides even the sheet id has been described in CONFIG. "
            "(valid when manager is gspread)")

    args = parser.parse_args()
    with open(args.configfile[0]) as conf_json:
        config = json.load(conf_json)

    # Override config file with explicit arguments
    if config['manager'] == 'gspread':
        gspread = config['gspread']
        if args.gspreadkey is not None:
            gspread['gspreadkey'] = args.gspreadkey[0]
        if args.sheet_id is not None:
            gspread['sheet_id'] = args.sheet_id[0]

    return config


if __name__ == '__main__':
    conf = get_runtime_config()
    print(conf)
