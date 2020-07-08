import os
import csv
path = os.path.join('Resources', 'election_data.csv')
with open(path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader, None)
    total_votes = []
    candidate_vote_count = []
    candidate_names = []
    g = 0
    Winner = 0
    Winner_n = 0

    for row in csv_reader:
        total_votes.append(row[2]) 
        if total_votes[g] not in candidate_names:
            candidate_names.append(total_votes[g])
            candidate_vote_count.append(0)
        
        for i in range(len(candidate_names)):
            if (total_votes[g]) == candidate_names[i]:
                candidate_vote_count[i] = candidate_vote_count[i] + 1                
        g = len(total_votes)

    for i in range(len(candidate_names)):
        if Winner < candidate_vote_count[i]:
            Winner = candidate_vote_count[i]
            Winner_n = i


print(f'\nElection Results')
print(f'\n-------------------------')
print(f'\nTotal Votes: {len(total_votes)}')
print(f'\n-------------------------')

percentage = 0
for i in range(len(candidate_names)):
    percentage = candidate_vote_count[i]/(len(total_votes))

    print(f'\n{candidate_names[i]}: ' +  "{:.2%}".format(percentage) + f' ({candidate_vote_count[i]})')


print(f'\n-------------------------')
print(f'\nWinner: {candidate_names[Winner_n]}')
print(f'\n-------------------------')

txt_file =  os.path.join("Analysis","Results.txt")
f= open(txt_file, "w+")

f.write(f'\nElection Results')
f.write(f'\n-------------------------')
f.write(f'\nTotal Votes: {len(total_votes)}')
f.write(f'\n-------------------------')

percentage = 0
for i in range(len(candidate_names)):
    percentage = candidate_vote_count[i]/(len(total_votes))

    f.write(f'\n{candidate_names[i]}: ' +  "{:.2%}".format(percentage) + f' ({candidate_vote_count[i]})')


f.write(f'\n-------------------------')
f.write(f'\nWinner: {candidate_names[Winner_n]}')
f.write(f'\n-------------------------')