#!/usr/bin/env python3

"""
Creator:  VPR
Created:  November 20, 2021
Modified: November 20, 2021

Brief:
    This is a web scraping utility that pulls data from worldatlas.com
    and parses the table listed to extract a dictionary of the following
    key/value pairs: 'State' : list_of_area_codes.
"""

import requests
# import argparse

from bs4 import BeautifulSoup

from modules.scraper import parse_table
from modules.formatter import display_as_python_tuple

source = "https://www.worldatlas.com/na/us/area-codes.html"

def handle_command_line():
    return None

if __name__ == "__main__":
    # Determine output language format
    fmt = handle_command_line()

    # Retrieving data from source
    page = requests.get(source) 
    soup = BeautifulSoup(page.content, "html.parser")
     
    # Select the main table
    table = soup.find("table")

    # Use this map as you see fit
    area_codes_map = parse_table(table)

    # Format based on user input
    if fmt is None:
        display_as_python_tuple(area_codes_map)
    elif fmt == "py":
        display_as_python_tuple(area_codes_map)
    elif fmt == "cpp":
        ...
    elif fmt == "c":
        ...
