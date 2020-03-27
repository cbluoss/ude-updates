#!/usr/bin/env python3

import requests
from functools import reduce
from bs4 import BeautifulSoup
import html2markdown

URL = 'https://www.uni-due.de/med/corona'
basepath = 'content'

page = requests.get(URL)
soup = BeautifulSoup(page.text, 'html.parser')
jumbos = soup.find_all(class_='jumbotron')


with open(basepath+'.html','w+') as file:
    content = reduce(lambda x,y: x+y,[x.contents for x in jumbos])
    content = [str(x) for x in content]
    file.writelines(content)

with open(basepath+'.md','w+') as file:
    content = [html2markdown.convert(x)+'\n' for x in content]
    file.writelines(content)