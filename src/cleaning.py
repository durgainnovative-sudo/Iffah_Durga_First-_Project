{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 0,
   "id": "cb8b855a-fdeb-4ab7-99c3-d186ad679b64",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "",
   "name": ""
  },
  "language_info": {
   "name": ""
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
import pandas as pd
import json

def load_csv(path):
    return pd.read_csv(path)

def load_json(path):
    with open(path) as f:
        data = json.load(f)
    return pd.json_normalize(data)

def standardize_columns(df):
    df.rename(columns=lambda x: x.strip().lower().replace(' ', '_'), inplace=True)
    return df

def handle_missing(df):
    df.fillna(0, inplace=True)
    return df

def remove_duplicates(df):
    df.drop_duplicates(inplace=True)
    return df

def merge_datasets(df1, df2, on_keys):
    return pd.merge(df1, df2, on=on_keys, how='outer')

def main_cleaning(csv_path, json_path, merge_keys, output_path):
    df_csv = load_csv(csv_path)
    df_json = load_json(json_path)

    # Apply cleaning functions
    df_csv = remove_duplicates(handle_missing(standardize_columns(df_csv)))
    df_json = remove_duplicates(handle_missing(standardize_columns(df_json)))

    # Merge datasets
    df_merged = merge_datasets(df_csv, df_json, merge_keys)

    # Save cleaned data
    df_merged.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")
    return df_merged