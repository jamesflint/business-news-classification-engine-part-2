# Create a dataframe containing all the labelled text data from the Curation Corp JSONs

import json
import time
import argparse
import os
import pandas as pd
from pandas.io.json import json_normalize

columns = ["Title", "PublishedDate","Body","Source_name","Source_url","Category"]
index = np.arange(1)
all_articles_df = pd.DataFrame(columns=columns, index=index)

for filename in os.listdir("./data/"):
    if filename.endswith(".json"):
        #with open(os.path.join("./data/", filename)) as f:
        #    content = f.read()
        
        # Load json as string
        articles = json.load(open(os.path.join("./data/", filename)))

        # Normalise (i.e. breakout) nested Sources into Title and Url fields
        norm_articles_json = json_normalize(articles, "Sources")
        sources_df = norm_articles_json[["Title", "Url"]].copy()

        # Rename columns to maintain consistency with training data
        new_sources_df = sources_df.rename(columns={"Title": "Source_name", "Url": "Source_url"})

        # Load original articles as Pandas dataframe
        articles_df = pd.read_json(open(os.path.join("./data/", filename)))

        # Select the other relevant columns
        cleaned_articles_df = articles_df[["Title", "PublishedDate", "Body"]].copy()

        # Concatenate the relevant columns with the normalised sources columns
        full_articles_df = pd.concat([cleaned_articles_df, new_sources_df], axis = 1)

        # Drop rows containing NaNs
        full_articles_nn = full_articles_df.dropna(how="any")

        # Add a column containing the category (i.e. topic) label
        label = os.path.splitext(filename)[0]
        category = []
        for row in full_articles_nn['Body']:
            category.append(label)
        full_articles_nn["Category"] = category
        all_articles_df = pd.concat([all_articles_df, full_articles_nn], axis=0)
        
all_articles_df = all_articles_df.drop([0])

# Randomly reshuffle the order of the articles so they aren't grouped by topic
shuffled_df = all_articles_df.sample(frac=1).reset_index(drop=True)

# Drop all columns except title and content
shuffled_df = shuffled_df.drop(["PublishedDate", "Source_name", "Source_url"], axis=1)

# Create an extra column combining title and content into a single field, "text"
shuffled_df["Text"] = shuffled_df["Title"] + shuffled_df["Body"]

# Export the file to a CSV for later import
shuffled_df.to_csv("shuffled_df.csv")

# Create a more balanced dataset for later use
