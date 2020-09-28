#!/usr/bin/python

from bs4 import BeautifulSoup as Soup


def modify(id_list, filename=None):
    if filename is None:
        filename = 'index.html'
    html = open(filename, "r")
    button_html = Soup(html, "html.parser")
    html.close()
    '''Creates H3 tag which creates expandable bar in MFilm panel'''
    button_html.find("h3").insert_before(build_expander())
    '''Creates DIV tags under H3 with buttons'''
    button_html = build_bar(id_list, button_html)
    return button_html


def build_bar(id_list, button_html):
    soup = Soup("<div></div>", 'html.parser')
    div_out = soup.div

    div_in = soup.new_tag("div", attrs={"class": "ac_block2", "id": "custom_bar"})
    for id in id_list:
        button_code = button_html.find(id=id)
        div_in.append(button_code)
    div_out.append(div_in)

    button_html.find("h3").insert_after(div_out)
    return Soup.prettify(button_html)


def build_expander():
    soup = Soup("<h3></h3>", 'html.parser')
    h3 = soup.h3
    div = soup.new_tag("div", attrs={"class": "ac_marker", "id": "gre"})
    h3.append(div)
    h3.append("My Bar")
    return h3
