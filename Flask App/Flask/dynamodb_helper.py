from decouple import config
from boto3 import resource
from datetime import datetime as dt, timedelta
from time import time

AWS_ACCESS_KEY_ID     = config("AWSAccessKeyId")
AWS_SECRET_ACCESS_KEY = config("AWSSecretKey")
REGION_NAME           = config("REGION_NAME")

resource = resource(
    'dynamodb',
    aws_access_key_id     = AWS_ACCESS_KEY_ID,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
    region_name           = REGION_NAME
)

csgo_players = resource.Table('csgo_players')

def add_player(steam_id, name, curr_rank, best_rank, wins, profile_url, hsrate, kpd ):

    response = csgo_players.put_item(
        Item = {
            'steam_id'      : steam_id,
            'steam_name'    : name,
            'current_rank'  : curr_rank,
            'best_rank'     : best_rank,
            'wins'          : wins,
            'hsrate'        : hsrate,
            'kpd'           : kpd,
            'profile_url'   : profile_url,
            'ttl'           : int((dt.fromtimestamp(time()) + timedelta(1)).timestamp())
        }
    )

    return response

def get_player(steam_id):       # Output Example - {'profile_url': 'pr0noobs.ddns.net', 'best_rank': 'mge', 'ttl': Decimal('1636883702'), 'steam_id': Decimal('1'), 'current_rank': 'mge', 'wins': '1003', 'steam_name': 'test_ttl'}

    response = csgo_players.get_item(
        Key = {
            'steam_id'     : steam_id
        },
        AttributesToGet=[
            'steam_name', 'current_rank', 'best_rank', 'wins', 'hsrate', 'kpd', 'profile_url'
        ]
    )

    return response


