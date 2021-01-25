
import os
import csv

csvpath = os.path.join('election_data.csv')

with open(csvpath, newline='') as election:
    csvreader = csv.reader(election, delimiter=',')
    csv_header = next(election)
    total = 0 
    total_kahn = 0
    percent_kahn = 0
    total_correy = 0
    percent_correy = 0
    total_li = 0
    percent_li = 0 
    total_o = 0 
    percent_o = 0
    winner= []
    for row in csvreader: 
        total = total + 1

        if (row[2] == "Khan"):
            total_kahn = total_kahn + 1
            percent_kahn = (int(total_kahn)/int(total))*100

        if (row[2] == "Correy"):
            total_correy = total_correy + 1
            percent_correy = (int(total_correy)/int(total))*100

        if (row[2] == "Li"):
            total_li = total_li + 1
            percent_li = (int(total_li)/int(total))*100

        if (row[2] == "O'Tooley"):
            total_o = total_o + 1
            percent_o = (int(total_o)/int(total))*100

    if (percent_kahn > percent_correy and percent_kahn > percent_li and percent_kahn > percent_o):
            winner.append("Kahn")

    
    if (percent_correy > percent_kahn and percent_correy > percent_li and percent_correy > percent_o):
            winner.append("Correy")
    
    if (percent_li > percent_kahn and percent_li > percent_correy and percent_li > percent_o):
            winner.append("Li")

    if (percent_o > percent_kahn and percent_o > percent_correy and percent_o > percent_li):
            winner.append("O'Tooley")


    print("Election results")
    print("-----------------")
    print("Total Votes: " + str(total))
    print("-----------------")
    print("Khan: " + str(percent_kahn) + "% " + "(" + str(total_kahn) + ")")
    print("Correy: " + str(percent_correy) + "% " + "(" + str(total_correy) + ")")
    print("Li: " + str(percent_li) + "% " + "(" + str(total_li) + ")")
    print("O'Tooley: " + str(percent_o) + "% " + "(" + str(total_o) + ")")
    print("-----------------")
    print("Winner: " + str(winner[0]))