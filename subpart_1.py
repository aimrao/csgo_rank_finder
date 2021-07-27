import requests
from bs4 import BeautifulSoup

def find_rank(steam64id):
    # url = 'https://csgostats.gg/player/76561198404529974'
    url = 'https://csgo-stats.com/player/' + str(steam64id)

    r = requests.get(url=url, )
    soup = BeautifulSoup(r.text, 'lxml')

    rank = soup.find('span', class_='rank-name')
    name = soup.find('div', class_='title-card')
    print("{} : {}".format(name.h1.text,rank.text))

find_rank(76561198404529974)

# Test Inputs

'''
# userid name uniqueid connected ping loss state rate adr
#  2 1 "Arion" STEAM_1:0:222132123 00:09 9 0 active 196608 loopback
# 3 "Marvin" BOT active 128
# 4 "Frank" BOT active 128
# 5 "Ulric" BOT active 128
# 6 "Harvey" BOT active 128
# 7 "Elliot" BOT active 128
# 8 "Yuri" BOT active 128
# 9 "Allen" BOT active 128
#10 "Toby" BOT active 128
#11 "Clarence" BOT active 128
#end
'''



'''
# userid name uniqueid connected ping loss state rate
# 379 2 "🎮รaм" STEAM_1:1:555251468 02:02 82 0 active 196608
# 364 3 "RED WOLF" STEAM_1:0:245855857 03:21 80 0 active 196608
# 380 4 "Ralph Gaming" STEAM_1:1:448953605 01:56 68 0 active 786432
# 356 5 "saneJoker" STEAM_1:0:219556434 10:40 57 0 active 786432
# 383 6 "AYAHUASCA" STEAM_1:1:564213075 00:14 50 56 spawning 196608
# 382 7 "Arion" STEAM_1:0:222132123 00:32 63 0 active 196608
# 358 8 "🅣🅨🅢🅞🅝" STEAM_1:1:418070643 09:53 59 0 active 786432
# 260 9 "GHøsTツÁnshu" STEAM_1:0:564337581 50:50 127 0 active 196608
# 362 10 "itElyas" STEAM_1:0:229309217 03:59 148 0 active 196608
# 252 12 "☛ Cypher Boy ☚" STEAM_1:1:588272711 56:07 135 0 active 786432
# 292 13 "wassup" STEAM_1:1:522849968 40:05 96 0 active 786432
# 333 14 "✝caЯЯoT" STEAM_1:0:38853895 24:03 41 0 active 128000
# 337 15 "∇ CAPTAIN ∇" STEAM_1:1:558002231 19:57 48 0 active 196608
# 375 16 "H!t£€®" STEAM_1:0:445231607 02:49 75 0 active 128000
# 355 17 "B.TECH CHAAT WALA" STEAM_1:1:449983525 12:17 76 0 active 196608
# 374 24 "Chris P" STEAM_1:1:81936499 02:50 94 0 active 196608
#end
'''