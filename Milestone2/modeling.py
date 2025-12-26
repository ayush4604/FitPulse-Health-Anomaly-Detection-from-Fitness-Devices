import pandas as pd
from prophet import Prophet
from sklearn.cluster import KMeans, DBSCAN
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

def fit_prophet_model(df, date_col='time_stamp', value_col='heart_rate', periods=60, freq='min'):
    """
    Fits a Prophet model and forecasts future values.
    
    Args:
    - df: Input dataframe.
    - date_col: Name of column with datetime.
    - value_col: Name of column with values to forecast.
    - periods: Number of periods to forecast forward.
    - freq: Frequency of the time series (e.g., 'min', 'H', 'D').
    
    Returns:
    - model: Trained Prophet model.
    - forecast: DataFrame containing forecast results.
    """
    # Prepare data for Prophet
    # Prophet expects columns 'ds' and 'y'
    data = df[[date_col, value_col]].rename(columns={date_col: 'ds', value_col: 'y'}).dropna()
    
    # Sort by date
    data = data.sort_values('ds')
    
    model = Prophet()
    model.fit(data)
    
    future = model.make_future_dataframe(periods=periods, freq=freq)
    forecast = model.predict(future)
    
    return model, forecast

def detect_anomalies_prophet(df, forecast, date_col='time_stamp', value_col='heart_rate'):
    """
    Identifies anomalies where actual values are outside the Prophet confidence intervals.
    """
    # Merge original data with forecast
    # Ensure date_col is datetime
    df[date_col] = pd.to_datetime(df[date_col])
    
    results = pd.merge(df[[date_col, value_col]], forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']],
                       left_on=date_col, right_on='ds', how='inner')
    
    results['anomaly'] = (results[value_col] < results['yhat_lower']) | (results[value_col] > results['yhat_upper'])
    results['importance'] = abs(results[value_col] - results['yhat'])
    
    return results

def perform_clustering(features_df, method='kmeans', n_clusters=3, eps=0.5, min_samples=5):
    """
    Performs clustering on a feature set.
    """
    # Standardize the data
    # Drop any non-numeric columns if passed, assuming index is ID or handled before
    numeric_data = features_df.select_dtypes(include=['number', 'float', 'int'])
    
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(numeric_data.dropna())
    
    if method == 'kmeans':
        model = KMeans(n_clusters=n_clusters, random_state=42)
        clusters = model.fit_predict(scaled_features)
    elif method == 'dbscan':
        model = DBSCAN(eps=eps, min_samples=min_samples)
        clusters = model.fit_predict(scaled_features)
    else:
        raise ValueError("Invalid clustering method. Choose 'kmeans' or 'dbscan'.")
        
    return clusters, scaled_features

def visualize_clusters_pca(scaled_features, clusters):
    """
    Visualizes clusters in 2D space using PCA.
    """
    pca = PCA(n_components=2)
    pca_components = pca.fit_transform(scaled_features)
    
    df_pca = pd.DataFrame(data=pca_components, columns=['PC1', 'PC2'])
    df_pca['Cluster'] = clusters
    
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='PC1', y='PC2', hue='Cluster', data=df_pca, palette='viridis', s=100)
    plt.title('User Behavioral Clusters (PCA Reduced)')
    plt.show()
