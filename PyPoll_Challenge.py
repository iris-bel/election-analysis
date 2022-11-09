# The data we need to retreive
# 1. The total number of votes cast
# 2. A complete list of candidaes who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_results.txt")

# Initialize a total vote counter
total_votes = 0

# Candidate options and candidate votes
candidate_options = []
candidate_votes = {}

# Participating counties and votes per county
counties = []
county_votes = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Track largest county and its voter turn out
largest_county = ""
voter_turnout = 0

# Open the election results and read the file
with open(file_to_load) as election_data:

    # To do: read and analyze the data here
    file_reader = csv.reader(election_data)
    # Read and print the header row
    headers = next(file_reader)
    
    # Print each row in the CSV file
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1 
        # Get the candidate name from each row
        candidate_name = row[2]
        # Get the county name from each row
        county = row[1]

        # Add candidate name to candidate list if not already in list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

        if county not in counties:
            counties.append(county)
            county_votes[county] = 0
        county_votes[county] += 1 

# Save the results to our text file
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal
    election_results = (
        f"Election Results\n"
        f"------------------------------------------\n"
        f"Total Votes = {total_votes:,}\n"
        f"------------------------------------------\n"
        f"County Votes:\n")
    print(election_results, end="")
    # Save the final vote count to the text file
    txt_file.write(election_results)

    for county in county_votes:
        turnout = county_votes[county]
        turnout_percentage = float(turnout)/float(total_votes) *100
        county_results = (f"{county}: {turnout_percentage:.1f}% ({turnout:,})\n")
        print(county_results)
        txt_file.write(county_results)

        if (turnout > voter_turnout):
            voter_turnout = turnout
            largest_county = county

    voter_turnout_summary = (
        f"------------------------------------------\n"
        f"Largest County Turnout: {largest_county}\n"
        f"------------------------------------------\n")
    print(voter_turnout_summary)
    txt_file.write(voter_turnout_summary)

    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        votes_percentage = float(votes)/float(total_votes) * 100
        candidate_results = (f"{candidate_name}: {votes_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal
        print(candidate_results)
        # Save the candidate results to txt file
        txt_file.write(candidate_results)

        # Print the winning candidate's results to the text file
        if (votes > winning_count) and (votes_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = votes_percentage
            winning_candidate = candidate_name

    # Print Winning info
    winning_candidate_summary = (
        f"------------------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"------------------------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's name to the txt file
    txt_file.write(winning_candidate_summary)

# Print the candidate vote dictionary
#print(candidate_votes)

# Print the candidate list
#print(candidate_options)

# Print the total votes
#print(total_votes)