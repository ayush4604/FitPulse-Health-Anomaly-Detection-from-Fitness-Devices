import pandas as pd
from tsfresh import extract_features
from tsfresh.utilities.dataframe_functions import impute
from tsfresh.feature_extraction import ComprehensiveFCParameters, MinimalFCParameters

def load_data(filepath):
    df = pd.read_csv(filepath)
    if 'time_stamp' in df.columns:
        df['time_stamp'] = pd.to_datetime(df['time_stamp'])
    return df

def extract_ts_features(df, column_id='Id', column_sort='time_stamp', value_columns=None, kind='comprehensive'):
    if kind == 'minimal':
        settings = MinimalFCParameters()
    else:
        settings = ComprehensiveFCParameters()

    if value_columns is None:
        value_columns = [c for c in df.select_dtypes(include=['number']).columns if c not in [column_id, column_sort]]

    print("Extracting features with TSFresh...")
    extracted_features = extract_features(
        df, 
        column_id=column_id, 
        column_sort=column_sort,
        value_columns=value_columns,
        default_fc_parameters=settings
    )
    
    print("Imputing missing values...")
    impute(extracted_features)
    
    return extracted_features

def compute_manual_features(df, group_col='Id', value_cols=['heart_rate', 'steps']):
    valid_cols = [c for c in value_cols if c in df.columns]
    
    if not valid_cols:
        return pd.DataFrame()

    funcs = ['mean', 'std', 'min', 'max', 'skew']
    
    stats = df.groupby(group_col)[valid_cols].agg(funcs)
    kurt = df.groupby(group_col)[valid_cols].apply(lambda x: x.kurtosis())
    kurt = kurt.rename(columns={c: f"{c}_kurt" for c in valid_cols})
    
    stats.columns = ['_'.join(col).strip() for col in stats.columns.values]
    
    result = pd.concat([stats, kurt], axis=1)
    
    return result
