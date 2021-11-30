from dynamodb_helper import get_player, add_player
from bs4 import BeautifulSoup
import cloudscraper, json, re


#<-------------------------Global Variables [start]------------------------->#

#Fill this list with steam ID of your friends to exclude them from the search
friends = [76561198404529974,76561198816159059, 76561198430918852, 76561198435814829, 76561198807553119, 76561198405059981, 76561198059938292, 76561198401931678]


#All CSGO Ranks
ranks = {       
                0:"Unranked",
                1:"S1",     2:"S2",     3:"S3",     4:"S4",     5:"SE",     6:"SEM",    # Silver
                7:"GN1",    8:"GN2",    9:"GN3",    10:"GNM",                           # Gold Nova
                11:"MG1",   12:"MG2",   13:"MGE",   14:"DMG",                           # Master Guardian       
                15:"LE",    16:"LEM",                                                   # Legendary Eagle            
                17:"SMFC",                                                              # Supreme
                18:"GE"                                                                 # Global 
        }
#<-------------------------Global Variables [end]--------------------------->#



#<----------------------------Modules [start]------------------------------->#

#1. Convert steamid to steam64id, e.g. STEAM_1:1:607974202 to 76561198402829974
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

#2. Format 'status' command output and extract the steamids
def take_input(console_output):
    n = len(console_output)
    steam_id = []
    for i in range(n):
        try:
            steam_id.append(console_output[i].split()[-6])
        except:
            continue
    steam64 = set()
    for i in steam_id:
        steam64.add(steamid_to_64bit(i))
    return steam64

#3. Scrape the stats website for a particular steam64id
def scraper(id):
    url = 'https://csgostats.gg/player/' + str(id)
    flag = False
    while not flag:
        try:
            sc = cloudscraper.create_scraper()
            html_text = sc.get(url).text
            flag = True
        except:
            continue
        
    p = re.compile('var stats = .*')
    soup = BeautifulSoup(html_text, 'lxml')
    name = soup.find('div', id='player-name')
    scripts = soup.find_all('script')
    data = ''
    for script in scripts:
        try:
            m = p.match(script.string.strip())
            if m:
                data = m.group()
                break
        except:
            continue

    data_json = json.loads(data[12:-1])
    data_json['player_name'] = name.text
    data_json['profile_url'] = url
    return data_json

#4. Find ranks and other stats of the user and return the result in a pretty table
def find_rank_new(steam64id):
    
    global friends, ranks

    rows = []
    
    for id in steam64id:
        if id not in friends:
            try:
                response        = get_player(id)['Item']
                player_name     = response['steam_name']
                curr_rank       = response['current_rank']
                best_rank       = response['best_rank']
                total_wins      = response['wins']
                headshot_rate   = response['hsrate']
                kills_per_death = response['kpd']
                url             = response['profile_url']
            except KeyError:
                data_json       = scraper(id)
                player_name     = data_json['player_name']
                curr_rank       = ranks[data_json['rank']]
                best_rank       = ranks[data_json['best']['rank']]
                total_wins      = data_json['comp_wins']
                headshot_rate   = str(data_json['overall']['hs'])
                kills_per_death = str(data_json['overall']['kpd'])
                url             = data_json['profile_url'] 
                
                add_player(steam_id=id,name=player_name,curr_rank=curr_rank,best_rank=best_rank,wins=total_wins,hsrate=headshot_rate,kpd=kills_per_death,profile_url=url)

            rows.append([player_name, curr_rank, best_rank, total_wins, headshot_rate, kills_per_death, url])

    return rows

#<----------------------------Modules [end]--------------------------------->#

