# csgo_rank_finder
1. Run main.py
2. Copy-paste the 'status' command output (starting with #userid and till #end) from csgo console to the input and wait for the results. 

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
+----------------------------------+---------+---------+------+
|               Name               |   Rank  |   Best  | Wins |
+----------------------------------+---------+---------+------+
|             wassup               |   SEM   | Unknown |  38  |
|            RED WOLF              |    SE   | Unknown | 116  |
|             itElyas              |   GN3   |   MG2   | 500  |
|            saneJoker             |   GN3   |   MG2   | 306  |
| cover the face, fuck the base!!  |    SE   |   SEM   | 114  |
|              🅣🅨🅢🅞🅝            |   GN1   |   MG1   | 343  |
|             Chris P              |   GN2   |   GN3   | 545  |
|          Ralph Gaming            |   SEM   |   GN2   | 442  |
|        B.TECH CHAAT WALA         |   GN1   |   GN2   | 268  |
|             ✝caЯЯoT              | Unknown | Unknown | 2936 |
|         ☛ Cypher Boy ☚          |    S4   | Unknown |  76  |
|           ∇ CAPTAIN ∇            |    S3   | Unknown |  66  |
|             H!t£€®               |   GNM   |   MG2   | 1204 |
|              🎮รaм               |   GN1   |   GN2   | 259  |
|          GHøsTツÁnshu            |    SE   |   GN1   | 197  |
+----------------------------------+---------+---------+------+

```
