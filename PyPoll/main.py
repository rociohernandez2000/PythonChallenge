import os
import csv
csvpath = os.path.join('election_data.csv')
file_output=os.path.join('output_file.txt')
total_voters=0
candidates = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0

#with open(csvpath, 'r') as file_handler:
#    lines=file_handler.read()
 #   print (lines)
  #  print(type(lines))
with open(csvpath,newline='') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')

    csv_header=next(csvreader)
    #print(f"CSV Header: {csv_header}")

    for row in csvreader:
        total_voters=total_voters + 1
        candidate = row[2]
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate]=0
        total_votes_candidate=candidate_votes[candidate]
        candidate_votes[candidate]=candidate_votes[candidate]+1
    print("Elections results")
    print("**********************************************")
    print ("Total voters : " + str(total_voters))
    print("Total votes and percentage by candidate")
    #print (candidates)
    #print (candidate_votes)

    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_voters) * 100

        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
        #print (total_voters)
        #print (candidates)
        #outputprint = f"{candidate_votes}: {vote_percentage}"
        outputprint = f"{candidate}: {total_votes_candidate}: {vote_percentage}"
    #print (candidate_votes)
    #print (vote_percentage)
        print (outputprint)
    print (winning_candidate)