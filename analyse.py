import os
import pandas as pd
import matplotlib.pyplot as plt

# Initialize a dictionary to store dataframes for each repository
repo_dfs = {}

# List of repository folders
repos = [
    "kafka_results/kafka_results",
    "nifi_results/nifi_results",
    "flink_results/flink_results",
    "commons-io_results/commons-io_results",
    "presto_results/presto_results"
]

# Iterate over each repository folder
for repo_folder in repos:
    repo_name = os.path.basename(repo_folder)  # Extract repository name from folder path
    versions = []
    avg_ccn_values = []

    # Iterate over subfolders
    for version_folder in sorted(os.listdir(repo_folder)):
        if version_folder.startswith("v"):
            version = version_folder[1:]  # Extract version number
            versions.append(int(version))

            # Read lizard.txt file
            file_path = os.path.join(repo_folder, version_folder, "lizard.txt")
            with open(file_path, "r") as file:
                lines = file.readlines()

            # Extract average cyclomatic complexity from the last line
            last_line_values = lines[-1].strip().split()
            avg_ccn = float(last_line_values[2])  # Average cyclomatic complexity (AvgCCN)
            
            # Append average cyclomatic complexity to the list
            avg_ccn_values.append(avg_ccn)

    # Create DataFrame for the repository
    repo_df = pd.DataFrame({
        "Version": versions,
        "AvgCCN": avg_ccn_values
    })

    # Store the DataFrame in the dictionary
    repo_dfs[repo_name] = repo_df

# Plot cyclomatic complexity for each repository
plt.figure(figsize=(10, 6))
for repo_name, repo_df in repo_dfs.items():
    plt.plot(repo_df["Version"], repo_df["AvgCCN"], marker='o', label=repo_name)

plt.xlabel("Version")
plt.ylabel("Average Cyclomatic Complexity (AvgCCN)")
plt.title("Change in Average Cyclomatic Complexity (AvgCCN) Across Repositories")
plt.xticks(repo_df["Version"], rotation=90)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
