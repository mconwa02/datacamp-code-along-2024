import pandas as pd

# Sample DataFrame on Bank Client Data from Kaggle
df = pd.read_csv(r"C:\dev\data\code_along\train.csv", sep=";")

# Adding a nested list for duration column which is the contract duration
df["annual_duration"] = [[i, i / 2] for i in df["duration"]]

# Adding a tuple column on campaign -number of contacts performed during this campaign to the client
df["campaign_limit"] = [(i, i**2) for i in df["campaign"]]

# Group by column 'marital' and apply a lambda function to aggregate
result = df.groupby("marital").apply(
    lambda x: pd.Series(
        {
            "balance_max": x["balance"].max(),
            "age_mean": x["age"].mean(),
            "annual_duration_flat": [
                x for sublist in x["annual_duration"].tolist() for x in sublist
            ],
            "campaign_limit_concat": "".join(
                str(item) for item in x["campaign_limit"].tolist()
            ),
        }
    ),
    include_groups=False,
)


if __name__ == "__main__":
    print(result)

