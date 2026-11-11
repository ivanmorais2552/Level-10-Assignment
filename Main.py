import pandas as pd

# Read the CSV file and use Team as the index
df = pd.read_csv("cfb.csv", index_col="Team")

# Ask the user for a season
input_season = int(input("\nEnter a season to analyze: "))

# Check if the season exists
if input_season in df["Season"].values:

    # Filter and sort teams by wins
    df = df[df["Season"] == input_season]

    # Create a dictionary for the four categories
    categories = {
        "10 or more wins": [],
        "8-9 wins": [],
        "6-7 wins": [],
        "Fewer than 6 wins": []
    }

    # Loop through each team and organize by wins
    for team in df.index:
        wins = df.loc[team, "Win"]

        if wins >= 10:
            categories["10 or more wins"].append(team)
        elif wins >= 8:
            categories["8-9 wins"].append(team)
        elif wins >= 6:
            categories["6-7 wins"].append(team)
        else:
            categories["Fewer than 6 wins"].append(team)

    # Display the results
    print(f"\nCollege Football Results for {input_season}")

    for category in categories:
        print(f"\n{category}:")

        for team in categories[category]:
            print(team)

else:
    print("The selected year is not available.")
