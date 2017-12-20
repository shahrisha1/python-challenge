# You will be given two sets of poll data (election_data_1.csv and election_data_2.csv). 
# Each dataset is composed of three columns: Voter ID, County, and Candidate. 
# Your task is to create a Python script that analyzes the votes and calculates each of the following:

# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

#dependencies
#os module will allow us to create file paths across operating systems
import os
import csv

#create csv file path using os module to read file with
election_data_path = os.path.join('raw_data', 'election_data_1.csv')

#create text file path to write file to
election_data_path_out = os.path.join('election_data_1_output.txt')

#create variables to store the data
total_votes = 0 #integer
candidate = "" #string 
candidate_list = [] #list
candidate_votes = {} #dictionary 
winner_votes = 0  #integer
winner_candidate = "" #string 

#improved reading with csv module
with open(election_data_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip first row that is a header row so it doesn't pull into total counts/sums
    next(csvreader, None)

    #begin for loop, which will continue running until file reads last row
    for row in (csvreader):

        #calculate total number of months in dataset
        total_votes = total_votes + 1

        #identify list of candidates and append to the empty list
        candidate = row[2] 

        #start the if statement to start adding candidates to the list
        if candidate not in candidate_list:

            #using append method add the candidate value in the list
            candidate_list.append(candidate)

            #candidate votes starting at 0 for counter variable
            candidate_votes[candidate] = 0

        #once the candidates are added, continue the loop to add the value of counts
        candidate_votes[candidate] = candidate_votes[candidate] + 1

#write all the content of print statement to text file (output path)
with open(election_data_path_out, "w") as txt_file:

    #first output section to print to terminal and write to text file
    election_results_output = (
    "\nElection Results\n"
    "---------------------------------\n"
    "Total Votes: "+ str(total_votes) + "\n")

    print(election_results_output)
    txt_file.write(election_results_output)

    candidate_summary_output_temp = ""
    #for loop for winner
    for candidate in candidate_votes:

        #create variables for vote count and percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes)/float(total_votes)*100

        #use conditional to assess the candidate with largest vote count and assign to variables
        if (votes > winner_votes):
            winner_votes = votes
            winner_candidate = candidate

        #formatting not working - investigate this
        # candidate_summary_output = (
        #     "\n" + [candidate] + ":" + [vote_percentage] + "% (" + [votes] + ")\n"

        candidate_summary_output_temp += candidate + ": " + str(vote_percentage) + "% (" + str(votes) + ")\n" # ([candidate] + [vote_percentage] + [votes])
    print (candidate_summary_output_temp)
        #txt_file.write(candidate_summary_output_temp)

    winner_candidate_output = (
        f"-------------------------\n"
        f"Winner: {winner_candidate}\n"
        f"-------------------------\n")
    print(winner_candidate_output)
    txt_file.write(winner_candidate_output)

# #final output/need to split out since voter output is within for loop to print & write
# print("Election Results")
# print("-------------------------")
# print("Total Votes: " + str(total_votes))
# print("-------------------------")
# print(voter_output)
# print("-------------------------")
# print("Winner: " + str(winner_candidate))
# print("-------------------------")
# print([candidate] + [vote_percentage] + [votes])


