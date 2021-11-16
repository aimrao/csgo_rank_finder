# csgo_rank_finder

**Info : Flask App is Live [here](http://pr0noobs.ddns.net/). If anyone is interested in improving the frontend, please create an issue and we can discuss.** 

## 1. Local Python App
        1. ```pip install -r requirements.txt``` to install the dependencies.
        2. Run main.py
        3. Copy-paste the 'status' command output (starting with #userid and till #end) from csgo console to the input and wait for the results.
        
## 2. Dockerized Flask App
        1. Install docker and docker-compose.
        2. Run ```docker-compose up -d``` and the flask app will be deployed on http://0.0.0.0:80 on your local machine or at http://server-ip:80 if run on a server like aws, gcp, etc.
        
**Note : The results may take some time to show based on the number of players in the input/server.**

# Sample Inputs

## 1

```
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

```

## 2

```
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

```

# Sample Output

```
+--------------------+------+------+------+------------+------+
|        Name        | Rank | Best | Wins |    HS %    | K/D  |
+--------------------+------+------+------+------------+------+
|      wassup        | SEM  | SEM  |  38  |     28     | 0.97 |
|     RED WOLF       |  S4  |  SE  | 155  |     24     | 0.76 |
|      𝐏𝐨𝐛𝐥𝐞𝐫𝐞       | MG1  | MG2  | 738  |     40     | 1.08 |
|     saneJoker      | GN2  | MG2  | 322  |     35     | 1.02 |
|       MiTR         | GN1  | GN1  | 160  |     31     | 0.51 |
|       🅣🅨🅢🅞🅝     | GN3  | MG1  | 356  |     43     | 1.14 |
|      Chris P       | GN3  | GN3  | 612  |     35     | 1.06 |
| RaLPh GaMiNg #YT   | GN3  | GN3  | 658  |     35     | 1.06 |
| B.TECH CHAAT WALA  | GN1  | GNM  | 402  |     37     | 1.04 |
|       -GTR         | MG1  | LEM  | 2989 |     42     | 1.02 |
|    hos._.sein      | SEM  | SEM  | 213  |     34     | 0.64 |
|    ∇SPELECTO∇      |  S4  |  S4  |  83  |     33     | 0.6  |
|      H!t£€®        | MG1  | MG2  | 1259 |     43     | 0.91 |
|       🎮รaм        | GN2  | GN3  | 372  |     30     | 0.81 |
|   GHøsTツÁnshu     | SEM  | GN1  | 263  |     38     | 0.82 |
+--------------------+------+------+------+------------+------+

```
