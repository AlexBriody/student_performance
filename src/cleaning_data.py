import pandas as pd

def clean_data(df):
    # Add an 'id' column to the DataFrame
    df['id'] = range(1, len(df) + 1)
    
    df.columns = df.columns.str.replace(' ', '_').str.strip().str.lower()

    education_mapping = {
        0: 'none',
        1: 'primary education',
        2: '5th to 9th grade',
        3: 'secondary education',
        4: 'higher education'
    }

    df['medu'] = df['medu'].map(education_mapping)
    df['fedu'] = df['fedu'].map(education_mapping)

    return df
