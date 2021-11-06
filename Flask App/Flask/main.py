from bs4 import BeautifulSoup
import cloudscraper

#Fill this list with steam ID of your friends to exclude them from the search
friends = [76561198404529974,76561198816159059, 76561198430918852, 76561198435814829, 76561198807553119, 76561198405059981, 76561198059938292, 76561198401931678]


def steamid_to_64bit(steamid):
    steam64id = 76561197960265728 # kinda Seed                                 
    id_split = steamid.split(":")
    try:
        steam64id += int(id_split[2]) * 2 
    except:
        return 76561198404529974
    if id_split[1] == "1":
        steam64id += 1
    return steam64id

def take_input(console_output):
    n = len(console_output.split('\n'))
    steam_id = []
    for i in range(1,n):
        try:
            steam_id.append(console_output.split('\n')[i].split()[-6])
        except:
            continue
    steam64 = set()
    for i in steam_id:
        steam64.add(steamid_to_64bit(i))
    return steam64

def find_rank_new(steam64id):
    global friends
    rows = []

    for id in steam64id:
        if id not in friends:
            url = 'https://csgostats.gg/player/' + str(id)

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
            flag = False
            while not flag:
                try:
                    sc = cloudscraper.create_scraper()
                    html_text = sc.get(url).text
                    flag = True
                except:
                    continue

            soup = BeautifulSoup(html_text, 'lxml')
            rank = soup.find('div', style="float:right; width:92px; height:120px; padding-top:56px; margin-left:32px;")
            wins = soup.find('span', id='competitve-wins')
            name = soup.find('div', id='player-name')

            fetch_count = 0
            player = name.text
            try:
                total_wins = wins.span.text
            except:
                total_wins = "Unknown"
            tries = 3
            while(fetch_count!=2):
                try:
                    curr_rank = ranks[rank.img['src'].split('/')[-1].split('.')[0]]
                    fetch_count+=1
                except:
                    try:
                        curr_rank = ranks[rank.img['data-cfsrc'].split('/')[-1].split('.')[0]]
                        fetch_count+=1
                    except:
                        if tries>0:
                            tries -= 1
                            continue
                        curr_rank = "Unranked"
                        fetch_count+=1
                        
                tries = 3
                try:
                    best_rank = ranks[rank.div.img['src'].split('/')[-1].split('.')[0]]
                    fetch_count+=1
                except:
                    try:
                        best_rank = ranks[rank.img['data-cfsrc'].split('/')[-1].split('.')[0]]
                        fetch_count+=1
                    except:
                        if tries>0:
                            tries -= 1
                            continue
                        curr_rank = "Unranked"
                        fetch_count+=1
            
            rows.append([player, curr_rank, best_rank, total_wins, url])

    return rows
