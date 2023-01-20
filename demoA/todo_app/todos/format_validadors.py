"""
Avoiding parsing using regular expression
using brute force parsing. It is prone to 
errors but its beyond the scope at the moment.
"""

from datetime import date

def parse_date_string(date_string):
    if date_string[4]!="-" or date_string[7]!="-":
        print("Date not having '-' ")
        return 0
    ds = date_string.split("-")
    try:
        assert type(int(ds[0])) is int
        assert type(int(ds[1])) is int
        assert type(int(ds[2])) is int
    except AssertionError:
        print("Date not int")
        return 0
    if len(ds[0]) != 4:
        print("Bad year")
        return 0
    if date.today().year>int(ds[0])<(date.today().year-1):
        print("Bad year range!")
        return 0
    if len(ds[1]) != 2:
        print("Bad month!")
        return 0
    if 1>int(ds[1])>12:
        print("Bad month range!")
        return 0
    if len(ds[2]) != 2:
        print("Bad day!")
        return 0
    if 1>int(ds[2])>31:
        print("Bad date range")
        return 0        
    return 1

def parse_content(content):
    return 1
