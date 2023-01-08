import csv
import os
csvpath = os.path.join('Resources', 'election_data.csv')
# Open the CSV file and read the rows into a list
with open(csvpath, 'r') as f:
    rows = list(csv.reader(f))

# Extract the candidate names from the rows
candidates = [row[2] for row in rows[2:]]

# Calculate the total number of votes cast
num_votes = len(candidates)

# Create a list of the candidates who received votes
candidate_names = list(set(candidates))

# Create a dictionary to store the total number of votes received by each candidate
candidate_votes = {name: 0 for name in candidate_names}

# Iterate through the candidates list and update the candidate_votes dictionary with the number of votes received by each candidate
for name in candidates:
    candidate_votes[name] += 1

# Calculate the percentage of votes received by each candidate
candidate_percentages = {name: (votes / num_votes) * 100 for name, votes in candidate_votes.items()}
# Convert the candidate percentages to whole number percentages
whole_number_percentages = {name: int(round(percentage)) for name, percentage in candidate_percentages.items()}
# Find the candidate who received the most votes
winner = max(candidate_votes, key=candidate_votes.get)

# Print the results
print("Total number of votes:", num_votes)
print("Candidates:", candidate_names)
print("Votes received by each candidate:", candidate_votes)
print("Percentage of votes received by each candidate:")
for name, percentage in whole_number_percentages.items():
    print(f"{name}: {percentage}%")
print("Winner:", winner)

output_path = os.path.join("Analysis",'results.txt')
with open(output_path, 'w') as f:
    f.write("Total number of votes: " + str(num_votes) + "\n")
    f.write("Candidates: " + str(candidate_names) + "\n")
    f.write("Votes received by each candidate:\n")
    for name, votes in candidate_votes.items():
        f.write(f"{name}: {votes}\n")
    f.write("Percentage of votes received by each candidate:\n")
    for name, percentage in whole_number_percentages.items():
        f.write(f"{name}: {percentage}%\n")
    f.write("Winner: " + str(winner) + "\n")
