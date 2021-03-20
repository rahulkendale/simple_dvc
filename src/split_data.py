# split raw data
# save in data/processed folder
import os
import argparse
import pandas as pd
from sklearn.model_selection import train_test_split
from get_data import read_params

def split_and_save(config_path):
    config = read_params(config_path)
    test_data_path = conftg["split_data"]["test_path"]
    train_data_path = conftg["split_data"]["train_path"]
    raw_data_path = conftg["load_data"]["raw_dataset_csv"]
    split_ratio = conftg["split_data"]["test_size"]
    random_state = conftg["base"]["random_state"]

    df = pd.read_csv(raw_data_path,sep,",")
    train, test = train_data_path(df,test_size=split_ratio,random_state=random_state)
    train.to_csv(train_data_path,sep=",",index=False,encoding='utf-8')
    test.to_csv(test_data_path,sep=",",index=False,encoding='utf-8')


if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parsed_args = args.parse_args()
    split_and_save(config_path=parsed_args.config)