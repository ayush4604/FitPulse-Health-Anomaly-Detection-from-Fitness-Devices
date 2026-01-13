# Milestone 3: Anomaly Detection and Visualization Report

## Objective
The goal of this milestone was to implement anomaly detection on the fitness dataset to identify irregular patterns in heart rate and sleep activity. We employed **Prophet** for time-series forecasting and statistical thresholding to detect anomalies.

## Steps Followed

1.  **Data Loading & Preparation**:
    - Loaded the snapshot dataset from `data/cleaned_fitness_data.csv`.
    - **Simulation Strategy**: Since the source file contained single-point snapshots, we **seeded a historical simulation** (30 days) using the actual heart rate and step count values from the top 5 users in the dataset. This created a realistic time-series baseline for analysis.

2.  **Anomaly Detection Methodology**:
    - **Modeling**: We used **Facebook Prophet** to model the daily trend for Heart Rate and Sleep metrics.
    - **Forecasting**: Identifying the expected baseline (`yhat`) for each day.
    - **Residual Analysis**: Calculated residuals (`actual - expected`).
    - **Thresholding**: Defined anomalies as data points where the residual deviated by more than **2 standard deviations** from the mean error.

3.  **Visualization Output**:
    - **Heart Rate Anomalies**: Line charts tracking daily average heart rate for 5 users, with red markers highlighting statistically significant deviations (spikes/dips).
    - **Sleep Pattern Anomalies**: Similar tracking for total sleep minutes, flagging days of unusual sleep duration.
    - **Combined Overview**: A summary bar chart aggregating the number of anomalous days per user across metrics.

## Tools Used
-   **Python**: Primary programming language.
-   **Prophet**: Time-series forecasting and trend analysis.
-   **Pandas & NumPy**: Data manipulation and simulation.
-   **Matplotlib**: Visualization.

## Key Insights and Visualizations

### Heart Rate Anomalies
The chart below shows the daily average heart rate for 5 users. Red points indicate days where the heart rate significantly deviated from the Prophet-predicted trend.

![Heart Rate Anomalies](visualizations/heart_rate_anomalies.png)

### Sleep Pattern Anomalies
The chart below tracks "Total Sleep Minutes" per day. Anomalies (e.g., sleep deprivation or oversleeping) are flagged based on residual thresholds.

![Sleep Patterns](visualizations/sleep_anomalies.png)
