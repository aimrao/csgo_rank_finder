import requests
from bs4 import BeautifulSoup
import cloudscraper

sc = cloudscraper.create_scraper()

def find_rank(steam64id):
    url = 'https://csgostats.gg/player/' + str(steam64id)

    ranks = {
        "1":"S1",
        "2":"S2",
        "3":"S3",
        "4":"S4",
        "5":"SE",
        "6":"SEM",
        "7":"GN1",
        "8":"GN2",
        "9":"GN3",
        "10":"GNM",
        "11":"MG1",
        "12":"MG2",
        "13":"MGE",
        "14":"DMG",
        "15":"LE",
        "16":"LEM",
        "17":"SMFC",
        "17":"GE"
    }

    soup = BeautifulSoup(sc.get(url).text, 'lxml')
    rank = soup.find('div', style="float:right; width:92px; height:120px; padding-top:56px; margin-left:32px;")
    wins = soup.find('span', id='competitve-wins')
    name = soup.find('div', id='player-name')
    # print(wins.span.text)
    # print(ranks[rank.img['src'].split('/')[-1].split('.')[0]])
    # print(ranks[rank.div.img['src'].split('/')[-1].split('.')[0]])    

    print("{} [Rank : {}] [Best : {}] [Wins : {}]".format(name.text,ranks[rank.img['src'].split('/')[-1].split('.')[0]],ranks[rank.div.img['src'].split('/')[-1].split('.')[0]],wins.span.text))
   


find_rank(76561198404529974)




