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
import sys

from bs4 import BeautifulSoup
from argparse import ArgumentParser

from modules.scraper import parse_table
from modules.formatter import display_as_python_tuple, display_as_c_int_array

from typing import Union, NoReturn

source = "https://www.worldatlas.com/na/us/area-codes.html"

def handle_command_line() -> Union[NoReturn, None, str]:
    argc = len(sys.argv)

    if argc > 2:
        __usage_error(1) # only specify one switch pls

    parser = ArgumentParser()

    parser.add_argument( "-c",
                         action="store_true",
                         dest="c",
                         help="Convert bytes in file to raw string." )

    parser.add_argument( "--cpp",
                         action="store_true",
                         dest="cpp",
                         help="Convert bytes in file to cstr." )

    parser.add_argument( "--py",
                         action="store_true",
                         dest="py",
                         help="Convert bytes in file to cstr." )

    args = parser.parse_args()

    if args.c == True:
        return "c"
    elif args.cpp == True:
        return "cpp"
    elif args.py == True:
        return "py"

    return None

def __usage_error(exit_code: int) -> NoReturn:
    if exit_code == 1:
        sys.stderr.write(f"{sys.argv[0]} [ -c | -cpp | -py ]\n\n")

    sys.stderr.write(f"Exited with exit code: {exit_code}.")
    sys.exit(exit_code)

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
    elif fmt == "c":
        display_as_c_int_array(area_codes_map)
    elif fmt == "cpp":
        # TODO
        display_as_c_int_array(area_codes_map)
    elif fmt == "py":
        display_as_python_tuple(area_codes_map)
