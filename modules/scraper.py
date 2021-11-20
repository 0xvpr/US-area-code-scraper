#!/usr/bin/env python3

import requests
import sys

from bs4 import BeautifulSoup

from typing import Dict, List, Union
from bs4.element import Tag, NavigableString

def parse_table(table: Union[Tag, NavigableString, None]) -> Dict[str, List[int]]:
    area_codes_map = {}
    
    if isinstance(table, Tag):
        table_rows = table.find_all("tr")

        # Exclude 'th' tag
        for tr in table_rows[1:]:
            td = tr.find_all("td")

            # iterate through the rows
            state, area_codes_string = [i.text for i in td]

            # Populate the resulting dict
            area_codes_map[state] = tuple(map(int, area_codes_string.split(",")))
    else:
        sys.stderr.write(f"An error occurred while attempting to parse table.\n")
        sys.exit(1)

    return area_codes_map

if __name__ == "__main__":
    # Retrieving data from source
    page = requests.get(source) 
    soup = BeautifulSoup(page.content, "html.parser")
     
    # Select the main table
    table = soup.find("table")

    # Use this map as you see fit
    area_codes_map = parse_table(table)

    # DEBUGGING
    print(area_codes_map)
