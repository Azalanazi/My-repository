#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from pycaret.classification import predict_model, load_model

def load_data(filepath):
    """
    Loads Churn data into a DataFrame from a string filepath.
    """
    df = pd.read_csv('/Users/newuser/Downloads/prepped_Churn_data.csv')
    return df


def make_predictions(df):
    """
    Uses the pycaret best model to make predictions on data in the df dataframe.
    """
    model = load_model('GBC')
    predictions = predict_model(model, data=df)
    predictions.rename({'Label': 'Churns_prediction'}, axis=1, inplace=True)
    predictions['Churns_prediction'].replace({1: 'Churn', 0: 'No Churn'},
                                            inplace=True)
    return predictions['Churns_prediction']


if __name__ == "__main__":
    df = load_data('data/prepped_Churn_data.csv')
    predictions = make_predictions(df)
    print('predictions:')
    print(predictions)

