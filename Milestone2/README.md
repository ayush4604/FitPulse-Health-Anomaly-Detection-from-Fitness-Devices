# Milestone 2: Feature Extraction and Modeling

## Objective
The primary objective of Milestone 2 is to derive meaningful insights from the preprocessed fitness datasets. This involves extracting statistical and time-series features, modeling trends to identify anomalies, and clustering users based on behavioral patterns. These steps lay the foundation for the advanced anomaly detection tasks in subsequent milestones.

## Datasets Used
- **Source**: `cleaned_fitness_data.csv` (Output from Milestone 1).
- **Description**: A processed dataset containing normalized fitness metrics aligned to 1-minute intervals.
- **Key Columns**:
  - `Id`: User identifier.
  - `time_stamp`: UTC timestamps for each record.
  - `heart_rate`: Beats per minute (BPM).
  - `step_count`: Number of steps taken.
  - `sleep_tracking`: Categorical sleep state (e.g., awake, asleep).

## Steps Performed

### 1. Feature Extraction
- **Tools**: `tsfresh`, `pandas`.
- **Process**:
  - Extracted basic statistical features (Mean, Standard Deviation, Skewness, Kurtosis) for heart rate and steps.
  - Utilized `tsfresh` to automatically extract complex time-series features such as absolute energy, spectral density, and autocorrelation.
  - Imputed missing values in the extracted feature set.

### 2. Trend Modeling
- **Tools**: `Facebook Prophet`.
- **Process**:
  - Modeled the temporal trends of heart rate data.
  - Forecasted expected heart rate values with confidence intervals.
  - Identified potential anomalies where actual values deviated significantly from the predicted trend (falling outside confidence bounds).

### 3. Clustering Behavioral Patterns
- **Tools**: `scikit-learn` (`KMeans`, `PCA`).
- **Process**:
  - Standardized the extracted features to ensure equal weighting.
  - Applied K-Means clustering (k=3) to group users/time-windows into distinct behavioral profiles.
  - Reduced the dimensionality of the feature space using PCA (Principal Component Analysis) to visualized the clusters in 2D.

## Tools and Libraries Used
- **Language**: Python 3.8+
- **Libraries**:
  - `pandas`, `numpy`: Data manipulation.
  - `matplotlib`, `seaborn`: Visualization.
  - `tsfresh`: Automatic time-series feature extraction.
  - `prophet`: Time-series forecasting.
  - `scikit-learn`: Machine learning (Clustering, PCA, Scaling).

## Key Observations
- **Seasonality**: Heart rate data exhibits clear daily (circadian) rhythms.
- **Anomalies**: Prophet successfully identifies spikes in heart rate that deviate from the expected baseline trend.
- **User Groups**: Clustering reveals distinct groups of activity patterns, likely corresponding to different activity levels (e.g., sedentary vs. active periods).



---
**How to Run**:
1. Install dependencies: `pip install -r requirements.txt`
2. Run the notebook: `Milestone2_Analysis.ipynb`
