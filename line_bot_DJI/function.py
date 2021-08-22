import requests
from bs4 import  BeautifulSoup


def search():  
    headers = {
    'user-agent' : 'Mozilla/5.0'
    }
    r = requests.get('https://tw.stock.yahoo.com/us/q?s=^DJI', headers = headers, timeout = 10)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text

def searchSOX():
    headers = {
    'user-agent' : 'Mozilla/5.0'
    }
    s = requests.get('https://tw.stock.yahoo.com/us/q?s=^SOX', headers = headers, timeout = 10)
    s.raise_for_status()
    s.encoding = s.apparent_encoding
    return s.text

def searchIXIC():
    headers = {
    'user-agent' : 'Mozilla/5.0'
    }
    i = requests.get('https://tw.stock.yahoo.com/us/q?s=^IXIC', headers = headers, timeout = 10)
    i.raise_for_status()
    i.encoding = i.apparent_encoding
    return i.text

        

def gethtml(text):
    soap = BeautifulSoup(text, 'html.parser')
    table = soap.find_all('tr', align = 'center')
    for i in range(len(table)):
        if i == 1:
            td = table[i]('td')
            
    for x in range(len(td)):
        if x == 4:
            a = str(td[x].text).strip('<td>').lstrip()
    return a

def getdata(text):
    soap = BeautifulSoup(text, 'html.parser')
    table = soap.find('td', align = 'right')
    return table.text
