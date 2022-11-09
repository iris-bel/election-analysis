# Analysis of Congressional Election

## Overview of Project
This project is an election audit of a recent local congressional election. The following analysis of the election results aims to complete the following tasks:

1. Calculate the total number of votes cast
2. Get a complete list of participating candidates
3. Calculate the total number of votes cast for each candidate
4. Calculate the voter turnout for each county
5. Calculate the percentage of votes from each county out of the total count
6. Determine the county with the highest turnout
7. Calculate the percentage of votes cast for each candidate
8. Determine the winner og the election based on popular vote

## Resources
* Data Source: election_results.csv
* Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Election Audit Results
The analysis of the election reveals that:
* There were 369,711 votes cast in the election
* The participating candidates were:
      - Charles Casper Stockham
      - Diana DeGette
      - Raymon Anthony Doane
* The distribution of votes per county was:
      - Jefferson County accounted for 10.5% of the total votes with 38,855 votes cast
      - Denver County accounted for 82.8% of the total votes with 306,055 votes cast
      - Arapahoe County accounted for 6.7% of the total votes with 24,801 votes cast
* The largest voter turnout was in Denver County
* The election results were:
      - Charles Casper Stockham received 23.0% of the vote and 85,213 total votes
      - Diana DeGette received 73.8% of the vote and 272,892 total votes
      - Raymon Anthony Doane received 3.1% of the vote and 11,606 total votes
* The winner of the election was Diana DeGette

## Election Audit Summary
In its current form, this script can be used for any election involving multiple counties/geographical regions and/or multiple candidates as long as the data .csv file is formatted the way the original file is formatted. This script can currently handle processing election results for an election with more counties and more candidates than the example that we have here.

Currently, our code determines the winner of the election based on a simple majority of votes. This calculation can be tailored to the requirements of the voting system in question. For instance, if the election we plan to analyze requires that a candidate must receive over 50% of the vote in order to win, we can add a line of code to check whether the winning_count variable is greater than 50% of the total_votes before confirming the winning_candidate.

In addition to changing the conditions that lead to a winning candidate, the script can be expanded to handle the analysis of multiple election decisions, as local elections often involve voting on multiple goverment positions and proposals. The script can be expanded to perform the same analysis that it currently performs on the candidate column on additional columns containing voting data on other candidates and propositions. 

Ultimately, the modifications that can be made on this script are endless and depend primarily on the specifications of the specific election and the electoral rules of the region.
