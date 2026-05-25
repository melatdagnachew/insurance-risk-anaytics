import pandas as pd

df = pd.read_csv(
    "data/MachineLearningRating_v3.txt",
    delimiter="|",
    low_memory=False
)
clean_df = df.drop_duplicates()

clean_df.to_csv(
    "data/insurance_cleaned.csv",
    index=False
)
