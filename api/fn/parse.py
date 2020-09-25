#!/usr/bin/python

import argparse
import re
from bs4 import BeautifulSoup as Soup
from json import dumps


def list_maker(filename='index.html'):

    html = open(filename, "r")
    soup = Soup(html, "html.parser")
    html.close()
    buttons_list = soup.find_all("button")
    butlist = list()
    for i in buttons_list:
        butlist.append(make_buttons_id(str(i)))
    butlist = list(dict.fromkeys(butlist))
    return dumps(butlist)


def make_buttons_id(button):
    m = re.search('id="(.+?)"', button)
    if m:
        found = m.group(1)
    return found


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input')
    args = parser.parse_args()
    if args.input != None:
        print(list_maker(args.input))
    elif args.input == None:
        print(list_maker('index.html'))
