import math
import pandas as pd

from_csv = pd.read_csv("11yearsMenUSOpenMatches.csv")
from_csv['firstServe1'] = from_csv['firstServe1'].astype(str)
from_csv['firstServe2'] = from_csv['firstServe2'].astype(str)

players_stats = {}

headers = ["year", "player", "winner", "error", "ace", "firstServe", "double", "firstPointWon", "secPointWon",
           "fastServe", "avgFirstServe", "break", "return", "total", "net"]

# Remove null entries
from_csv = from_csv[from_csv.fastServe1.notnull()]
from_csv = from_csv[from_csv.winner1.notnull()]
from_csv = from_csv[from_csv.break2 != '-']
from_csv = from_csv[from_csv.net1 != '-']

# from_csv['break2'] = from_csv['break2'].replace('-', '0%')
# Replace Percentage with its numeric and store as numeric data
from_csv['firstServe1'] = from_csv['firstServe1'].str[0:-1].astype(float)
from_csv['firstServe2'] = from_csv['firstServe2'].str[0:-1].astype(float)
from_csv['firstPointWon1'] = from_csv['firstPointWon1'].str[0:-1].astype(float)
from_csv['firstPointWon2'] = from_csv['firstPointWon2'].str[0:-1].astype(float)
from_csv['secPointWon1'] = from_csv['secPointWon1'].str[0:-1].astype(float)
from_csv['secPointWon2'] = from_csv['secPointWon2'].str[0:-1].astype(float)
from_csv['break1'] = from_csv['break1'].str[0:-1].astype(float)
from_csv['break2'] = from_csv['break2'].str[0:-1].astype(float)
from_csv['return2'] = from_csv['return2'].str[0:-1].astype(float)
from_csv['return1'] = from_csv['return1'].str[0:-1].astype(float)
from_csv['net1'] = from_csv['net1'].str[0:-1].astype(float)
from_csv['net2'] = from_csv['net2'].str[0:-1].astype(float)

from_csv.info()
#
# losers = set(from_csv['player2'])
# winnners = set(from_csv['player1'])
# print len(winnners)
# winners = winnners.intersection(losers)
# print len(winnners)
# print len(winners)
#
# for i in winners:
#     print from_csv[from_csv.player1 == i]

total_matches = len(from_csv)

win_ace = sum(from_csv.ace1)
lose_ace = sum(from_csv.ace2)

win_error = sum(from_csv.error1)
lose_error = sum(from_csv.error2)

win_winner = sum(from_csv.winner1)
lose_winner = sum(from_csv.winner2)

win_firstServe = sum(from_csv.firstServe1)
lose_firstServe = sum(from_csv.firstServe2)

win_double = sum(from_csv.double1)
lose_double = sum(from_csv.double2)

win_firstPointWon = sum(from_csv.firstPointWon1)
lose_firstPointWon = sum(from_csv.firstPointWon2)

win_secPointWon = sum(from_csv.secPointWon1)
lose_secPointWon = sum(from_csv.secPointWon2)

win_fastServe = sum(from_csv.fastServe1)
lose_fastServe = sum(from_csv.fastServe2)

win_avgFirstServe = sum(from_csv.avgFirstServe1)
lose_avgFirstServe = sum(from_csv.avgFirstServe2)

win_break = sum(from_csv.break1)
lose_break = sum(from_csv.break2)

win_return = sum(from_csv.return1)
lose_return = sum(from_csv.return2)

win_total = sum(from_csv.total1)
lose_total = sum(from_csv.total2)

win_net = sum(from_csv.net1)
lose_net = sum(from_csv.net2)

"""firstServe", "double", "firstPointWon", "secPointWon",
           "fastServe", "avgFirstServe", "break", "return", "total", "net"""

overall_stats = [
    {
        "name": "ace",
        "win_avg": win_ace / total_matches,
        "win_percent": float(win_ace) / float(win_ace + lose_ace),
        "lose_avg": lose_ace / total_matches,
        "win_lit": win_ace,
        "lose_lit": lose_ace
    },
    {
        "name": "error",
        "win_avg": win_error / total_matches,
        "lose_avg": lose_error / total_matches,
        "win_percent": win_error / (win_error + lose_error),
        "win_lit": win_error,
        "lose_lit": lose_error
    },
    {
        "name": "winner",
        "win_avg": win_winner / total_matches,
        "lose_avg": lose_winner / total_matches,
        "win_percent": win_winner / (win_winner + lose_winner),
        "win_lit": win_winner,
        "lose_lit": lose_winner
    },
    {
        "name": "firstServe",
        "win_avg": win_firstServe / total_matches,
        "lose_avg": lose_firstServe / total_matches,
        "win_percent": win_firstServe / (win_firstServe + lose_firstServe),
        "win_lit": win_firstServe,
        "lose_lit": lose_firstServe
    },
    {
        "name": "double",
        "win_avg": float(win_double) / float(total_matches),
        "lose_avg": float(lose_double) / float(total_matches),
        "win_percent": float(win_double) / float(win_double + lose_double),
        "win_lit": win_double,
        "lose_lit": lose_double
    },

    {
        "name": "return",
        "win_avg": win_return / total_matches,
        "lose_avg": lose_return / total_matches,
        "win_percent": win_return / (win_return + lose_return),
        "win_lit": win_return,
        "lose_lit": lose_return
    },

    {
        "name": "break",
        "win_avg": win_break / total_matches,
        "lose_avg": lose_break / total_matches,
        "win_percent": win_break / (win_break + lose_break),
        "win_lit": win_break,
        "lose_lit": lose_return
    },

    {
        "name": "avgFirstServe",
        "win_avg": win_avgFirstServe / total_matches,
        "lose_avg": lose_avgFirstServe / total_matches,
        "win_percent": win_avgFirstServe / (win_avgFirstServe + lose_avgFirstServe),
        "win_lit": win_avgFirstServe,
        "lose_lit": lose_avgFirstServe
    },

    {
        "name": "fastServe",
        "win_avg": win_fastServe / total_matches,
        "lose_avg": lose_fastServe / total_matches,
        "win_percent": win_fastServe / (win_fastServe + lose_fastServe),
        "win_lit": win_fastServe,
        "lose_lit": lose_fastServe
    },

    {
        "name": "net",
        "win_avg": win_net / total_matches,
        "lose_avg": lose_net / total_matches,
        "win_percent": win_net / (win_net + lose_net),
        "win_lit": win_net,
        "lose_lit": lose_net
    },

    {
        "name": "total",
        "win_avg": float(win_total) / float(total_matches),
        "lose_avg": float(lose_total) / float(total_matches),
        "win_percent": float(win_total) / float(win_total + lose_total),
        "win_lit": win_total,
        "lose_lit": lose_total
    },

]

header = {}
data_overall = []
for index, value in enumerate(overall_stats[0].keys()):
    header[value] = index

for i in range(0, len(overall_stats)):
    temp = []
    for key in header:
        temp.insert(header.get(key), overall_stats[i].get(key))
    data_overall.append(temp)

with open("aster_data_overall.csv", 'w') as file_w:
    file_w.write(",".join(str(l) for l in header))
    file_w.write("\n")
    for i in data_overall:
        file_w.write(",".join(str(l) for l in i))
        file_w.write("\n")

features = ["winner", "error", "ace", "firstServe", "double", "firstPointWon", "secPointWon",
            "fastServe", "avgFirstServe", "break", "return", "total", "net"]
avg_stats = []
players_set = set(from_csv['player1']).intersection(from_csv['player2'])
with open("player.csv",'w') as player_file:
    player_file.write(', '.join(i for i in players_set))

for i in players_set:
    player_stat = {}
    player_stat["name"] = str(i)
    won_set = from_csv[from_csv.player1 == i]
    lost_set = from_csv[from_csv.player2 == i]
    match_won = len(won_set)
    match_lost = len(lost_set)
    total = match_won + match_lost
    player_stat["won"] = match_won
    if total==0:
        print "0-matches won by {0}".format(i)
    else:
        player_stat["won_percent"] = math.ceil((float(match_won) / total) * 100) / 100
        player_stat["lost"] = match_lost
        for j, value in enumerate(features):
            total_won = len(won_set)
            total_loss = len(lost_set)
            feature = features[j]
            won = math.ceil(float(sum(won_set[feature + "1"]))) * 100 / match_won
            loss = math.ceil(float(sum(lost_set[feature + "2"]))) / match_lost
            player_stat[feature + "_w"] = won
            player_stat[feature + "_l"] = loss
        avg_stats.append(player_stat)

total_features = []
for feature in features:
    total_features.append(feature+"_w")
    total_features.append(feature+"_l")

header_pl = ["name", "won", "lost", "won_percent"]
total_features = total_features + header_pl
player_overall = []
for stat in avg_stats:
    temp = []
    for feature in total_features:
        temp.append(stat[feature])
    player_overall.append(temp)

# sort according to win_percent
df_players = pd.DataFrame(avg_stats)

df_players = df_players.sort_values(by='won_percent', ascending=0)
df_players.iloc[:50].to_csv('aster_data_players.csv', index=False)
df_players['name'][:50].to_csv('players.csv', index=False)

with open("normal_aster_data_players.csv", 'w') as file_w:
    file_w.write(",".join(str(l) for l in total_features))
    file_w.write("\n")
    for i in player_overall:
        file_w.write(",".join(str(l) for l in i))
        file_w.write("\n")
